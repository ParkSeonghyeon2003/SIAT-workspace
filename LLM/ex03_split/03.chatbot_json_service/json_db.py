# json_db.py

# JSON 파일 입출력을 위한 표준 라이브러리
import json

# 파일 경로를 객체 형태로 다루기 위한 라이브러리
from pathlib import Path

# Path는 파일 경로를 객체 형태로 다루기 위한 클래스입니다.
# JSON 파일의 경로를 Path 객체로 만들어 DB_FILE 변수에 저장합니다.
DB_FILE = Path("chat_history.json")


# JSON 파일 초기화 함수
def init_db() -> None:

    # DB_FILE(chat_history.json)이 존재하지 않으면 새 JSON 파일을 생성합니다.
    if not DB_FILE.exists():

        DB_FILE.write_text(

            json.dumps([], ensure_ascii=False, indent=2),

            # JSON 파일을 UTF-8 인코딩으로 저장
            encoding="utf-8"
        )


# 전체 메시지 불러오기 함수
def load_messages() -> list[dict[str, str]]:
    # 파일이 없으면 먼저 초기화
    init_db()

    # JSON 파일 내용을 문자열로 읽기
    text = DB_FILE.read_text(encoding="utf-8")

    # 문자열(JSON) → Python 리스트 변환
    return json.loads(text)


# 메시지 1개 저장 함수
def save_message(role: str, content: str) -> None:
    # 기존 대화 내용 불러오기
    messages = load_messages()

    # 새 메시지 추가
    messages.append({
        "role": role,
        "content": content
    })

    # Python 리스트 → JSON 문자열로 변환 후 저장
    DB_FILE.write_text(
        json.dumps(messages, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


# 전체 대화 삭제 함수
def clear_messages() -> None:
    # 빈 리스트로 다시 저장
    DB_FILE.write_text(
        json.dumps([], ensure_ascii=False, indent=2),
        encoding="utf-8"
    )