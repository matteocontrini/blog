---
title: "Comparison of static website hosting services"
date: 2024-08-29T14:27:59+02:00
lastmod: 2024-08-29T14:27:59+02:00
slug: static-website-hosting
summary: "Here's a comparison of Netlify, Vercel, Cloudflare Pages, Render, AWS Amplify, Azure Static Web Apps and their main features."
showtoc: true
---

Here's a comparison of the most popular static website hosting services.

With static hosting I mean hosting of static HTML pages and their linked resources (CSS, JS, images, etc.).

Other than serving the static content with a **global CDN**, these services usually also take care of things like **CI/CD builds**, **atomic deployments**, **instant cache invalidation** and **preview deployments**, which often aren't easy to achieve (or not achievable at all) with simpler DIY storage+CDN solutions.

Below, the feature "rewrite" usually includes the ability to have a navigation fallback for single-page applications, and custom error pages.

## [Netlify](https://www.netlify.com/)

- ⚠️ CDN: only 6 locations on free/Pro plans, 70+ locations with very expensive *High Performance Edge* (enterprise plan)
- Bandwidth: 100 GB on the free plan (then $550 / TB), 1 TB on the Pro plan (then $550 / TB)
- ✅ Automatic hosted builds (CI/CD)
- ✅ GitHub commit checks
- ❌ No GitHub environments/deployments support
- ✅ Rollbacks
- ✅ Atomic deployments
- ✅ Instant cache invalidation
- ✅ Custom domain with HTTPS certificate and redirect
- ✅ Branch/PR preview environments, also on custom domain
- ✅ Rewrites/redirects/proxy
- ✅ Custom response headers
- ✅ DDoS/flood protection
- ✅ HTTP/2
- ❌ No HTTP/3
- ✅ IPv6

## [Vercel](https://vercel.com)

- ✅ CDN: 100+ PoPs (all plans)
- Bandwidth: 100 GB on the free plan, 1 TB on the Pro plan (then $150+ / TB)
- ✅ Automatic hosted builds (CI/CD)
- ✅ GitHub commit checks, environments/deployments
- ✅ Rollbacks
- ❓ Probably atomic deployments
- ✅ Instant cache invalidation
- ✅ Custom domain with HTTPS certificate and redirect
- ✅ Branch/PR preview environments, also on custom domain
- ✅ Rewrites/redirects/proxy
- ✅ Custom response headers
- ✅ DDoS/flood protection
- ✅ HTTP/2
- ❌ No HTTP/3
- ❌ No IPv6

## [Cloudflare Pages](https://pages.cloudflare.com/)

- ✅ CDN: full Cloudflare network on all plans (330 cities)
- Bandwidth: unlimited
- ✅ Automatic hosted builds (CI/CD)
- ✅ GitHub commit checks
- ❌ No GitHub environments/deployments support
- ✅ Rollbacks
- ❓ Probably atomic deployments
- ✅ Instant cache invalidation
- ✅ Custom domain with HTTPS certificate and redirect
- ⚠️ Custom domain requires Cloudflare NS
- ✅ Branch/PR preview deployments
- ❌ Preview deployments on custom domain are manual
- ✅ Rewrites/redirects
- ❌ No proxied paths
- ✅ Custom response headers
- ✅ DDoS/flood protection
- ✅ HTTP/2
- ✅ HTTP/3
- ✅ IPv6

## [Render](https://render.com/)

- ⚠️ CDN: unknown ("global CDN")
- Bandwidth: 100 GB on the free plan, 500 GB or 1 TB on paid plans, then $300 / TB
- ✅ Automatic hosted builds (CI/CD)
- ❓ GitHub commit checks, environments/deployments
- ✅ Rollbacks
- ❓ Probably atomic deployments
- ✅ Instant cache invalidation
- ✅ Custom domain with HTTPS certificate and redirect
- ✅ PR (not branch) preview environments
- ❌ No preview deployments on custom domain
- ✅ Rewrites/redirects
- ❌ No proxied paths
- ✅ Custom response headers
- ✅ DDoS/flood protection
- ✅ HTTP/2
- ✅ HTTP/3
- ❌ No IPv6

## [AWS Amplify Hosting](https://aws.amazon.com/amplify/hosting/)

- ✅ CDN: full CloudFront network, 600+ PoPs in 100+ countries
- Bandwidth: 5 GB on the free plan (12 months), then $150 / TB
- ✅ Automatic hosted builds (CI/CD)
- ❓ GitHub commit checks, environments/deployments
- ✅ Rollbacks
- ✅ Atomic deployments
- ✅ Instant cache invalidation
- ✅ Custom domain with HTTPS certificate and redirect
- ✅ PR (not branch) preview environments
- ✅ Preview deployments on custom domain (Route53 only)
- ✅ Rewrites/redirects
- ❌ No proxied paths
- ✅ Custom response headers
- ❌ No DDoS/flood protection included
- ✅ HTTP/2
- ✅ HTTP/3
- ❌ No IPv6 (officially)

## [Azure Static Web Apps](https://learn.microsoft.com/en-us/azure/static-web-apps/overview)

- ⚠️ CDN: limited locations by default, but on the paid plan you can enable the Front Door CDN (192 locations in 109 cities) for $17.52 / month
- Bandwidth: 100 GB on the free plan, $200 / TB on the paid plan
- ❌ No automatic hosted builds (CI/CD), a GitHub Actions workflow is required
- ❌ No GitHub commit checks, environments/deployments
- ❌ No rollbacks
- ✅ Atomic deployments
- ⚠️ Instant cache invalidation, but there's a max age of 30 seconds by default
- ✅ Custom domain with HTTPS certificate and redirect
- ✅ Preview environments, to be created through the GitHub action (I think)
- ❌ No preview deployments on custom domain
- ✅ Rewrites/redirects
- ❓ Unclear if proxied paths are supported
- ✅ Custom response headers
- ❌ No DDoS/flood protection included
- ✅ HTTP/2
- ❌ HTTP/3
- ✅ IPv6 (only with Front Door enabled)

I left out some features, like access control, form submissions, analytics, etc., which are sometimes included.

I also left out some simpler services, like GitHub Pages, DigitalOcean App Platform, Surge.sh, because they miss basic features like preview deployments or response headers. I also looked at Firebase Hosting but I find the docs incredibly confusing.
