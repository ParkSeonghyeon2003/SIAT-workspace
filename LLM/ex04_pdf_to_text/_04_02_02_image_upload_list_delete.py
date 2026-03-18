from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path="C:/workspace/LLM/.env")

# OpenAI API 서버와 통신할 클라이언트 객체 생성합니다.
client = OpenAI()


# 업로드된 파일 확인합니다.
files = client.files.list()

for f in files:
    print(f.id, f.filename)

try:
    client.files.delete("file-VQj41ZaJftMbdDzgbb7AM9")
    print("삭제 후")

    files = client.files.list()
    for f in files:
        print(f.id, f.filename)
except Exception as e:
    print("해당하는 파일 명이 없습니다.")
