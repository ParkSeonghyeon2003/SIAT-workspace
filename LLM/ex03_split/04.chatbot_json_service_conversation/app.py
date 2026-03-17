# app.py

# Streamlit 웹 앱 라이브러리
import streamlit as st

# .env 파일의 환경 변수를 불러오기 위한 라이브러리
from dotenv import load_dotenv

# 운영체제 환경 변수 사용
import os

# JSON 저장 전용 파일에서 필요한 함수 가져오기
from json_db import (
    init_db,
    load_messages,
    save_message,
    clear_messages,
    load_conversation_id,
    save_conversation_id
)

# OpenAI 관련 기능 가져오기
from openai_service import (
    create_openai_client,
    create_conversation,
    get_ai_response
)

# .env 파일 로드
load_dotenv(dotenv_path="C:/workspace/LLM/.env")

# 앱 시작 시 JSON 파일 초기화
init_db()

# ----------------------------
# 사이드바
# ----------------------------
with st.sidebar:
    # 환경 변수에서 OpenAI API Key 읽기
    openai_api_key = os.getenv("OPENAI_API_KEY")

    st.write("### 설정")
    st.write("대화 내용은 JSON 파일에 저장됩니다.")

    # 대화 초기화 버튼
    if st.button("초기화"):
        clear_messages()

        # session_state도 초기화
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}
        ]

        # 초기 메시지를 JSON 파일에도 저장
        save_message("assistant", "How can I help you?")

        st.rerun()

# ----------------------------
# 제목
# ----------------------------
st.title("💬 Chatbot")
st.caption("🚀 JSON 파일에 대화가 저장되는 Streamlit 챗봇")

# ----------------------------
# 초기 대화 불러오기
# ----------------------------

if "messages" not in st.session_state:
    db_messages = load_messages()

    # 저장된 대화가 없으면 최초 안내 메시지 생성
    if not db_messages:
        first_message = {
            "role": "assistant",
            "content": "How can I help you?"
        }
        st.session_state["messages"] = [first_message]
        save_message(first_message["role"], first_message["content"])
    else:
        st.session_state["messages"] = db_messages

if "conversation_id" not in st.session_state:
    st.session_state["conversation_id"] = load_conversation_id()

# ----------------------------
# 기존 대화 출력
# ----------------------------
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# ----------------------------
# 사용자 입력 처리
# ----------------------------
if prompt := st.chat_input("메시지를 입력하세요"):
    # API Key가 없으면 중단
    if not openai_api_key:
        st.info("OPENAI_API_KEY를 .env 파일에 설정해 주세요.")
        st.stop()

    # 사용자 메시지 생성
    user_message = {
        "role": "user",
        "content": prompt
    }

    # session_state에 저장
    st.session_state["messages"].append(user_message)

    # JSON 파일에도 저장
    save_message(user_message["role"], user_message["content"])
    
    # 화면에 사용자 메시지 출력
    st.chat_message("user").write(prompt)


    # OpenAI 클라이언트 생성
    # st.cache_resource가 적용되어 같은 api_key면 재사용합니다.
    client = create_openai_client(openai_api_key)

    # 현재 세션에서 conversation_id 확인
    conversation_id = st.session_state.get("conversation_id")

    # 세션에 없으면 JSON 파일에서 확인
    if not conversation_id:
        conversation_id = load_conversation_id()

    # JSON 파일에서 없으면 새로 생성
    if not conversation_id:
        conversation_id = create_conversation(client)
        save_conversation_id(conversation_id)

    # session_state에도 반영
    st.session_state["conversation_id"] = conversation_id


    # AI 응답 받기
    try:
        assistant_text = get_ai_response(
            client=client,
            prompt=prompt,
            conversation_id=st.session_state["conversation_id"]
        )
    except Exception as e:
        assistant_text = f"오류가 발생했습니다: {e}"

    # AI 응답 메시지 생성
    assistant_message = {
        "role": "assistant",
        "content": assistant_text
    }

    # session_state에 저장
    st.session_state["messages"].append(assistant_message)

    # JSON 파일에도 저장
    save_message(assistant_message["role"], assistant_message["content"])

    # 화면에 AI 응답 출력
    st.chat_message("assistant").write(assistant_text)
