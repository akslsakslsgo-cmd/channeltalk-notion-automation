from notion_client import Client
from config import NOTION_TOKEN, NOTION_DATABASE_ID


class NotionService:
    def __init__(self):
        self.client = Client(auth=NOTION_TOKEN)
        self.database_id = NOTION_DATABASE_ID

    def create_channeltalk_page(self, item: dict):
        self.client.pages.create(
            parent={"database_id": self.database_id},
            properties={
                "상담ID": {
                    "title": [
                        {
                            "text": {
                                "content": item.get("chat_id", "")
                            }
                        }
                    ]
                },
                "이용자ID": {
                    "rich_text": [
                        {
                            "text": {
                                "content": item.get("user_id", "")
                            }
                        }
                    ]
                },
                "담당자ID": {
                    "rich_text": [
                        {
                            "text": {
                                "content": item.get("manager_id", "")
                            }
                        }
                    ]
                },
                "상태": {
                    "rich_text": [
                        {
                            "text": {
                                "content": item.get("status", "")
                            }
                        }
                    ]
                },
                "태그": {
                    "rich_text": [
                        {
                            "text": {
                                "content": item.get("tags", "")
                            }
                        }
                    ]
                },
                "생성일시": {
                    "rich_text": [
                        {
                            "text": {
                                "content": item.get("created_at", "")
                            }
                        }
                    ]
                },
                "수정일시": {
                    "rich_text": [
                        {
                            "text": {
                                "content": item.get("updated_at", "")
                            }
                        }
                    ]
                },
                "요약": {
                    "rich_text": [
                        {
                            "text": {
                                "content": item.get("summary", "")
                            }
                        }
                    ]
                },
            },
        )
