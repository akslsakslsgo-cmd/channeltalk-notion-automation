def extract_text_from_messages(messages: list) -> str:
    texts = []

    for msg in messages[:10]:
        if not isinstance(msg, dict):
            continue

        text = (
            msg.get("plainText")
            or msg.get("text")
            or msg.get("body")
            or ""
        )

        if text:
            texts.append(text.strip())

    return " / ".join(texts[:3])[:500]


def extract_channeltalk_fields(chat: dict) -> dict:
    messages = chat.get("messages", []) if isinstance(chat, dict) else []

    tags = chat.get("tags", [])
    if isinstance(tags, list):
        tags = ", ".join(str(tag) for tag in tags)
    else:
        tags = str(tags)

    return {
        "chat_id": str(chat.get("id", "")),
        "user_id": str(chat.get("userId", "")),
        "manager_id": str(chat.get("managerId", "")),
        "status": str(chat.get("state", "")),
        "tags": tags,
        "created_at": str(chat.get("createdAt", "")),
        "updated_at": str(chat.get("updatedAt", "")),
        "summary": extract_text_from_messages(messages) or "상담 내용 없음",
    }
