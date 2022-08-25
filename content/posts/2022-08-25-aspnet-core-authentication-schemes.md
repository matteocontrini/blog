---
title: "Working with custom authentication schemes in ASP.NET Core 6.0 Web API"
date: 2022-08-25T22:00:00+02:00
lastmod: 2022-08-25T22:00:00+02:00
slug: aspnet-core-authentication-schemes
summary: "How to define custom authentication schemes in ASP.NET Core 6.0, and why they're not enough to actually enforce authentication for your Web API."
showtoc: true
---

**ASP.NET Core** has support for both **authentication** and **authorization**. However, in my opinion the official documentation on the topic is sometimes a bit confusing or lacking, especially if you don't want to use Identity, don't have a UI, or don't like/want the opinionated authentication schemes that are included with the framework.

This article is an **introduction on how to use custom authentication schemes** to build a simple Web API application with authentication. You would use this approach if you wanted to implement, for example, session tokens-based authentication for your API.

## Authentication vs authorization

You probably already know the difference, but in ASP.NET Core the distinction is especially important, so let's refresh the concepts. It will later help understanding why stuff works in a way that you maybe wouldn't expect.

So, very briefly:

- **authentication** is about verifying that the user is who they say they are, usually by verifying that a token is valid;
- **authorization** is the process of determining whether a specific (authenticated) user is allowed to perform some action.

As we will see later, authentication alone is not enough to protect an API in ASP.NET Core, as it only means verifying a token (without actually enforcing that authentication is mandatory for an endpoint, for example).

## Authentication schemes

Let's start with authentication. In ASP.NET Core authentication is achieved with the use of **authentication schemes**:

- an authentication scheme is basically the piece of code that is responsible for authenticating users
- **there are many possible schemes**, since you can implement authentication in many different ways
- an application isn't necessarily limited to one authentication scheme, it can define more than one and **even use even more than one at the same time**
- an example of a scheme is the cookie authentication scheme, where the actual authentication code would consist of:
  - reading the cookie from the request;
  - verifying that it's valid;
  - providing the framework with an authentication ticket that certifies that the user has been successfully authenticated;
  - alternatively, if the user cannot be authenticated with the cookie the scheme code returns a failure result
- ASP.NET Core 6.0 ships with two authentication schemes:
  - the **cookie** authentication scheme
  - the **JWT token** authentication scheme
- these two schemes are **configurable to some extent**, but are still quite opinionated
  - for example, the cookie scheme builds a cookie that is encrypted and contains the claims (the properties of the user), which is something that you may want to avoid since the cookie can become large
- if you don't like how they work or if you have different requirements (e.g. using session tokens) **you can create a custom authentication scheme**

There are a few more details about authentication schemes that you can read about in the [overview page](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/?view=aspnetcore-6.0) of the official docs.

## Custom authentication schemes

At this point we're ready to write our own **custom authentication scheme**. We'll be using an (incomplete) implementation of session token authentication as an example.

Remember that authentication schemes are registered with the framework at startup. For example, when using the cookie scheme you would write something like this:

```c#
builder.Services.AddAuthentication()
    .AddCookie();
```

`AddCookie()` is a simple extension method that actually calls the generic `AddScheme()` method internally.

If you wanted to register a custom scheme, you would use exactly that `AddScheme()` method:


```c#
builder.Services.AddAuthentication()
    .AddScheme<TokenAuthenticationSchemeOptions, TokenAuthenticationSchemeHandler>(
        "Tokens",
        opts => {}
    );
```

As you can guess, when defining a new scheme you need to create an options class (`TokenAuthenticationSchemeOptions` in the example) and a handler that takes the authentication requests (`TokenAuthenticationSchemeHandler`). The handler must inherit from `AuthenticationHandler` or implement the `IAuthenticationHandler` interface. The first approach is a bit easier because the base abstract class provides a sensible default implementation for most methods. We'll see an example in a minute.

Other than specifying the **type of the options and of the handler** as generic types, the `AddScheme<TOptions, THandler>()` method takes the **name of the scheme** as the first argument. To avoid hardcoding it you would usually put it in a static class, but we'll keep it simple here.

The second argument allows you to assign the **options** of the scheme (defined as properties of the options class). If you don't have any, you can also pass `null`.

The authentication handler in its most basic form only implements the `HandleAuthenticateAsync` method, by overriding it. This method gets called automatically at every request to an endpoint (if authentication is enabled on the endpoint) through a middleware.

```c#
public class TokenAuthenticationSchemeHandler : AuthenticationHandler<TokenAuthenticationSchemeOptions>
{
    public TokenAuthenticationSchemeHandler(
        IOptionsMonitor<TokenAuthenticationSchemeOptions> options,
        ILoggerFactory logger,
        UrlEncoder encoder,
        ISystemClock clock) : base(options, logger, encoder, clock)
    {
    }

    protected async override Task<AuthenticateResult> HandleAuthenticateAsync()
    {
        // Read the token from request headers/cookies
        // Check that it's a valid session, depending on your implementation
        
        // If the session is valid, return success:
        var principal = new ClaimsPrincipal(new ClaimsIdentity("Test"));
        var ticket = new AuthenticationTicket(principal, this.Scheme.Name);
        return AuthenticateResult.Success(ticket);

        // If the token is missing or the session is invalid, return failure:
        // return AuthenticateResult.Fail("Authentication failed");
    }
}
```

If you run this code and then send an HTTP request to any controller/endpoint of your application, you'll notice that **the handler is not called**. Authentication is in fact **not enabled by default**. To enable it, there are two ways:

- setting a **default authentication scheme**
- **enabling *authorization*** and specifying the authentication scheme to use

To set a default authentication scheme, simply pass its name to the `AddAuthentication()` method:

```c#
builder.Services.AddAuthentication("Tokens") // <--
    .AddScheme<TokenAuthenticationSchemeOptions, TokenAuthenticationSchemeHandler>(
        "Tokens",
        opts => {}
    );
```

>**NOTE**: this behavior [is going to change](https://docs.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/default-authentication-scheme) in ASP.NET Core 7.0, where if you add only one authentication scheme it will be selected as the default one automatically.

If you run the code again and put a breakpoint in the handler you'll notice that the authentication handler is now indeed **called at every request**.

However this is not enough: if you change the handler code to return a **failure result** you would expect an error to be returned, but instead the controller code is executed anyway, **ignoring the authentication outcome**.

This is where **authorization** comes into play.

## Authorization

So far, we've implemented the authentication mechanism. Now we need to tell the framework **the rules that define which endpoints a user is authorized to access**.

Theoretically you could implement authorization by yourself. For example, you could use the `HttpContext.User.Identity.IsAuthenticated` property to return an error if the user is not authenticated:

```c#
[HttpGet()]
public IActionResult GetActuallyNothing()
{
    if (!HttpContext.User.Identity.IsAuthenticated) // <--
    {
        return StatusCode(401);
    }

    return Ok();
}
```

Using ASP.NET Core authorization is obviously a wiser choice. The simplest way to enable authorization is to **require authorization globally**, on every controller and action. It can be done in your startup code, as follows:

```c#
app.MapControllers().RequireAuthorization();
```

Now, if the authentication handler returns a failure result, the client will get a `401 Unauthorized` error. If you want to change the response you could override the `HandleChallengeAsync` method in the handler or tweak error handling globally.

What if you wanted to **whitelist some specific controller or action**, e.g. for implementing the login endpoint?

You can do that with the `[AllowAnonymous]` attribute:

```c#
[ApiController]
public class AuthController : ControllerBase
{
    [HttpGet("/login")]
    [AllowAnonymous] // <--
    public IActionResult Login()
    {
        // Create your token and store the associated session somewhere
        // Probably return the token in the response...
        return Ok();
    }
}
```

**An important detail**: even if you put the `[AllowAnonymous]` attribute, **the authentication handler will be executed anyway**. This is because `[AllowAnonymous]` indeed *allows* unauthenticated users but doesn't really care about authentication. In other words, the effect of `[AllowAnonymous]` is to **entirely bypass authorization** (in this case the one we've enabled with `RequireAuthorization()`) **without affecting authentication in any way**.

An alternative approach to the global `RequireAuthorization()` is to use the `[Authorize]` endpoint, which you can put on specific controllers or actions, like this:

```c#
[HttpGet("/secret")]
[Authorize] // <--
public IActionResult KindaSecret()
{
    return Ok();
}
```

Note that this works only because we've set the default authentication scheme in the `AddAuthentication()` call in the startup code. If we don't do it, we get an exception that explains the problem:

>***System.InvalidOperationException**: No authenticationScheme was specified, and there was no DefaultChallengeScheme found. [...]*

We can however still use the `[Authorize]` attribute by simply specifying the authentication scheme we want to use, like this:

```c#
[HttpGet("/secret")]
[Authorize(AuthenticationSchemes = "Tokens")] // <--
public IActionResult Secret()
{
    return Ok();
}
```

You can actually specify **multiple authentication schemes** at the same time (comma-separated) and also use **different authentication schemes** in different contexts.

To avoid passing the authentication scheme every time we can make it the default by creating a default authorization policy:

```c#
builder.Services.AddAuthorization(options =>
{
    options.DefaultPolicy = new AuthorizationPolicyBuilder()
        .AddAuthenticationSchemes("Tokens")
        .RequireAuthenticatedUser()
        .Build();
});
```

And then simply use `[Authorize]` on controllers and actions.

As you've seen there are many possible combinations of what you can do with the authentication and authorization mechanisms that come with ASP.NET Core. Which one to choose depends on your application requirements.

## Summary

Here's a few takeaways to summarize what we've seen:

- you can define many authentication schemes, whose handlers contain the actual authentication code
- if you choose a default authentication scheme...
  - the authentication handler will be called at each request, no matter what
  - to actually enforce authorization, use `RequireAuthorization()` or `[Require]`
  - to selectively disable authorization where already enabled, use `[AllowAnonymous]`
- if you don't set a default scheme...
  - you must explicitly choose an authentication scheme when enabling authorization, with `[Require(AuthenticationSchemes = "...")]`
  - the authentication handler will then be run only where you enabled authorization
  - to simplify the syntax and simply use `[Authorize]`, define a default authorization policy at startup

That's a wrap, I hope it helped!

Feel free to leave a comment if you have questions or feedback.
