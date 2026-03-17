from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# sidebar가 활성화 되어 있으면 아래 내용 실행
with st.sidebar:
    # openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

# st.session_state는 Streamlit에서 제공하는 메모리 저장 공간입니다.
# 앱이 다시 실행되어도 상태 값을 유지할 수 있습니다.

# messages라는 키가 없으면 초기 메시지를 생성합니다.
if "messages" not in st.session_state:
    # 초기 챗봇 메시지
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]


# 대화 내용을 출력
# session_state에 저장된 대화 메시지를 화면에 출력합니다.
for msg in st.session_state.messages:

    # role에 따라 user / assistant 말풍선 생성합니다.
    st.chat_message(msg["role"]).write(msg["content"])

# st.chat_input() : 채팅 입력창을 생성합니다.
# 사용자가 Enter를 누르면 입력 문자열이 반환됩니다.
if prompt := st.chat_input():

    # API 키가 없으면 안내 메시지 출력 후 실행 중단합니다.
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # OpenAI API 클라이언트 생성합니다.
    client = OpenAI(api_key=openai_api_key)

    # 사용자 메시지를 대화 기록(messages)에 추가합니다.
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 사용자 메시지를 화면에 출력합니다.
    st.chat_message("user").write(prompt)

    # 대화 내용을 LLM으로 전달
    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions="당신은 사용자를 도와주는 상담사입니다.",
        max_output_tokens=100,
        input=[
            {"role": "user", "content": prompt},
        ],
    )
    
    msg = response.output_text

    # LLM 응답을 대화 내용에 추가합니다.
    st.session_state.messages.append({"role": "assistant", "content": msg})

    # LLM 응답을 화면에 출력합니다.
    st.chat_message("assistant").write(msg)
