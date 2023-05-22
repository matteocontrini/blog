---
title: "Using Vite to bundle JS/CSS in ASP.NET Core MVC"
date: 2023-05-21T22:30:00+02:00
lastmod: 2023-05-22T10:00:00+02:00
slug: aspnet-core-vite
summary: "Vite is a popular build tool for frontends. Here's how to integrate it in an ASP.NET Core MVC multi-page application."
showtoc: true
---

In this article we're going to explore how to integrate [**Vite**](https://vitejs.dev/) for building (and bundling) JavaScript/CSS files in an **ASP.NET Core application**.

The following is what we're going to achieve in brief. If the setup you have in mind is different, you can probably still take inspiration from this.

- We're creating a **Multi-Page Application** (MPA), not an SPA. This means we'll use Razor templates for HTML generation and Vite for JavaScript and CSS. This setup was tested with ASP.NET Core MVC (7.0) but it should work with Razor Pages too.
- We will be using the [`Vite.AspNetCore`](https://github.com/Eptagone/Vite.AspNetCore) library, which does a lot of things for us. Thanks to the author for making our lives simpler.
- The solution will work differently depending on whether we're in a production environment:
  - In the **development** environment, we'll be proxying the requests for static files to the Vite dev server, which will be running in background in "watch" mode
  - In **production**, the assets will be built at build time and served from the web root, without the Vite CLI playing any role after the build
- We will make sure to not lose ASP.NET Core features like referencing images and other assets from `wwwroot` (with IDE auto-complete) or assets versioning (`asp-append-version="true"`). You'll still be able to use the Vite `public` directory if you want, but I think using `wwwroot` is a better experience during development.
- We will use Tailwind CSS to demonstrate how to use CSS in this setup, but you're free to use anything else that is compatible with Vite.
- For the sake of the example we won't be using TypeScript.

## File structure

The following is the file structure we'll get to at the end of the article.

As a starting point we're using an empty ASP.NET Core MVC project (of which you will recognize folders like `Views` and `Controllers`).

```
ViteTest/
├─ Properties/...
├─ Controllers/...
├─ Views/...
├─ node_modules/...
├─ wwwroot/
├─ Assets/
│  ├─ main.js
│  ├─ main.css
├─ dist/
│  ├─ main.js
│  ├─ main.css
│  ├─ manifest.json
├─ ViteTest.csproj
├─ package.json
├─ package-lock.json
├─ vite.config.js
├─ postcss.config.js
├─ tailwind.config.js
ViteTest.sln
```

Here are some important things to notice:

- All the configuration files, like `package.json` and `vite.config.js`, will be placed in the root of the ASP.NET Core project (and not of the solution).
- The source JavaScript/CSS files are going to be in the `Assets` directory
- In production, the bundled output will be generated at build time and placed in the `dist` directory, together with the `manifest.json` that tells how to map each entry point to its output bundle. You don't need to create the `dist` directory manually.
  - Note that we're not including the file hash in the output file names, since we'll use the fingerprinting feature provided by ASP.NET Core (which adds `?v=` as a query string parameter).
- The classic web root `wwwroot` is still there and it's the place where you're going to put other static assets (images, icons, etc.) that are not processed by Vite.
  - Note that both `dist` and `wwwroot` are going to be web roots in our implementation.
- `postcss.config.js` and `tailwind.config.js` are Tailwind CSS-related configuration files.

## Vite configuration

Let's start from the Vite configuration. This is the content of the `vite.config.js` file:

```js
export default {
    appType: 'custom',
    root: 'Assets',
    build: {
        manifest: true,
        outDir: '../dist',
        emptyOutDir: true,
        assetsDir: '',
        rollupOptions: {
            input: {
                main: 'Assets/main.js',
            },
            output: {
                entryFileNames: '[name].js',
                chunkFileNames: '[name].js',
                assetFileNames: '[name].[ext]'
            }
        },
    },
    server: {
        port: 5173,
        strictPort: true,
        hmr: {
            clientPort: 5173
        }
    }
}
```

Let's go through it:

- `root` defines the root directory for the Vite application. In our case it's `Assets`, where the source JS/CSS files are located.
- `manifest` enables the creation of the `manifest.json` file, which contains the mapping between the inputs and the outputs. This will be used later in the .NET application to discover the output file names. In our case the setup is simple enough that input file names correspond to output file names, but in general this is the correct way of doing it. You can learn more about this in [Backend integration](https://vitejs.dev/guide/backend-integration.html) in the Vite docs.
- `outDir` is the directory where Vite will put the bundled files. In our case it's `../dist`, relative to the `Assets` directory. Since the `dist` directory is outside the Vite root, we need to explicitly allow Vite to clean the directory before build, with the `emptyOutDir` option.
- `assetsDir` is set to an empty string so that output files are placed directly in `dist` and not in `dist/assets` (the default).
- in `rollupOptions.input` we specify the entry points of the application. Here we have a single `main` entry point corresponding to the `Assets/main.js` file. The `output` overrides the output file names to remove the hashes. If you want hashes, just remove the `output` key.
- the `server` options enforce the use of port `5173` and makes sure that the WebSockets client for Hot Module Replacement (HMR) connects directly to the development server (instead of going through the proxy, as we will see).

You've probably noticed that there's no mention of CSS. That's because in Vite we import CSS files through JavaScript. Here's the content of the `main.js` file:

```js
import './main.css';
```

The `main.css` can be an empty file for now.

Note that this is not CSS-in-JS: the processed CSS will be output as a "normal" CSS file.

At this point you can create the `package.json` and install Vite:

```sh
# don't forget to cd to the project directory before running these commands
npm init -y
npm install -D vite
```

Modify the `package.json` and add the `dev` and `build` npm scripts:

```json
{
  "name": "vitetest",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "devDependencies": {
    "vite": "^4.3.8"
  }
}
```

You can test that the build is working correctly (without ASP.NET Core being involved, for now) by running `npm run build`.

The output should tell you which output files were generated:

```sh
❯ npm run build

> build
> vite build

vite v4.3.8 building for production...
✓ 2 modules transformed.
../dist/manifest.json  0.19 kB │ gzip: 0.10 kB
../dist/main.css       4.98 kB │ gzip: 1.56 kB
../dist/main.js        0.02 kB │ gzip: 0.04 kB
✓ built in 278ms
```

The `manifest.json` file will look like this:

```json
{
  "main.css": {
    "file": "main.css",
    "src": "main.css"
  },
  "main.js": {
    "css": [
      "main.css"
    ],
    "file": "main.js",
    "isEntry": true,
    "src": "main.js"
  }
}
```

You can also check that `npm run dev` starts correctly without errors.

## Integrating Vite with ASP.NET Core

The next step is to integrate the Vite build with the ASP.NET Core application.

First, install the [`Vite.AspNetCore`](https://github.com/Eptagone/Vite.AspNetCore) package with Nuget.

We now have to prepare for two different situations: development and production. Let's start by making things work in the development environment.

### Development

In the services section of `Program.cs`, add Vite:

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllersWithViews();
builder.Services.AddViteServices(); // <--
```

Then add the middleware for the development server:

```csharp
if (app.Environment.IsDevelopment())
{
    app.UseViteDevMiddleware();
}
```

According to [this issue](https://github.com/Eptagone/Vite.AspNetCore/issues/12) it's best to add the middleware as the last middleware, but in my experience it seems to work just fine even if you put it somewhere above.

Now, modify your `_ViewImports.cshtml` and enable the Vite tag helpers:

```
@addTagHelper *, Vite.AspNetCore
```

Next, modify `_Layout.cshtml` and add the following lines:

```html
<link rel="stylesheet" vite-href="~/main.js" asp-append-version="true" />
<script type="module" vite-src="~/main.js" asp-append-version="true"></script>
```

When rendering the Razor templates these lines will be replaced with different stuff depending on whether we're in development or production. The [README](https://github.com/Eptagone/Vite.AspNetCore) of the project explains how this works in greater detail.

At this point, if you run the Vite development server:

```sh
npm run dev
```

and start the ASP.NET Core application, things should already work.

If you look at the generated HTML the two lines above should have been replaced by something like:

```html
<script type="module" src="/@vite/client"></script>
<script type="module" src="/main.js?v=-URFENx0A-QQSd6xM_aJKqamPAVZGytZ5O5bI017vZk"></script>
```

Which is the standard way of integrating Vite with custom backends in development.

If you want the development server to be run automatically when you start the application, `Vite.AspNetCore` [has an option](https://github.com/Eptagone/Vite.AspNetCore#configuration) for that.

One further thing you can verify is that we're still able to refer static files from the `wwwroot` directory. For example, this line of code would work correctly and we'd still have the IDE autocomplete available:

```html
<img src="~/dotnet.svg" asp-append-version="true" width="50" height="50" />
```

The generated HTML would be:

```html
<img src="/dotnet.svg?v=ckU8b02NWzo9KQihdtOs-DgVSfR6kALDD7yUZ2NU584" alt="dotnet" width="50" height="50" />
```

Note that the development server doesn't use the `dist` folder.

### Production

For production, what you typically want is to generate the output files at build time and then have them served statically.

Run `npm run build` manually so that the `dist` directory is populated with JS/CSS bundles. We'll see how to automate this step later.

To make ASP.NET Core read static files from the `dist` directory, we need to change the web root path. At the same time, we'd like to retain the ability of using the "old" `wwwroot` directory to embed additional static files from there.

To achieve this, we need to replace the default web root file provider with a [composite file provider](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-7.0#serve-files-from-multiple-locations) which reads static files from both `dist` and `wwwroot`. We also change the default web root path to `dist` since `Vite.AspNetCore` uses that to find the files.

Here's how you can do it:

```csharp
if (!app.Environment.IsDevelopment())
{
    var webRootProvider = new PhysicalFileProvider(Path.Combine(builder.Environment.ContentRootPath, "wwwroot"));
    var distProvider = new PhysicalFileProvider(Path.Combine(builder.Environment.ContentRootPath, "dist"));
    var compositeProvider = new CompositeFileProvider(webRootProvider, distProvider);
    app.Environment.WebRootFileProvider = compositeProvider;
    app.Environment.WebRootPath = distProvider.Root;
}

app.UseStaticFiles();
```

If you run the application with the production environment you'll notice that the `<head>` now contains:

```html
<link rel="stylesheet" href="/main.css?v=1i5SKik2NbXlYrQ_wIJhSUNplJr5ZIvLEm7y0bCmFeg" />
<script type="module" src="/main.js?v=-URFENx0A-QQSd6xM_aJKqamPAVZGytZ5O5bI017vZk"></script>
```

Which are the CSS and JavaScript bundles, respectively. The Vite library uses the `manifest.json` file to map the source files to the output files (in this case they have the same names, but in more complex setups they probably won't).

Note that the `manifest.json` will be served publicly along with the other output files. If that's a problem for you, you can implement a middleware to stop those requests, or simply change the manifest file name to something less discoverable.

Finally, you can automate the execution of the `npm run build` command by adding a pre-build task to your `csproj` file. A basic example follows but you can think of [more complex configurations](https://www.meziantou.net/running-npm-tasks-when-building-a-dotnet-project.htm).

```xml
<Target Name="ViteBuild" BeforeTargets="BeforeBuild" Condition=" '$(Configuration)' == 'Release' ">
    <Exec Command="npm run build" />
</Target>
```

To make sure that both `wwwroot` and `dist` are copied to the publish directory when publishing the project, add the following configuration to your `csproj` file:

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
    <!-- ...omitted... -->

    <!-- Copy `wwwroot` and `dist` -->
    <ItemGroup>
        <None Include="wwwroot/**" CopyToPublishDirectory="PreserveNewest" />
        <None Include="dist/**" CopyToPublishDirectory="PreserveNewest" />
    </ItemGroup>

    <!-- Don't copy npm files -->
    <ItemGroup>
        <Content Update="package-lock.json" CopyToPublishDirectory="Never" />
        <Content Update="package.json" CopyToPublishDirectory="Never" />
    </ItemGroup>
</Project>
```

Also, if you use git make sure to add the `dist` and `node_modules` folders to your `.gitignore`.

## Adding Tailwind CSS

Just to demonstrate that this setup works with typical frontend development workflows, we can add Tailwind CSS to the mix.

Follow the official [installation instructions](https://tailwindcss.com/docs/guides/vite) for Vite and make sure to change `tailwind.config.js` so that Tailwind knows about the Razor views:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './Views/**/*.cshtml',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

You can then easily test that Tailwind CSS works correctly in both development and production.

The development server will recreate the pruned/trimmed CSS file based on your Razor views as soon as you make changes to them. In this way, you don't need to restart the application nor rebuild anything manually.

Note that for this experience to work you probably need to enable [Razor runtime compilation](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/view-compilation?view=aspnetcore-7.0&tabs=visual-studio#enable-runtime-compilation-conditionally) during development.

## Conclusion

In this article we explored how to integrate Vite with ASP.NET Core in a multi-page application (MPA). This is only one of the possible ways of using Vite in a web application, but I hope it was useful in some way.

If you have questions or feedback, feel free to leave a comment below.
