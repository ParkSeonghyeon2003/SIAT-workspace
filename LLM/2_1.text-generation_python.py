import os
import requests
from dotenv import load_dotenv

# 1. 환경 변수 로드
# override=True를 하면, 시스템 환경 변수에 이미 같은 이름의 변수가 있더라도,
# 파이썬 프로그램이 실행되는 동안만큼은 .env에 적힌 값으로 덮어써서 사용합니다.
load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

# 2. 엔드포인트 URL 설정
# Responses API 전용 주소입니다.
url = "https://api.openai.com/v1/responses"

# 3. 요청 헤더 설정
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "gpt-4.1-nano",
    "input": "OpenAI Responses API에 대해 한 문장으로 설명해줘"
}

# 5. HTTP POST 요청 발송
# 지정된 URL로 JSON 데이터를 포함한 POST 요청을 보내고, 서버의 응답을 response 변수에 저장한다.
response = requests.post(url, headers=headers, json=data)

# 6. 결과 처리 (JSON 파싱)
completion = response.json()

# 7. 출력 부분
print("전체 답변 데이터 구조:", completion)
print()
