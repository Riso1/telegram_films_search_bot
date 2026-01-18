import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")
TMDB_API_KEY: str | None = os.getenv("TMDB_API_KEY")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in .env")

if not TMDB_API_KEY:
    raise RuntimeError("TMDB_API_KEY is not set in .env")
