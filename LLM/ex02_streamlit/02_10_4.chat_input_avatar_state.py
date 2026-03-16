import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []



for msg in st.session_state.messages:
    st.chat_message(msg["role"], avatar=f"data/{msg["role"]}.png").write(msg["content"])

if prompt := st.chat_input("메시지를 입력하세요"):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    st.chat_message("user", avatar="data/user.png").write(prompt)
    
    response = "응답: " + prompt

    st.session_state.messages.append(
        {"role": "assistant", "content": "응답: " + response}
    )

    st.chat_message("assistant", avatar="data/assistant.png").write(response)