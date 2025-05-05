# backend/config.py

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# PDF Generator
PDF_API_KEY = os.getenv("PDF_GENERATOR_API_KEY")
PDF_SECRET_KEY = os.getenv("PDF_GENERATOR_SECRET_KEY")

# HuggingFace AI
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# Geoapify (used in frontend too)
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")

# Pixel AI
PIXELAI_API_KEY = os.getenv("PIXELAI_API_KEY")

# Twilio
TWILIO_SECRET = os.getenv("TWILIO_SECRET")

# DeepSeek AI
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# Cloudinary
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

# Financial APIs
COINBASE_API_KEY = os.getenv("COINBASE_API_KEY")
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")

# Unsplash
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
UNSPLASH_SECRET_KEY = os.getenv("UNSPLASH_SECRET_KEY")

# Security Tools
SNYK_API_KEY = os.getenv("SNYK_API_KEY")
