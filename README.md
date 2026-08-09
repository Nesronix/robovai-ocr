# RoboVAI OCR 🚗🆔👤

<p align="center">
  <img src="docs/banner.jpg" alt="RoboVAI OCR Banner" width="100%" />
</p>

[![PyPI Version](https://img.shields.io/pypi/v/robovai-ocr.svg?color=blue)](https://pypi.org/project/robovai-ocr/)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://pypi.org/project/robovai-ocr/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/tests-15%2F15%20PASSING-brightgreen.svg)](https://github.com/m0shaban)

**RoboVAI OCR** is a high-performance, enterprise-grade Computer Vision and OCR framework built for **Automatic License Plate Recognition (ALPR), National ID Card Parsing, and Driver Facial Verification**.

Designed for seamless deployment in **Smart Parking Systems, Barrier Gate Controls, Fleet Management, and Access Security**, RoboVAI OCR provides an intuitive **Python SDK**, a high-throughput **Async Pipeline**, and a production-ready **FastAPI REST & WebSocket Server**.

---

## 🖥️ Live Control Center Dashboard

<p align="center">
  <img src="docs/screenshots/dashboard_preview_1.jpg" alt="RoboVAI OCR National ID Dashboard Preview" width="48%" />
  <img src="docs/screenshots/dashboard_preview_2.jpg" alt="RoboVAI OCR ALPR Dashboard Preview" width="48%" />
</p>

<p align="center">
  <img src="docs/screenshots/dashboard_preview_3.jpg" alt="RoboVAI OCR Gate Control Dashboard" width="48%" />
  <img src="docs/screenshots/dashboard_preview_4.jpg" alt="RoboVAI OCR Face Match Preview" width="48%" />
</p>

---

## 🔥 Key Capabilities

- **Automatic License Plate Recognition (ALPR)**: Multi-scale inference (TTA) with region-split whitelisted OCR for Egyptian, Arabic, and international vehicle plates.
- **National ID & Driver License Parsing**: End-to-end deep learning OCR extracting 14-digit Egyptian National ID, Full Name, Address, DOB, Gender, Governorate, and photo crop.
- **Driver Facial Verification**: Real-time facial feature extraction and authorization matching against a driver registration database.
- **High-Concurrency RTSP / Stream Processing**: Async queue architecture decoupling object tracking from heavy OCR background execution.
- **Developer First**: Clean Python SDK, interactive Web Dashboard, CLI tools, OpenAPI docs, and Webhooks for automated hardware/barrier control.

---

## ⚡ Quick Start

### Installation

Install the latest release directly from PyPI:

```bash
pip install --upgrade robovai-ocr
```

Or install from source for development:

```bash
git clone https://github.com/m0shaban/robovai_ocr_system.git
cd robovai_ocr_system
pip install -e .
```

---

## 💻 Developer Guide & Usage Examples

### 1. Python SDK Integration

```python
from robovai_ocr import RoboVAIEngine

# Initialize engine (auto-detects CPU/GPU)
engine = RoboVAIEngine()

# --- License Plate Recognition ---
plate_res = engine.read_license_plate("car.jpg")
print(plate_res["plate_number"])  # e.g. "س ط أ 1 2 3"
print(plate_res["confidence"])    # e.g. 0.96

# --- Egyptian National ID Extraction ---
id_res = engine.extract_national_id("national_id.jpg")
print(id_res["national_id"])     # e.g. "29901010100123"
print(id_res["full_name"])       # e.g. "أحمد محمد علي"
print(id_res["governorate"])     # e.g. "Cairo"

# --- Driver Face Verification ---
face_res = engine.verify_driver_face("driver.jpg", db_path="data/driver_faces")
print(face_res["match"])         # True / False
```

### 2. High-Throughput Async Pipeline

```python
import asyncio
from robovai_ocr.core.pipeline import AsyncOCRPipeline

async def main():
    pipeline = AsyncOCRPipeline()
    await pipeline.start()
    
    # Submit frame for non-blocking processing
    job_id = await pipeline.submit_frame(frame_bytes)
    result = await pipeline.get_result(job_id)
    print(result)

asyncio.run(main())
```

### 3. Command Line Interface (CLI)

```bash
# Run ALPR on single image
robovai-cli alpr --image path/to/car.jpg

# Extract National ID fields
robovai-cli idcard --image path/to/id.jpg

# Start REST API & Web Control Dashboard
robovai-server --host 0.0.0.0 --port 8500
```

---

## 📡 REST API & WebSockets

Deploy as a standalone microservice:

```bash
robovai-server --port 8500
```

- **Control Center Dashboard**: [http://localhost:8500/](http://localhost:8500/)
- **Interactive OpenAPI Documentation**: [http://localhost:8500/docs](http://localhost:8500/docs)

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/v1/alpr` | `POST` | Process license plate image with OCR & bounding box visualization |
| `/api/v1/id-card` | `POST` | Extract structured fields from National ID / Driver License |
| `/api/v1/face` | `POST` | Match driver face photo against registered driver database |
| `/api/v1/pipeline` | `POST` | Asynchronous background processing queue |
| `/ws/stream` | `WebSocket` | Real-time RTSP/Webcam video stream processing |

---

## 🛠️ Architecture Overview

```text
                               +-----------------------------+
                               |     RTSP Stream / Image     |
                               +--------------+--------------+
                                              |
                                              v
                               +--------------+--------------+
                               |    RoboVAI OCR Engine SDK   |
                               +--------------+--------------+
                                              |
            +---------------------------------+---------------------------------+
            |                                 |                                 |
            v                                 v
   +--------+--------+               +--------+--------+               +--------+--------+
   |   ALPREngine    |               |    IDEngine     |               |   FaceEngine    |
   | (YOLO + EasyOCR)|               | (3x YOLO Models)|               | (Face Match DB) |
   +--------+--------+               +--------+--------+               +--------+--------+
            |                                 |                                 |
            +---------------------------------+---------------------------------+
                                              |
                                              v
                               +--------------+--------------+
                               | FastAPI REST & WebSockets   |
                               +--------------+--------------+
                                              |
                                              v
                               +--------------+--------------+
                               | Smart Barrier Gate / Webhook|
                               +-----------------------------+
```

---

## 🤝 Contributing

We welcome contributions from the open-source community! Whether you are fixing bugs, improving docs, or proposing new features:

1. **Fork the Repository** on GitHub.
2. **Create a Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Commit Your Changes**: `git commit -m 'Add amazing feature'`
4. **Push to Branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author & Connect

Developed by **Mohamed Shaban (محمد شعبان العتماني)** — Founder & AI Architect at RoboVAI.

- ⭐ **Star & Follow on GitHub**: [github.com/m0shaban](https://github.com/m0shaban)
- 🌐 **Personal Website**: [msalatmani.org](https://msalatmani.org)
- 🏢 **Company**: [robovai.tech](https://robovai.tech)
- 📦 **PyPI Package**: [pypi.org/project/robovai-ocr/](https://pypi.org/project/robovai-ocr/)
