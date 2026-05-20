import os
from dotenv import load_dotenv

# Load .env file (works locally, ignored gracefully in ECS)
load_dotenv()

# ==============================
# NEWS API CONFIGURATION
# ==============================

API_KEY = os.getenv("API_KEY", "")

NEWS_URL = (
    f"https://newsapi.org/v2/top-headlines?"
    f"country=us&"
    f"category=business&"
    f"apiKey={API_KEY}"
)

# ==============================
# POSTGRESQL CONFIGURATION
# ==============================

DB_USER     = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST     = os.getenv("DB_HOST", "localhost")
DB_PORT     = int(os.getenv("DB_PORT", "5432"))  # ← KEY FIX
DB_NAME     = os.getenv("DB_NAME", "newsdb")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)