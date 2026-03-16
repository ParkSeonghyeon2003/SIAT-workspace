import streamlit as st


# st.chat_input("메시지를 입력하세요") : 채팅 입력창을 화면 아래에 생성합니다.
# 사용자가 메시지를 입력하고 Enter를 누르면 입력 문자열이 반환됩니다.

# `:=` (월러스 연산자, Walrus Operator)
# 입력값을 prompt 변수에 저장하면서 동시에 if 조건문에서 검사합니다.
# 입력값이 존재하면 True로 간주되어 아래 코드 블록이 실행됩니다.
if prompt := st.chat_input("메시지를 입력하세요"):


    # st.chat_message("user") : 사용자 메시지를 채팅 형태로 화면에 출력합니다.
    # avatar="data/user.png" : 사용자 아이콘 이미지를 data 폴더 안의 user.png 파일로 지정합니다.
    # 즉, 프로젝트 구조는 다음과 같이 되어 있어야 합니다.
    #
    # project/
    # ├ app.py
    # └ data/
    #    ├ user.png
    #    └ assistant.png
    #
    st.chat_message("user", avatar="data/user.png").write(prompt)


    # st.chat_message("assistant") : 챗봇(assistant)의 메시지를 채팅 형태로 화면에 출력합니다.
    # avatar="data/assistant.png" : 챗봇 아이콘을 data 폴더 안의 assistant.png 파일로 표시합니다.
    # write() 함수로 챗봇의 응답 메시지를 화면에 출력합니다.
    st.chat_message("assistant", avatar="data/assistant.png").write(
        "안녕하세요! 무엇을 도와드릴까요?"
    )