# openai_service.py

# OpenAI API 사용을 위한 공식 라이브러리
from openai import OpenAI

# Streamlit 사용
import streamlit as st

# OpenAi 클라이언트 생성 함수
# 같은 api_key로 호출되면 재실행되어도 클라이언트를 재사용합니다.
@st.cache_resource
def create_openai_client(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key)

# OpenAI Conversations API로 새 대화방 생성
def create_conversation(client: OpenAI) -> str:
    conversation = client.conversations.create()
    return conversation.id

# 사용자 입력(prompt)을 받아 AI 응답 텍스트를 반환하는 함수
def get_ai_response(client: OpenAI, prompt: str, conversation_id: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions="당신은 사용자를 도와주는 상담사입니다.",
        max_output_tokens=100,
        input=[
            {"role": "user", "content": prompt},
        ],
        conversation=conversation_id
    )
    return response.output_text