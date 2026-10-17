from __future__ import annotations

import base64
import io
import os
from functools import lru_cache

import cv2
import easyocr
import numpy as np
from flask import Flask, render_template, request
from PIL import Image, UnidentifiedImageError
from ultralytics import YOLO

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
MODEL_NAME = os.environ.get("BOOK_DETECTOR_MODEL", "yolov8n.pt")


@lru_cache(maxsize=1)
def get_model() -> YOLO:
    # Ultralytics downloads the pretrained weights on first run if needed.
    return YOLO(MODEL_NAME)


@lru_cache(maxsize=1)
def get_reader() -> easyocr.Reader:
    return easyocr.Reader(["en"], gpu=False)


def image_to_data_url(image_bgr: np.ndarray) -> str:
    ok, encoded = cv2.imencode(".jpg", image_bgr, [cv2.IMWRITE_JPEG_QUALITY, 88])
    if not ok:
        raise RuntimeError("Could not encode the preview image.")
    payload = base64.b64encode(encoded.tobytes()).decode("ascii")
    return "data:image/jpeg;base64," + payload


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/detect")
def detect():
    uploaded = request.files.get("image")
    if not uploaded or not uploaded.filename:
        return render_template("index.html", error="Choose an image first.")

    extension = uploaded.filename.rsplit(".", 1)[-1].lower() if "." in uploaded.filename else ""
    if extension not in ALLOWED_EXTENSIONS:
        return render_template("index.html", error="Use a PNG, JPG, JPEG, or WEBP image.")

    try:
        image = Image.open(io.BytesIO(uploaded.read())).convert("RGB")
        image_rgb = np.asarray(image)
    except (UnidentifiedImageError, OSError, ValueError):
        return render_template("index.html", error="That file could not be read as an image.")

    if image_rgb.size == 0:
        return render_template("index.html", error="The image is empty.")

    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
    book_detections = []
    try:
        model_result = get_model()(image_rgb, verbose=False)[0]
        names = model_result.names
        for box in model_result.boxes:
            class_id = int(box.cls[0].item())
            label = str(names.get(class_id, class_id))
            confidence = float(box.conf[0].item())
            if label.lower() != "book":
                continue
            x1, y1, x2, y2 = (int(v) for v in box.xyxy[0].tolist())
            book_detections.append({"confidence": confidence, "box": (x1, y1, x2, y2)})
            cv2.rectangle(image_bgr, (x1, y1), (x2, y2), (40, 210, 120), 2)
            cv2.putText(
                image_bgr, f"book {confidence:.0%}", (x1, max(22, y1 - 8)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (40, 210, 120), 2, cv2.LINE_AA
            )
    except Exception:
        app.logger.exception("Object detection failed")
        return render_template("index.html", error="The detector failed to process this image.")

    try:
        ocr_results = get_reader().readtext(image_rgb, detail=1, paragraph=False)
        recognized_text = [
            {"text": str(text).strip(), "confidence": float(confidence)}
            for _bbox, text, confidence in ocr_results
            if str(text).strip()
        ]
    except Exception:
        app.logger.exception("OCR failed")
        recognized_text = []

    return render_template(
        "index.html",
        preview=image_to_data_url(image_bgr),
        book_count=len(book_detections),
        detections=book_detections,
        recognized_text=recognized_text,
        note=(
            "The pretrained YOLO model detects the COCO 'book' class; it may miss book covers "
            "or confuse them with other objects. OCR is a separate text-reading pass."
        ),
    )


@app.errorhandler(413)
def too_large(_error):
    return render_template("index.html", error="Image is too large. Maximum upload size is 10 MB."), 413


if __name__ == "__main__":
    # Local-only by default. Do not expose this development server directly to the internet.
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=False)
