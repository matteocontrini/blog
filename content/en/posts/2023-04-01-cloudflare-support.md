---
title: "Surreal adventures with Cloudflare's (paid) support"
date: 2023-04-01T15:30:00+02:00
lastmod: 2023-04-01T15:30:00+02:00
slug: cloudflare-support
summary: "In my experience, Cloudflare's paid support is unbelievably bad, they seem to miss basic understanding of how their products and features work."
showtoc: true
---

In 2021, I discovered that Cloudflare's page rules didn't correctly handle redirects to URLs where the fragment symbol was present twice (e.g. `https://www.cloudflare.com/##test`). In fact, Cloudflare replaced the `##` part with the symbol `$`. I know what you're thinking: it doesn't make any sense to have `##` in the URL, but that's how some websites work and that was the requirement for the redirect.

It took more than 20 back-and-forth emails to have Cloudflare's support understand the issue, classify it as as bug and finally fix it, after several non-sense responses which had nothing to do with the actual issue. Note that Cloudflare's email support is part of their paid plans, but the support staff appears to be entirely unqualified and failed to understand basic concepts related to how Cloudflare works, multiple times.

A year later, in 2022, I noticed a similar issue with Cloudflare Pages. Cloudflare Pages is a way to deploy static websites on Cloudflare's infrastructure. One of the features is redirects, which can be defined in a file named `_redirects`, part of your source code. This time the redirect would duplicate the `##` part. For example, `https://www.cloudflare.com/##test` would become `https://www.cloudflare.com/##test##test`.

I contacted Cloudflare's email support and it took 18 messages to have them understand and fix the issue, an unbelievable waste of resources for such a simple issue to understand.

The whole conversation follows. It includes Cloudflare's support:

- Not understanding that the page rule was to be looked for on my domain and not on the destination domain of the redirect.
- Claiming that URLs with fragments are processed on the client side and therefore "page rules will never work", which doesn't make any sense, since we're talking about server-side redirects.
- Claiming that "the current issue you are seeing is expected because page rules won’t apply to custom domain [on Cloudflare Pages]", which is incorrect if you're proxying the domain through Cloudflare (with Pages as the origin).
- Linking StackOverflow questions unrelated to the issue about hash signs in the URL.
- Suggesting that I disable strict TLS on the configuration of my domain on Cloudflare, while providing a curl warning of the destination domain, clearly unrelated to my Cloudflare's TLS configuration.
- Trying to blame Hugo (a \*static* website generator) for the issue, twice.
- Claiming that there are "no signs of us manipulating the extra content on the URL", after providing extensive proof of that.
- Deploying a page on Cloudflare Pages with a `<meta>` HTML redirect, while we were debugging a bug in Cloudflare's redirect feature.

## Pages Rules bug (2021)

### 2021-09-23 (me)

>Hello, I configured a page rule to redirect to a page that contains an anchor with two `#`. This is the URL:
>
>```text
>https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-custom3
>```
>
>Unfortunately when deployed Cloudflare redirects to:
>
>```text
>https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/$heading-custom3
>```
>
>Why is that? Is there some kind of escaping needed?

### 2021-09-23 (Cloudflare)

>Hi there,
>
>Thanks for contacting Cloudflare support. My name is Yuri and I will be looking into this ticket for you.
>We're sorry to read that you're experiencing difficulties.
>
>Upon checking your account, you have several domains registered on your Cloudflare account.
>Which domain you are trying to create Forward rule?
>Have you already created page rule?
>
>Looking forward to your reply.
>
>Yuri | Cloudflare Support

### 2021-09-25 (me)

>These are the steps to reproduce the issue:
>
>- create a new redirection page rule (on any domain) with this destination URL:
>
>```text
>https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-custom3
>```
>
>- open the page URL in the browser and notice that Cloudflare directs to this URL instead:
>
>```text
>https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/$heading-custom3
>```
>
>Thanks.

### 2021-09-28 (Cloudflare)

>Hi Matteo,
>
>Thanks for contacting Cloudflare Support. My name is Kiki and I will be looking into this ticket for you.
>I'm sorry to read that you're experiencing difficulties.
>
>I have run a curl to the URL you mentioned, we can see this site is not on Cloudflare, please note that Page Rules require an "Orange Clouded" DNS record for your page rule to work. Page Rules won't apply to hostnames that don't exist in DNS or aren't being directed to Cloudflare.
>
>```bash
>curl -svo /dev/null https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-custom3
>*   Trying 34.90.10.138...
>* TCP_NODELAY set
>* Connected to wdc.wholesale.telecomitalia.it (34.90.10.138) port 443 (#0)
>* ALPN, offering h2
>* ALPN, offering http/1.1
>* successfully set certificate verify locations:
>*   CAfile: /etc/ssl/cert.pem
>  CApath: none
> ...omitted...
>* Using HTTP2, server supports multi-use
>* Connection state changed (HTTP/2 confirmed)
>* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
>* Using Stream ID: 1 (easy handle 0x7f84a000d600)
>> GET /tw_servizi/vula/ HTTP/2
>> Host: wdc.wholesale.telecomitalia.it
>> User-Agent: curl/7.64.1
>> Accept: */*
>>
>* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
>< HTTP/2 200
>< date: Tue, 28 Sep 2021 15:31:17 GMT
>< server: Apache
> ...omitted...
><
>{ [8823 bytes data]
>* Connection #0 to host wdc.wholesale.telecomitalia.it left intact
>* Closing connection 0
>```
>
>I hope this helps but please let us know if you have further questions.
>
>[Understanding and Configuring Cloudflare Page Rules (Page Rules Tutorial)](https://support.cloudflare.com/hc/en-us/articles/218411427-Understanding-and-Configuring-Cloudflare-Page-Rules-Page-Rules-Tutorial-?source=search)
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-09-28 (me)

>I'm sorry, why should the *destination* URL in a redirection page URL be served by Cloudflare? That doesn't make any sense. Please read again my last message, carefully.
>
>Thank you.

### 2021-09-29 (Cloudflare)

>Hi Matteo,
>
>Thanks for getting back to us.
>
>I am very sorry for previous confusion.
>
>- I have read through your previous messages. Could you please give me us additional information to assist you in a better place?
>- If you have created this page rule, please let us know on which domain you have created? We wanted to check how you exactly configure this page rule on your domain.
>
>Please send us a A HAR file demonstrating the issue you are seeing.
>
>Please respond with that information as soon as you can so we can continue to work with you to resolve your issue.
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-09-29 (me)

>Hello,
>
>I've created the page rule which can be tested with the following URL: `https://fibra.click/test`
>
>You can reproduce the issue as follows:
>
>```bash
>❯ curl -v https://fibra.click/test 2>&1 | grep -i "Location:"
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/$heading-custom3
>```
>
>As you can see, the destination URL is different. `##` became `$`, which is not something I expect.
>
>Thank you.

### 2021-10-01 (Cloudflare)

>Hi Matteo,
>
>Thanks for getting back to us.
>
>Please note that the path after the `#` sign is referred to as fragments and they are processed only on the client side and the client (browser) never forwards it to the server (Cloudflare).
>
>Source: https://tools.ietf.org/html/rfc3986#section-3.5
>
>```text
>   Fragment identifiers have a special role in information retrieval
>   systems as the primary form of client-side indirect referencing,
>   allowing an author to specifically identify aspects of an existing
>   resource that are only indirectly provided by the resource owner.  As
>   such, the fragment identifier is not used in the scheme-specific
>   processing of a URI; instead, the fragment identifier is separated
>   from the rest of the URI prior to a dereference, and thus the
>   identifying information within the fragment itself is dereferenced
>   solely by the user agent, regardless of the URI scheme.
>```
>
>I am afraid in your case targeting the request through page rule will never work because the server (Cloudflare) will never see a request containing the fragment.
>
>Hope this explains the issue, let us know if there's any other question for us.
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-10-01 (me)

>I'm sorry but I don't how this is even remotely related to the problem I'm reporting...
>
>I'm talking about a redirect that is done server-side by Cloudflare. It's a `Location` header. And that header contains the wrong value as I've demonstrated in previous messages.
>
>Please take a minute to read and give a sensible response.
>
>Thank you.

### 2021-10-06 (Cloudflare)

>Hi Matteo,
>
>Very sorry for previous confusion caused.
>
>After checking your domain fibra.click, we can see it is configured as Cloudflare pages Custom domain, so the current issue you are seeing is expected because page rules won't apply to custom domain.
>
>However, you can achieve this by using redirects on Cloudflare Pages, please check this public article for detailed steps: https://developers.cloudflare.com/pages/platform/redirects
>
>I hope this helps but please let us know if you have further questions.
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-10-06 (me)

>That's simply not true, I created the same page rule on another domain not using Cloudflare Pages and the issue is present there as well:
>
>```
>$ curl -v https://[omitted]/tim 2>&1 | grep -i location:
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/$heading-custom3
>```

### 2021-10-07 (Cloudflare)

>Hi Matteo,
>
>Thanks for getting back to us, sorry for the inconvenience.
>
>Upon reviewing your issue, we have opened an internal ticket with our Engineer team. The team will run some diagnostics, and we will keep you updated for any further details.
>
>In the meantime, I will put your ticket as 'on-hold' and please let me know if you have other qustions.
>
>Thanks for your patience!
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-10-15 (Cloudflare)

>Hi Matteo,
>
>Thanks for your patience!
>
>We have some updates from our Engineer team.
>
>- Could you please read through this public link: https://stackoverflow.com/questions/10850781/multiple-hash-signs-in-url and please let us know the reason you were trying to realize this redirect?
>
>https://www.rfc-editor.org/rfc/rfc3986
>
>Thank you!
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-10-15 (me)

>Hello,
>
>I'm not sure how this is relevant but that is how the destination page is coded, and it's not under my control. They have an anchor in the page which contains the hash symbol, so in the URL you see # twice.
>
>I can't change that but I don't think Cloudflare should break the URL when it happens.
>
>Thanks.

### 2021-10-18 (Cloudflare)

>Hi Matteo,
>
>Thanks for getting back to us.
>
>Thank you for providing the information. Sorry for the inconvenience!
>
>Just wanted to leave you a quick note to ensure you that our Engineer teams are working actively on your issue.
>
>Although we do not have an ETA, we shall keep you posted on any new findings.
>
>Thank you for your patience during the investigation period.
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-10-28 (Cloudflare)

>Hi Matteo,
>
>Thanks for your patience during investigation.
>
>Our engineer team has made some changes. This issue should have been fixed now.
>
>Could you please check from your side to see if you still have some issue?
>
>Thank you!
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-10-29 (me)

>Hello,
>
>As you can see by yourself, the issue is still there.
>
>```bash
>$ curl -v https://fibra.click/test 2>&1 | grep -i "Location:"
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/$heading-custom3
>```
>
>The `$` in the location should be `##`.
>
>Thanks.

### 2021-10-29 (Cloudflare)

>Hi Matteo,
>
>Thanks for getting back to us.
>
>I have run the curl just now and see the result as below:
>
>```bash
>curl -v https://fibra.click/test 2>&1 | grep -i "Location:"
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-custom3
>```
>
>Could you please try again?
>
>Thank you!
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-10-29 (me)

>Hello,
>
>I've just tried again and unfortunately I get the same issue.
>
>If it helps I'm attaching the full request and response.
>
>Thanks.

### 2021-10-29 (Cloudflare)

>Hi Matteo,
>
>Thanks for getting back to us with the full request.
>
>I have just reported to our Engineer team with your information. The team will run some diagnostics, and we will keep you updated for any further details.
>
>Thanks for your patience during investigation!
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-11-03 (Cloudflare)

>Hi Matteo,
>
>Thanks for your patience!
>
>Our engineer team has made some changes. This issue should have been fixed now.
>
>Could you please check from your side to see if you still have some issue?
>
>I hope this helps but please let us know if you have further questions.
>
>Kind regards
>
>Kiki | Customer Support Agent

### 2021-11-03 (me)

>Hello,
>
>I can confirm it's fixed, thank you very much!
>
>Have a nice day.

## Cloudflare Pages bug (2022)

### 2022-08-10 (me)

>Hello,
>
>I'm using Cloudflare Pages with a redirect that looks like the following, to be placed in the `_redirects` file:
>
>```text
>/tim https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-7
>```
>
>However the redirect is executed incorrectly:
>
>```bash
>$ curl -v https://fibra.click/tim 2>&1 | grep location
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-7##heading-7
>```
>
>Notice that instead of ending with `##heading-7` it ends with `##heading-7##heading-7`.
>
>I think this is a bug?
>
>Thanks.

### 2022-08-10 (Cloudflare)

>Hi Matteo,
>
>Thanks for contacting Cloudflare support, my name is Sean and I will help assist you.
>
>Anchors are not passed in the browser:
>
>The request is actually being passed to:
>
>```text
>https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/
>```
>
>Kind regards,
>
>Sean Eustace  
>Technical Support Engineer - Cloudflare

### 2022-08-10 (me)

>Thanks for the information but that has nothing to do with what I said.
>
>Please read the question again: Cloudflare Pages is applying a wrong redirect.
>
>Thanks.

### 2022-08-22 (Cloudflare)

>Hello Matteo,
>
>Thank you so much for your continued patience and update.
>As of now, I am trying to build an hugo app to try to replicate the same behavior.
>I would like the following test performed.
>
>This test is necessary so I can record the before and after behavior and see what may be overriding what.
>
>Please create a Page rule for `/tim` manually. We provide a guide on how to do that [here](https://support.cloudflare.com/hc/en-us/articles/4729826525965-Configuring-URL-forwarding-or-redirects-with-Page-Rules).
>Please confirm if the redirect with `#` appended, works as intended.
>Thanks for your patience and I will wait for your next update.
>
>Kind regards,
>
>Erick Monroy  
>Technical Support Engineer - Cloudflare

### 2022-08-23 (me)

>Hello,
>
>I have created a page rule as requested (redirect from `https://fibra.click/tim` to `https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-7`), and the redirect works correctly in this case.
>
>```bash
>❯ curl -v https://fibra.click/tim 2>&1 | grep location:
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-7
>```
>
>Let me know how we should proceed.
>
>Thanks.

### 2022-08-24 (Cloudflare)

>Hello again,
>
>Thanks for your cooperation. Can you please temporarily set this zone to "Flexible" mode under TLS/SSL here?
>
>From there, turn off the Page Rule and let Hugo's application try to redirect `/tim` again.
>
>From our end, the Full Strict mode appears to be complaining about:
>
>```text
>"https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/#%23heading-7": x509: certificate signed by unknown authority
>```
>
>The workaround would be to just rely on this Page rule for the redirect.
>
>Kind regards,  
>Erick Monroy  
>Technical Support Engineer - Cloudflare

### 2022-08-25 (me)

>Excuse me? This is a redirect, I'm not proxying, so changing the TLS settings has no effect. And even if I was, this obviously has no effect on the URL.
>
>I know I can use the page rule, but I'm here to report a bug so that it can be fixed.
>
>Thanks.

### 2022-08-31 (Cloudflare)

>Hello again,
>
>Thanks for the update and cooperation. This appears to be a setting that Hugo may need to have configured as mentioned [here](https://gohugo.io/content-management/urls/#ugly-urls) on the variables. I recommend deploying a sample html only Page and testing if the redirect works there.
>
>I am not seeing any signs of us manipulating the extra content on the URL.
>
>Alternatively, you can also this URL to test:
>https://developers.cloudflare.com/pages/get-started/#configure-your-deployment
>
>This will help determine if wholesale's website is potentially processing #'s different in comparison to our documentation.
>
>Kind regards,  
>Erick Monroy  
>Technical Support Engineer - Cloudflare

### 2022-09-03 (me)

>>*This appears to be a setting that Hugo may need to have configured*
>
>As you know, Hugo is a static site generator and plays no role in the Cloudflare Pages `_redirects` file, which is handled by Cloudflare and by Cloudflare alone when receiving requests. Before even getting to the static files. So no, Hugo has nothing to do with this issue and I shouldn't be here to explain it...
>
>>*This will help determine if wholesale's website is potentially processing #'s different in comparison to our documentation.*
>
>The destination website does no processing, this is Cloudflare redirecting to the wrong URL:
>
>```bash
>❯ curl -v https://fibra.click/tim 2>&1 | grep location:
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-7##heading-7
>```
>
>>*I am not seeing any signs of us manipulating the extra content on the URL.*
>
>I'm seeing it, see the example above, which I also put in the first email...

### 2022-09-07 (Cloudflare)

>Hello Matteo,
>
>Thanks for the update. I have deployed a .html Pages application and my redirect is working just fine on my end. https://redirect9000.pages.dev/
>
>Regardless, I still want our engineering team to take a second look.
>For our engineers to validate further, please disable the redirect from the Page rule in the meantime.
>
>I will provide another update as soon as I receive one from our engineering team.
>
>Kind regards,  
>Erick Monroy  
>Technical Support Engineer - Cloudflare

For the record, source code of `https://redirect9000.pages.dev/`:

```html
<!DOCTYPE html>
<html>
<head>
   <title>HTML Redirect</title>
   <meta http-equiv="refresh" content="3; url = https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-7" />
</head>
<body>
   <h1>Rediret test</h1>
   <p>You'll be redirected to an external ur in 3 seconds</p>
</body>
</html>
```

I didn't reply.

### 2022-09-27 (Cloudflare)

>Hello,
>
>Thanks for your continued patience. Our engineering team advised that this may be an issue with Ugly URLs as referenced [here](https://gohugo.io/content-management/urls/#ugly-urls). They recommended to give this a try to see if it helps with the redirection issue.
>
>Kind regards,  
>Erick Monroy  
>Technical Support Engineer - Cloudflare

### 2022-10-02 (me)

>Oh jesus...
>
>It's not Hugo, it's a Cloudflare bug and it's two months I've been trying to explain it to you.
>
>Deploy this simple project: https://github.com/fibraclick/cloudflare-pages-bug
>
>And you'll see that the redirect is applied incorrectly.
>
>```bash
>❯ curl -v https://cloudflare-pages-bug.pages.dev/tim 2>&1 | grep -i "Location: "  
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-7##heading-7
>```
>
>^^^ wrong location, different from the one in the _redirects file

### 2022-11-04 (Cloudflare)

>Hi Matteo,
>
>Stefano here, and thanks for getting back to us.
>In our internal debugging ticket, we were not able to reproduce the issue,
>
>We have this case opened, and I have added your comment in this issue,
>
>We will let you know in case we have any updates on your case.
>Thanks for your patience on that.
>
>Best,
>
>Stefano Grammenos | Cloudflare® Technical Support Engineer

### 2022-11-04 (Cloudflare)

>Matteo  
>Thanks for patience,
>
>Would you be able to add a domain to your pages and retry please, once you add a domain to your page, are you able to reproduce the issue?
>
>During my tests, on the affected URL I get a 302 redirect:
>
>```text
>< HTTP/2 302
>< date: Fri, 04 Nov 2022 16:13:04 GMT
>< content-type: text/plain;charset=UTF-8
>< content-length: 92
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-7##heading-7
>< access-control-allow-origin: *
>< referrer-policy: strict-origin-when-cross-origin
>< x-content-type-options: nosniff
>< report-to: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=tCZEJ360SER0syiroFgvAUv7hfkNZiiahqi6HAodTkVkP6iQDtVLQiTkl0vpZbj17wckAqJfqvhLcC0Dc3tLvqJHHI1GWyWk29WZ0AHULuqq5ijbSRYwOyoh0nhkz%2B7oojFUXjogwhmSabRaE4E%2BBk0%3D"}],"group":"cf-nel","max_age":604800}
>< nel: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
>< server: cloudflare
>< cf-ray: 764ea2898d85353e-RGN
>< alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
><
>{ [92 bytes data]
>* Connection #0 to host 172.66.46.210 left intact
>
>finished in 2.143s
>```
>
>here:
>
>```text
>< location: https://wdc.wholesale.telecomitalia.it/tw_servizi/vula/##heading-7##heading-7
>```
>
>In your project, If I am checking the correct project, I see a redirect:
>
>/// *screenshot of the "Redirects" tab in the Cloudflare Pages dashboard for the test project*
>
>
>So, you are building a redirect as described here:
>https://developers.cloudflare.com/pages/platform/redirects
>
>I am confused however with the second one shared earlier: https://github.com/fibraclick/wiki/blob/0a4dd39d1ddf35663dd6cacce88051f6e042d682/static/_redirects#L3
>
>Can I have the exact github that we need to check in order to identify the issue?
>Also if you can add a domain name in your project to have a full setup and see if this is also affecting this.
>
>Let us know
>
>Best,
>
>Stefano Grammenos | Cloudflare® Technical Support Engineer

### 2022-11-04 (me)

>Hi,
>
>thanks for the reply. Sorry, I'm not sure I understand what the confusion is about or what you need exactly. I'll try to recap, maybe it helps.
>
>I have two projects on Cloudflare Pages that show the issue.
>
>1) Project "fibraclick-wiki", the domain is https://fibra.click/
>
>The redirect is defined here: https://github.com/fibraclick/wiki/blob/41f75237fb1c1153618434f67dba15bdb01af111/static/_redirects#L3
>
>On both domains the 302 redirects take to the "wrong" URL, which is longer than it should. See Screenshot_1.png attached to see a proof of that.
>
>/// *Screenshot_1.png shows the curl command returning the wrong URL, side by side with the contents of the _redirects file*
>
>2) Project `cloudflare-pages-bug`, which is a simplified empty project containing just the redirects file. Domain is https://cloudflare-pages-bug.pages.dev/
>
>Redirect is defined here: https://github.com/fibraclick/cloudflare-pages-bug/blob/eb61e5ede24130dafc8cf01c77a9da7398e83711/_redirects#L1
>
>See Screenshot_2.png (attached) to see that the same issue is present.
>
>/// *Screenshot_2.png is the same as above but on the test domain*
>
>I don't think the custom domain affects the issue since it happens with or without it. Hugo (the static website generator) is obviously unrelated since I'm using the Cloudflare Pages redirects feature.
>
>Is there anything else you need? The bug seems pretty clear and reproducible to me.
>
>Thanks.

### 2022-11-19 (Cloudflare)

>Hello,
>
>Thanks for the update. I have followed up with our engineering team to examine further, more updates to come.
>
>Kind regards,  
>Erick Monroy  
>Technical Support Engineer - Cloudflare

### 2022-12-22 (Cloudflare)

>Hello,
>
>Thanks for your continued patience. I just wanted to let you know that our engineering team is still working on this issue.
>We will provide another update as soon as we receive one.
>
>Kind regards,  
>Erick Monroy  
>Technical Support Engineer - Cloudflare

### 2023-03-28 (Cloudflare)

>Hi Matteo,
>
>Apologies for the long radio silence.
>The issue has been identified and is being prepared to be patched with a future update/release patch with the Pages product Team.
>
>This would be the only update I can provide at the moment and the solution the Pages Team have provided, as it needs this major release.
>As of now the release code is ready but they still need to follow a specific schedule/window to ensure the code gets out without breaking other stuff.
>
>As such there is no definite timeline to get this out to production.
>
>Please do note this trouble has been acknowledged by Engineering and will be fixed in the future release.
>
>Thank you.
>
>Omar Shariff | Cloudflare Support
