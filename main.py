from config import SYNC_MODE
from services.notion_service import NotionService
from services.channeltalk_service import ChannelTalkService
from processors.channeltalk_processor import extract_channeltalk_fields


def run_channeltalk_sync():
    ch_service = ChannelTalkService()
    notion_service = NotionService()

    response = ch_service.get_chats()
    chats = response.get("chats", []) if isinstance(response, dict) else []

    for chat in chats:
        item = extract_channeltalk_fields(chat)
        if item.get("chat_id"):
            notion_service.create_channeltalk_page(item)

    print(f"[완료] ChannelTalk 상담 {len(chats)}건 처리")


if __name__ == "__main__":
    if SYNC_MODE == "channeltalk":
        run_channeltalk_sync()
    else:
        raise ValueError("SYNC_MODE는 'channeltalk' 이어야 합니다.")
