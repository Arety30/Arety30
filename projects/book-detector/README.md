# Book Detector 📚

A Flask computer-vision prototype that combines a pretrained YOLO model with EasyOCR.

## What it does

- Accepts a PNG, JPG, JPEG, or WEBP image
- Uses Ultralytics YOLO to look for the COCO `book` object class
- Uses EasyOCR to read visible text from the image
- Shows an annotated preview and text-confidence estimates
- Processes the uploaded image in memory instead of saving it to an uploads folder

## Run locally

Python 3.10–3.12 is recommended. In this folder:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. The pretrained YOLO weights and EasyOCR model files may download on first run, so initial setup needs internet access.

## Limitations

The default YOLO model is trained on general COCO classes, not book-cover titles. It may miss books or produce false detections. OCR reads text from the whole image and is not guaranteed to identify a title correctly. This is a learning prototype, not a production service.

The Flask development server binds to localhost and is not intended for direct public deployment. If you deploy it, add authentication, request limits, hardened hosting, and appropriate privacy controls.

## Status

Fresh rebuild based on the earlier Book Detector project description in my development history; not claimed to be the original source recovered byte-for-byte.
