from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="robovai_ocr",
    version="1.0.8",
    description="Enterprise Computer Vision & OCR Core for Parking Management Systems (ALPR, Face Verification, National ID OCR)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mohamed Shaban (محمد شعبان العتماني)",
    author_email="msalatmani@gmail.com",
    url="https://msalatmani.org",
    project_urls={
        "Homepage": "https://msalatmani.org",
        "Company": "https://robovai.tech",
        "Source": "https://github.com/m0shaban",
        "Documentation": "https://msalatmani.org/#capabilities",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "robovai_ocr": ["api/static/*"],
    },
    python_requires=">=3.8",
    install_requires=[
        "opencv-python>=4.8.0",
        "numpy>=1.24.0",
        "ultralytics>=8.0.0",
        "easyocr>=1.7.0",
        "pillow>=9.5.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.22.0",
        "pydantic>=2.0.0",
        "httpx>=0.24.0",
        "loguru>=0.7.0",
        "python-multipart>=0.0.6",
    ],
    entry_points={
        "console_scripts": [
            "robovai-cli=robovai_ocr.cli.main:main",
            "robovai-server=robovai_ocr.api.app:start_server",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Graphics",
    ],
)
