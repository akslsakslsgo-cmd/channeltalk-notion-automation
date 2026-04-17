import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

CHANNELTALK_ACCESS_KEY = os.getenv("CHANNELTALK_ACCESS_KEY")
CHANNELTALK_ACCESS_SECRET = os.getenv("CHANNELTALK_ACCESS_SECRET")
CHANNELTALK_BASE_URL = os.getenv("CHANNELTALK_BASE_URL", "https://api.channel.io")

SYNC_MODE = os.getenv("SYNC_MODE", "channeltalk").lower()
