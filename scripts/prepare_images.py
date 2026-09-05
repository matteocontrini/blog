#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["Pillow==12.3.0"]
# ///
"""Convert tagged PNG/JPEG sources to sRGB in place, or report them with --check."""

import argparse
from io import BytesIO
from pathlib import Path
import sys
from tempfile import NamedTemporaryFile

from PIL import Image, ImageCms, JpegImagePlugin


SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB"))
SRGB_BYTES = SRGB.tobytes()


def prepare(path, check=False):
    with Image.open(path) as image:
        icc = image.info.get("icc_profile")
        if not icc:
            return False  # Do not guess a missing source profile.
        source = ImageCms.ImageCmsProfile(BytesIO(icc))
        description = ImageCms.getProfileDescription(source).strip()
        if description.casefold() in {"srgb", "srgb iec61966-2.1", "srgb built-in"}:
            return False
        if check:
            print(f"{path}: needs conversion ({description})")
            return True
        if getattr(image, "n_frames", 1) != 1:
            raise ValueError("animated PNG conversion is not supported")
        if image.format == "PNG":
            with path.open("rb") as header:
                if header.read(25)[24] == 16:
                    raise ValueError("16-bit PNG conversion would lose precision")
        mode = "RGBA" if "A" in image.getbands() or "transparency" in image.info else "RGB"
        pixels = image.convert(mode) if image.mode in {"P", "RGB", "RGBA"} else image
        converted = ImageCms.profileToProfile(pixels, source, SRGB, outputMode=mode)
        options = {"icc_profile": SRGB_BYTES}
        for key in ("exif", "dpi"):
            if key in image.info:
                options[key] = image.info[key]
        if image.format == "JPEG":
            options.update(qtables=image.quantization, subsampling=JpegImagePlugin.get_sampling(image))
        # Replace only after encoding succeeds; no copied content tree.
        with NamedTemporaryFile(dir=path.parent, suffix=path.suffix, delete=False) as temporary:
            replacement = Path(temporary.name)
        try:
            converted.save(replacement, format=image.format, **options)
            replacement.chmod(path.stat().st_mode)
            replacement.replace(path)
        finally:
            replacement.unlink(missing_ok=True)
    print(f"{path}: {description} -> sRGB")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report without modifying files; exit 1 if conversion is needed")
    parser.add_argument("paths", nargs="*", type=Path, help="optional files or directories")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    roots = args.paths or [root / name for name in ("content", "static", "assets")]
    count = 0
    for directory in roots:
        if not directory.exists():
            raise FileNotFoundError(directory)
        paths = directory.rglob("*") if directory.is_dir() else [directory]
        for path in sorted(paths):
            if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg"}:
                try:
                    count += prepare(path, check=args.check)
                except Exception as error:
                    raise RuntimeError(f"{path}: {error}") from error
    if args.check:
        print(f"{count} images need conversion. Run: uv run scripts/prepare_images.py")
        return int(count > 0)
    print(f"Converted {count} images in place. Review and commit the converted files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
