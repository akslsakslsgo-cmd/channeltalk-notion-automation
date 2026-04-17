import requests
from config import (
    CHANNELTALK_ACCESS_KEY,
    CHANNELTALK_ACCESS_SECRET,
    CHANNELTALK_BASE_URL,
)


class ChannelTalkService:
    def __init__(self):
        self.base_url = CHANNELTALK_BASE_URL.rstrip("/")
        self.headers = {
            "x-access-key": CHANNELTALK_ACCESS_KEY,
            "x-access-secret": CHANNELTALK_ACCESS_SECRET,
            "Content-Type": "application/json",
        }

    def get_chats(self, limit: int = 50):
        """
        실제 엔드포인트와 파라미터는 ChannelTalk API 문서 기준으로 보완 필요
        """
        url = f"{self.base_url}/open/v5/user-chats"
        params = {"limit": limit}

        response = requests.get(url, headers=self.headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
