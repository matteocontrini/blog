---
title: "Using Snowflake for database IDs"
date: 2024-12-24T16:30:10+01:00
lastmod: 2024-12-24T16:30:10+01:00
slug: snowflake-ef-core
summary: "A practical example of using Snowflake for database keys without a centralized service, with .NET and Entity Framework Core."
showtoc: true
---

When designing a database, the most common choice for primary keys and IDs has historically been **auto-incrementing numeric values**.

There are several reasons why you may want to not use that strategy: for example, avoiding leaking records count information (and the rate of new records) when IDs are exposed in URLs, avoiding the penalty of locks for generating the next number, or supporting distributed systems scenarios.

Alternative solutions involve masquerading IDs (e.g. [with Sqids](https://sqids.org/)), using **UUIDs** (which have their own set of problems, like possible suboptimal performance, long string representation, etc.) or **Snowflake IDs** and their variants.

The original version of Snowflake was designed by Twitter [in 2010](https://ws-dl.blogspot.com/2019/08/2019-08-03-tweetedat-finding-tweet.html) and consisted in a system to generate unique 64 bit numbers in the following format:

{{< fig src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Snowflake-identifier.png" caption="Wikimedia Commons. CC BY-SA 3.0" >}}

Specifically:

- The **timestamp** is the number of milliseconds since the chosen epoch. This allows for encoding almost 70 years of IDs.
- The application **instance** that generated the ID.
- A **sequence** to allow for multiple IDs in the same millisecond.

This design is especially suitable for distributed systems because it allows for up to 1024 instances generating IDs independently and concurrently, with the guarantee that they're not going to conflict. But it's also fine in simpler systems where you have few (or even one) instances of the application.

You still need a way to assign unique instance IDs, something that Twitter solved with a centralized service (Apache ZooKeeper), but we'll see a much simpler solution later.

The Snowflake format has been adapted and used by several other social networks, like [Discord](https://discord.com/developers/docs/reference#snowflakes), [Instagram](https://instagram-engineering.com/sharding-ids-at-instagram-1cf5a71e5a5c), and [Mastodon](https://github.com/mastodon/mastodon/blob/877090518682b6c77ba9bdfa0231afd56daec44d/lib/mastodon/snowflake.rb).

The structure of the ID can in fact be changed depending on specific needs. For example, you could use microseconds instead of milliseconds, assigning more bits to the timestamp part. Or, if you need to be able to generate more than 4k IDs per second per instance you could add more bits to the sequence part, and so on.

## Snowflakes in .NET

*I'm using .NET, C# and Entity Framework Core a lot lately, so the rest of this article will provide a complete example of using Snowflake IDs as database primary keys. This approach can be easily ported to other languages and frameworks.*

In .NET, there's an open source library called [**NewId**](https://github.com/RobThree/IdGen) that implements the Snowflake ID format.

It's actually very flexible and it allows to **override the default Snowflake structure** and decide how many bits are allocated to the three parts.

You can also **set your own epoch** so you know when you'll run out of IDs.

Here's an example of a static C# class using the NewId library to generate IDs:

```csharp
public static class Snowflake
{
    public static readonly IdStructure Structure = IdStructure.Default;

    private static readonly DateTimeOffset Epoch = new(2024, 1, 1, 0, 0, 0, TimeSpan.Zero);

    private static readonly IdGenerator? generator = new IdGenerator(
        0,
        new IdGeneratorOptions(Structure, new DefaultTimeSource(Epoch))
    );

    public static long New()
    {
        return generator.CreateId();
    }
}
```

You would use it like this:

```csh
long id = Snowflake.New();
```

The NewId library is thread-safe out of the box.

With an epoch of January 2024, this configuration will generate valid IDs until 2093. It won't be my problem anymore.

## Generating a unique instance ID

With Snowflake, it's your responsibility to make sure that the instance ID (called **generator ID** by NewId) is uniquely assigned to only one application instance at any given time.

It turns out you can use the database itself to assign generator IDs. The basic idea is that you store the last assigned generator ID in a database table and increment it when a new application instance boots.

To prevent concurrency issues, a solution is to use the built-in **concurrency check** feature of Entity Framework Core to prevent the same generator ID from being used by multiple instances.

You can actually implement this solution with any database and stack, as we will see by looking at the generated SQL command.

Here's a possible implementation in .NET. I have an Entity Framework Core entity that looks like this:

```csharp
public class SnowflakeGeneratorEntity
{
    public int Id { get; set; }
    
    [ConcurrencyCheck]
    public required int Value { get; set; }
}
```

The table in the database must have only one row, which can be created with EF Core data seeding:

```csharp
builder.Entity<SnowflakeGeneratorEntity>()
  		 .HasData(new SnowflakeGeneratorEntity { Id = 1, Value = 0 });
```

When the application starts, **I extract the current generator value, increment it and save it to the database**. If the generator ID exceeds the maximum allowed value, I reset the generator ID to zero.

Here's a .NET background service that does this automatically:

```csharp
public class SnowflakeInitializer(IServiceProvider serviceProvider, ILogger<SnowflakeInitializer> logger)
    : IHostedService
{
    public async Task StartAsync(CancellationToken cancellationToken)
    {
        using IServiceScope scope = serviceProvider.CreateScope();

        var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();

        SnowflakeGeneratorEntity? generator = await db.SnowflakeGenerators
            .SingleAsync(cancellationToken);

        if (generator == null)
        {
            throw new InvalidOperationException("Could not find existing Snowflake generator in the database");
        }

        // We increment by 1 before using the value so that the db will contain the current generator value
        generator.Value += 1;

        // Wrap around if we reach the max value
        if (generator.Value > Snowflake.Structure.MaxGenerators - 1)
        {
            generator.Value = 0;
        }

        Snowflake.Initialize(generator.Value);

        logger.LogInformation("Snowflake initialized with generator value {GeneratorValue}", generator.Value);

        await db.SaveChangesAsync(cancellationToken);
    }

    public Task StopAsync(CancellationToken cancellationToken)
    {
        return Task.CompletedTask;
    }
}
```

The `Snowflake` class must be updated to allow the initialization of the generator from the background service:

```csharp
public static class Snowflake
{
	  // ...omitted...

    private static IdGenerator? generator;

    public static void Initialize(int generatorId)
    {
        generator = new IdGenerator(
            generatorId,
            new IdGeneratorOptions(Structure, new DefaultTimeSource(Epoch))
        );
    }

    public static long New()
    {
        if (generator == null)
        {
            throw new InvalidOperationException("Snowflake generator has not been initialized.");
        }

        return generator.CreateId();
    }
}
```

Entity Framework will generate the following SQL query when saving the updated value:

```sql
UPDATE "SnowflakeGenerators" SET "Value" = @newValue
WHERE "Id" = 1 AND "Value" = @oldValue;
```

If the value field was changed by another process while it was incremented, this query won't do anything (no rows affected), EF Core will detect the concurrency issue and throw an exception.

This approach removes the need of a centralized "ticketing" system like in the original Twitter implementation based on ZooKeeper.

I've been using this implementation in production for some time and it's worked flawlessly so far.

## Value generators vs manual generation

To automatically generate primary keys as Snowflake IDs in Entity Framework Core, you can use value generators.

A value generator for Snowflake could look like this:

```csharp
public class SnowflakeValueGenerator : ValueGenerator<long>
{
    public override long Next(EntityEntry entry)
    {
        return Snowflake.New();
    }

    public override bool GeneratesTemporaryValues => false;
}
```

The value generator must then be attached to the entity where you're using a Snowflake ID as the primary key:

```csharp
builder.Entity<UserEntity>()
  .Property(x => x.Id)
  .ValueGeneratedNever()
  .HasValueGenerator<SnowflakeValueGenerator>();
```

Where `Id` is a non-nullable `long` property which will be populated automatically by the value generator when it has the default value of 0.

Note that I haven't tested this (I'm not sure whether `ValueGeneratedNever()` is needed), because I'm using a different approach.

Specifically, I'm using the [StronglyTypedId](https://github.com/andrewlock/StronglyTypedId) library to avoid the "primitive obsession" problem.

My `UserEntity` type in the example above actually looks like this:

```csharp
public class UserEntity
{
    public required UserId Id { get; set; }
	  // ...
}
```

Where the `UserId` is a type wrapping a `long` value:

```csharp
[assembly: StronglyTypedIdDefaults(Template.Long, "long-efcore")]

[StronglyTypedId]
public partial struct UserId;
```

When creating an entity, I would manually create the Snowflake ID, like this:

```csharp
var user = new UserEntity
{
    Id = new UserId(Snowflake.New())
}
```

I've found this to be a minor inconvenience that actually adds more flexibility: I can know the ID of the new entity in advance, before saving, and therefore use it in complex insertions.

This is useful in scenarios like a user sign up, where you need to create the user, maybe the organization it belongs to, the membership, etc., and you can do that all at once if you know the user ID.

---

There are certainly many variations of this approach, and it can also easily ported to other languages and frameworks.

Let me know your thoughts below!

*Thanks to Rob Janssen and Andrew Lock for creating and maintaining the libraries mentioned in this post.*

{{< dmarcwise >}}
