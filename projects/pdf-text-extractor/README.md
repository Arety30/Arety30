# PDF Text Extractor 📄

A tiny browser-based tool to extract, search, copy, and download selectable text from PDF files.

## Try it

Open `index.html` in a modern browser, or publish this folder as a static site. It loads Mozilla PDF.js from a CDN.

## Features

- Drag-and-drop or file-picker input
- Extracts selectable text page by page
- Search the extracted text
- Copy all text or download it as `.txt`
- No API key and no application backend
- The page does not upload the selected PDF to a server

## Limits

Scanned PDFs that contain only page images need OCR, which is not included. The PDF.js library is loaded from a CDN, so an internet connection is needed unless you vendor the library locally. For private documents, use trusted software and review your environment's network requirements.

## Run locally

Simply open `index.html` in a current browser. If your browser restricts module loading from local files, run a local static server:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000/projects/pdf-text-extractor/` from the repository root, or serve this folder directly.

## Status

A rebuilt, standalone version based on the project idea recorded in my development history. It is a new implementation, not a claim that the earlier working copy was recovered byte-for-byte.
