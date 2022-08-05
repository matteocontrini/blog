---
title: "A minimal Node.js TypeScript setup"
date: 2022-08-05T10:00:00+02:00
lastmod: 2022-08-05T10:00:00+02:00
slug: minimal-nodejs-typescript-setup
summary: "Confused about how to setup TypeScript with a Node.js backend application? Here's the most minimal setup to make it work."
showtoc: true
---

If you're just starting out with TypeScript with Node.js, you might have found yourself confused by the fact that there isn't a single way of configuring TypeScript with your project.

While there are lots of tools and frameworks, in this article I'll introduce **a minimal setup for a new empty Node.js application without using any framework**. This is something I wish the official TypeScript documentation had (or maybe I missed it).

## Initialization

The first thing you'll want to do is initialize the project with `npm init`.

You can then install TypeScript as a development dependency:

```sh
npm install --save-dev typescript
```

The source TypeScript files will be placed in the `src` directory, so this is the structure you should have by now:

```sh
├── package.json
├── package-lock.json
└── src
    └── index.ts
```

## `tsconfig.json`

While you could theoretically already use the TypeScript compiler to check types and transpile the `.ts` file to `.js`, you would usually create a `tsconfig.json` file to properly configure the compiler.

Since we're using Node.js to build a backend application (thus not for the browser), we can choose a configuration that is specific for the Node.js version we're using. This makes sure that modern JavaScript features are used directly if available, avoiding polyfills, etc.

At the time of writing, the Node.js LTS version is 16. The TypeScript team publishes a base `tsconfig.json` configuration for Node.js 16 with the [`@tsconfig/node16`](https://www.npmjs.com/package/@tsconfig/node16) npm package.

So let's install the package:

```sh
npm install --save-dev @tsconfig/node16
```

And create a `tsconfig.json` file with the following content:

```json
{
    "extends": "@tsconfig/node16/tsconfig.json",
    "compilerOptions": {
        "outDir": "dist"
    },
    "include": [
        "src/**/*.ts"
    ]
}
```

The most important part is the `extends` property, where we're basically importing the base configuration provided by the `@tsconfig/node16` package. This base configuration contains some good defaults which we're going to take a look to in a moment. This is also the reason why we don't need to specify almost any `compilerOptions` (you might find pretty long `tsconfig.json` files online), since the base config file already contains best practises.

The `include` property defines where to look for TypeScript files to compile. In this case we're including all `.ts` files in the `src` directory. If we didn't put it, TypeScript would for example attempt to compile the `node_modules` directory. In some examples you might also see the `exclude` property being used to exclude `node_modules`, but with the structure we're using here it's not required (since `node_modules` is outside `src`).

The compiler option `outDir` tells TypeScript where to output the transpiled `.js` files. If not specified, `.js` files are placed in the same directory where the corresponding `.ts` files lie.

You might sometimes find the following options in `tsconfig.json` examples:

- [`baseUrl`](https://www.typescriptlang.org/tsconfig#baseUrl), which is supposed to allow non-relative imports. For example you might get to a situation where you write `import helper from '../../helper'`, and you instead want to simplify the thing and write `import helper from 'helper'`. In our example this would require setting `baseUrl` to `src`, so that when you import `helper` TypeScript knowns that you're actually importing `src/helper`, starting from the root. This indeed [works](https://www.typescriptlang.org/docs/handbook/module-resolution.html) at the TypeScript level, meaning that the compiler doesn't complain anymore, but it doesn't work in practice because the Node.js module resolution doesn't work in the same way and it wouldn't find the module at runtime (Node.js looks for non-relative imports only in the `node_modules` directory). Making this work [isn't straightforward](https://github.com/microsoft/TypeScript/issues/10866) as it requires modifying paths in the output files, so I'll leave it for another time;
- [`rootDir`](https://www.typescriptlang.org/tsconfig#rootDir) is an option that allows to override the output directory structure. In our example the compiled `.js` files are placed directly in the `dist` folder, with the `src` prefix being stripped. If we wanted to preserve the `src` folder also in the output, we would need to set `rootDir` to `src`.

## About `@tsconfig/node16`

In addition to the above, our `tsconfig.json` file will include some additional compiler options from the `@tsconfig/node16` package:

```json
{
  "compilerOptions": {
    "lib": ["es2021"],
    "module": "commonjs",
    "target": "es2021",

    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node"
  }
}
```

In short, this is what the options do:

- [`target`](https://www.typescriptlang.org/tsconfig#target) defines which JavaScript specification we're using, and thus the syntax and APIs that are allowed in the output JavaScript. Here we're using ES2021, since Node.js 16 fully supports it;
- [`lib`](https://www.typescriptlang.org/tsconfig#lib) tells TypeScript to include type definitions for built-in APIs defined by ES2021. According to the docs it is automatically set to the same value of `target`, but here they made it explicit;
- [`module`](https://www.typescriptlang.org/tsconfig#module) defines that the JavaScript code should use CommonJS for imports, i.e. it should use `require()` to import modules. Although Node.js 16 adds native support for the new ECMAScript Modules (ESM) syntax (the one you actually always use in TypeScript when you write `import helper from 'helper'`), this is still a new thing and this config doesn't make use of it. You can read more about ESM [here](https://www.typescriptlang.org/docs/handbook/esm-node.html). Note that this option also modifies [`moduleResolution`](https://www.typescriptlang.org/tsconfig#moduleResolution), which is however made explicit anyway in this config file;
- `strict` enables a set of stricter checks that should really be the default. You can read more about the "strict mode family" options [in the official docs](https://www.typescriptlang.org/tsconfig#strict);
- [`esModuleInterop`](https://www.typescriptlang.org/tsconfig#esModuleInterop) fixes problems when trying to import CommonJS modules with the ESM syntax. This also enables [`allowSyntheticDefaultImports`](https://www.typescriptlang.org/tsconfig#allowSyntheticDefaultImports), which simply allows you to write something like `import moment from 'moment'` instead of `import * as moment from 'moment'`.

## Runing the compiler

To run the TypeScript compiler we'll use the `tsc` CLI tool.

In your terminal, run:

```sh
./node_modules/typescript/bin/tsc
```

And that's it! The compiler automatically reads the `tsconfig.json` file so it knows what to do. The output `.js` files should now be in the `dist` directory.

A better way to run `tsc` is to make use of npm scripts. Modify your `package.json` file so that it contains a `scripts` section as follows:

```json
{
    // ...
    "scripts": {
        "build": "tsc"
    }
}
```

Then you can use:

```sh
npm run build
```

To actually run the code, just use:

```sh
node dist/index.js
```

Or even better, create a `start` npm script:

```json
{
    // ...
    "scripts": {
        "build": "tsc",
        "start": "node dist/index.js"
    }
}
```

## Watch + reload

While you're developing, you will often need to recompile and restart the application. Instead of manually running `npm run build && npm start` each time there's a better way.

The `tsc` compiler allows to enable the "watch" feature with the `--watch` option: in this way the compiler will recompile the output each time a source file is changed.

This approach still requires you to manually run and restart the actual Node.js application, so a better solution could be to use the `tsc-watch` npm package.

You can install it with:

```sh
npm install --save-dev tsc-watch
```

And then add a new npm script that looks like the following:

```json
{
    // ...
    "scripts": {
        // ...
        "dev": "tsc-watch --onSuccess \"node dist/index.js\"
    }
}
```

So if you run `npm run dev` you'll have the Node.js application automatically recompiled and restarted whenever your source code changes.

(You might find the `--noClear` option of `tsc-watch` useful, as it disables clearing the terminal at each build.)

This is just one way of doing it, there are many other libraries and approaches.

## Conclusion

That's it! This was a minimal example of how to setup TypeScript with a Node.js backend application.

In practice you would probably want to add more stuff, when the project grows. This usually includes [ESLint](https://typescript-eslint.io/) for linting and something like [Prettier](https://prettier.io/) for enforcing a consistent code style.

If you're building a web application, using a framework like [NestJS](https://nestjs.com/) is also probably a good idea.

Feel free to leave a comment if you have suggestions or doubts!
