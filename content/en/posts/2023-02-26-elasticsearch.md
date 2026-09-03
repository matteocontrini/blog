---
title: "Elasticsearch isn't as scary as it seems"
date: 2023-02-26T19:00:00+01:00
lastmod: 2023-02-26T19:00:00+01:00
slug: elasticsearch-not-scary-as-it-seems
summary: "After using Elasticsearch for a while, I can say that it's not scary as people think. Here are some thoughts."
showtoc: true
---

In the past year or so, I've had to build a search engine for some websites a couple of times. This led me to consider and explore multiple **search indexing products**.

When I started my research I had a prejudice about Elasticsearch: everyone was saying that is a huge piece of software, heavy, hard to manage, hard to learn, etc.

For this reason, I initially considered only Elasticsearch alternatives, like [Meilisearch](https://www.meilisearch.com/) and [Typesense](https://typesense.org/). These products are advertised as much lighter search engines that are easier to learn an deploy, and with a better overall developer experience.

While that's definitely true, after using Elasticsearch in production for a while I can comfortably say that **Elasticsearch and the Elastic stack in general aren't as scary as most people think**.

## Some thoughts on Elasticsearch

- Elasticsearch is a JVM-based application and is indeed not very light on memory. However, **memory usage is something that can be controlled through configuration** (heap size settings) and adjusted depending on how much data you have in your index. When you're starting a project and have a small index, Elasticsearch will need little memory, probably no more than what your database instance needs.
- If you're not into self-hosting, **Elastic Cloud** is the official managed service from Elastic and **it works very well**, in my experience. Plus, it's quite **affordable**: the cheapest configuration you can deploy costs about 20€ for an entire ELK stack (no high availability), which includes Elasticsearch, Kibana and Enteprise search. These are deployed on three separate machines on AWS or other cloud providers. That seems a good deal, isn't it? (Of course pricing goes up as soon as you need HA or other features.)
- Elasticsearch's **query language (DSL)** is surely **complex and advanced** but also very powerful. While some might initially find it intimidating, it's an **extremely powerful way to build queries**. While Meilisearch and Typesense make it easy to run basic search queries, as soon as you need something more complex you'll probably be disappointed. Elasticsearch's query language has **tons of features** that solve pretty much every conceivable scenario. Off the top of my head: nested queries, compound queries (`dis_max`, etc.), custom scores, boosting, custom tokenizers, token filters and character filters, etc. As soon as you work on some non-trivial data or queries, these are features you'll find useful.
- **Elasticsearch evolves very fast**: there's a company behind it and they keep delivering improvements and new features.
- If you think the DSL query language is not for you, Elastic Cloud also includes **Enteprise Search/App Search**. It basically wraps Elasticsearch to provide a **simplified way of building a custom search engine** on your data or even website. It's very intuitive to use and keeps improving. You will however lose some of the customization options provided by the query DSL.
- **Kibana is a pleasure to use**. I've spent days in the development console and it just works very well. The visualization features are also very polished and keep improving.

## Learning Elasticsearch

How do you learn Elasticsearch? I personally **wouldn't recommend starting from the official documentation**. It's very good as a reference (it's extremely thorough), but **doesn't provide a clear learning path**. There's just a lot of content and it's not very clear what you should learn first.

What I personally did to learn Elasticsearch is to watch [Bo Andersen's course on Udemy](https://www.udemy.com/course/elasticsearch-complete-guide/): Bo is an excellent teacher and is very good at making things easy to understand. The course is very well organized and clearly conveys the **most important concepts** that are otherwise **scattered around in the documentation**. He also has a course on Kibana.

Once you get an idea of how Elasticsearch works, you'll find that **the documentation becomes much easier to navigate and understand**. It's an invaluable resource and it happened to me very rarely that the answer wasn't there.

## Conclusion

To summarize, if you have **basic search needs** and you think you'll never need more advanced queries or features, Meilisearch and Typesense are probably for you. They're inspired by Algolia and do an excellent work of making search work well out of the box.

However, if you want the **best of the industry** and you're worried that Elasticsearch might be too hard, don't be: it can be learned quite rapidly and it's definitely worth it!

I left out some considerations from this article: for example, Elasticsearch isn't useful for search only and can also be used for other use cases, like analyzing and visualizing logs, so it depends on your requirements. Also, much depends on the scale of your data. For example, Meilisearch [admits](https://blog.meilisearch.com/why-should-you-use-meilisearch-over-elasticsearch/) that Elasticsearch is a better choice if you have many large documents.

That's it for now. I hope this helped, if you have any questions or doubts feel free to leave a comment below.
