#!/usr/bin/env python3
"""Extract selectable text from a PDF resume for local review."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Keep PDF text extraction self-contained when this skill is copied to another
# agent environment. The bundled pypdf package is pure Python and requires no
# separate pip installation.
_VENDOR_DIR = Path(__file__).resolve().parent / "vendor"
if _VENDOR_DIR.is_dir():
    sys.path.insert(0, str(_VENDOR_DIR))


def extract_pdf(path: Path) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages = [(page.extract_text() or "").replace("\x00", "") for page in reader.pages]
    unreadable = [str(index + 1) for index, page in enumerate(pages) if not page.strip()]
    if unreadable:
        page_list = ", ".join(unreadable)
        raise ValueError(
            f"No selectable text found on PDF page(s): {page_list}. "
            "This helper does not perform OCR. Use the host's PDF vision/OCR capability, "
            "or provide a searchable PDF or copied text."
        )
    return "\n\n".join(f"[第 {i + 1} 页]\n{page.strip()}" for i, page in enumerate(pages))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="PDF resume with selectable text")
    parser.add_argument("--output", type=Path, help="Write extracted text to this file; defaults to stdout")
    args = parser.parse_args()

    if not args.input.is_file():
        parser.error(f"Input file does not exist: {args.input}")

    if args.input.suffix.lower() != ".pdf":
        parser.error("Resume input must be a PDF file")

    try:
        result = extract_pdf(args.input)
    except ImportError as exc:
        print(
            "The bundled PDF reader is missing or incomplete. Reinstall the full "
            "tech-resume-coach skill folder and try again.",
            file=sys.stderr,
        )
        return 2
    except Exception as exc:
        print(f"Could not read the resume: {exc}", file=sys.stderr)
        return 1

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
    else:
        print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
