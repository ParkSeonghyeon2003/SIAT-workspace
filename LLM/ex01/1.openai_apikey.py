# 운영체제의 환경변수(OS 환경변수)를 가져오거나 확인할 때 사용합니다.
import os

from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_KEY is None:
    raise EnvironmentError(
        "환경변수 OPENAI_API_KEY가 설정되어 있지 않습니다.\n"
        "1) 프로젝트 루트에 .env 파일을 만들고 아래처럼 넣으세요.\n"
        "   OPENAI_API_KEY=sk-여기에-실제-키\n"
        "2) 또는 시스템 환경변수에 OPENAI_API_KEY를 설정하세요\n"
        "3) 환경변수 설정 후 파이썬을 다시 실행하세요."
    )

print("OPENAI_API_KEY가 로드되었습니다. (길이:", len(OPENAI_KEY), "문자)")