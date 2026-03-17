# json_db.py
from typing import Any

# JSON 파일 입출력을 위한 표준 라이브러리
import json

# 파일 경로를 객체 형태로 다루기 위한 라이브러리
from pathlib import Path

# Path는 파일 경로를 객체 형태로 다루기 위한 클래스입니다.
# JSON 파일의 경로를 Path 객체로 만들어 DB_FILE 변수에 저장합니다.
DB_FILE = Path("chat_history.json")

# 기본 저장 구조를 반환하는 함수
def get_default_data() -> dict[str, Any]:
    return {
        "conversation_id": None,
        "messages": []
    }


# JSON 파일 초기화 함수
def init_db() -> None:
    if not DB_FILE.exists():
        DB_FILE.write_text(
            json.dumps(get_default_data(), ensure_ascii=False, indent=2),
            encoding="utf-8"
        )


# 전체 JSON 데이터 불러오기 함수
def load_data() -> dict[str, Any]:
    init_db()
    text = DB_FILE.read_text(encoding="utf-8")

    data = json.loads(text)

    if "conversation_id" not in data:
        data["conversation_id"] = None
    
    if "messages" not in data:
        data["messages"] = []

    return data


# 전체 JSON 데이터 저장 함수
def save_data(data: dict[str, Any]) -> None:
    DB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

# 전체 메시지 불러오기 함수
def load_messages() -> list[dict[str, str]]:
    data = load_data()
    return data["messages"]


# 메시지 1개 저장 함수
def save_message(role: str, content: str) -> None:
    data = load_data()
    data["messages"].append({
        "role": role,
        "content": content
    })
    save_data(data)


# conversation_id 저장 함수
def save_conversation_id(conversation_id: str) -> None:
    data = load_data()
    data["conversation_id"] = conversation_id
    save_data(data)


# conversation_id 불러오기 함수
def load_conversation_id() -> str:
    data = load_data()
    return data["conversation_id"]


# 전체 대화 삭제 함수
def clear_messages() -> None:
    data = load_data()

    # conversation_id는 유지하고 messages만 초기화
    data["messages"] = []

    save_data(data)