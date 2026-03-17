# openai_service.py

# OpenAI API 사용을 위한 공식 라이브러리
from openai import OpenAI

# OpenAi 클라이언트 생성 함수
def create_openai_client(api_key):
    return OpenAI(api_key=api_key)


# 사용자 입력(prompt)을 받아 AI 응답 텍스트를 반환하는 함수
def get_ai_response(client, prompt):
    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions="당신은 사용자를 도와주는 상담사입니다.",
        max_output_tokens=100,
        input=[
            {"role": "user", "content": prompt},
        ],
    )

    # 응답 객체에서 텍스트만 추출하여 반환
    return response.output_text