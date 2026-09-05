# Blog [![Netlify Status](https://api.netlify.com/api/v1/badges/99ab826c-1be9-41f4-a02c-53e5cd3d22d6/deploy-status)](https://app.netlify.com/sites/matteocontrini-blog/deploys)

My personal blog.

- Built with Hugo.
- Deployed to Netlify.
- Comments powered by [giscus](https://giscus.app/en).

## Image color profiles

Hugo's image processing [does not support reading color profiles](https://github.com/gohugoio/hugo/issues/8298), so color fidelity of the original images is lost during conversion.

Use the following commands to convert images with non-sRGB ICC profiles to sRGB before committing new images:

```sh
uv run scripts/prepare_images.py --check
uv run scripts/prepare_images.py
```

The GitHub Actions test workflow fails when PNG/JPEG files with non-sRGB ICC profiles are found.
