---
title: "A list of free self-hosted Google Analytics alternatives"
date: 2022-08-20T21:00:00+02:00
lastmod: 2022-08-20T21:10:00+02:00
slug: google-analytics-alternatives
summary: "My notes on a few Google Analytics alternatives that can be self-hosted, are open source and free."
showtoc: true
---

I was looking for Google Analytics alternatives I could self host, for situations where paid analytics services are over budget.

The following are my notes on a few solutions that can be self-hosted, are open source and free.

Feel free to leave your thoughts or recommend other tools in the comments!

## Matomo Analytics

https://matomo.org/matomo-on-premise/

- The classic one. It's quite advanced but maybe a bit too complex? You might end up never looking at most pages (like with Google Analytics)
- The UI attempts to be modern but still feels old. It lacks of proper UI/UX design IMO
- It's been around for ages, definitely stable
- It might require a cookie consent for GDPR compliance. From what I understand it's possible to configure Matomo so that consent is not required but it's not what you get out of the box
- Real-time stats: there's a page that shows recent visits but it lacks a count of how many users are online (it only shows active users in the past 30 minutes)
- Actively developed by the company that offers the cloud product
- Built with PHP and requires MySQL. Easy deployment only if you already have a PHP setup, I'd say

## Plausible Analytics

https://plausible.io/

- Somewhat less advanced when compared to Matomo, but it still probably has everything you need
- Easy to use and beautiful design
- Born as a cloud product but released as open source for self-hosting, with all the features. The product has been around since 2019 and the company behind it has grown *a lot* recently
- +1 for weekly email reports and reports about traffic spikes
- It features a real-time dashboard and shows the number of current visitors
- No cookie consent required
- Built with Elixir, uses both PostgreSQL and ClickHouse as database systems, which are not easy requirements. Still quite easy to deploy with the provided Docker Compose file

## umami

https://umami.is/

- It seems to be similar to Plausible but with less features overall
- It's been around since 2020 and it's actively developed
- According to the website a paid cloud product is coming soon, which I think is good for the future and sustainability of the project
- Similarly to Plausible: nice design, real-time dashboard, count of online users
- No cookie consent required
- Written in Node.js, works with both PostgreSQL and MySQL. A bit easier to deploy than Plausible especially because there's no ClickHouse requirement
- Very promising overall!

## Fathom Lite

https://usefathom.com/lite

- The open source Lite version of the Fathom service
- It's [very limited](https://github.com/usefathom/fathom#fathom-lite-vs-fathom-analytics) in terms of features compared to the full product (which went closed-source), so I would consider it only for very basic needs
- Still, nicely designed
- No cookie consent required
- Should be easy to deploy even without Docker, being a Go application. Uses SQLite as a database (!)

## Ackee

https://ackee.electerious.com/

- Another product from 2019, again similar to Plausible but less advanced
- It seems to work well for tracking multiple websites in a single dashboard
- No real-time dashboard but there's an active visitors count
- No cookie consent required
- Development is kind of active but I'm seeing only bug fixes in the past year
- Built with Node.js and requires MongoDB. Should be easy to deploy provided you know how to manage a MongoDB instance

## Shynet

https://github.com/milesmcc/shynet

- Nice UI. Basic features you need are probably there, but...
- It seems it hasn't received much attention lately, I'm not sure where the project is going
- Built with Python, requires PostgreSQL

## GoatCounter

https://www.goatcounter.com/

- This is a weird one: basic service, with a basic-but-charming old-school UI
- Not very advanced, e.g. you can only filter by page
- No online users count/no real-time dashboard
- The developer doesn't work on the project full-time anymore, but fixes are still delivered from what I can tell
- There's a free managed service but only for non-commercial use
- No cookie consent required
- Built with Go ❤ + SQLite/PostgreSQL
