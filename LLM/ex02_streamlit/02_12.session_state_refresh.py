import streamlit as st

# count가 세션 상태에 없으면 0으로 초기화
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("증가"):
    st.session_state.count += 1

st.write(st.session_state.count)

# 문제점: 새로 고침하면 새로운 세션을 시작하는 것과 같습니다.
# count 값이 다시 초기화 됩니다.
# 최종 conut 값을 파일에 저장 후 유지되도록 해보겠습니다.

# 세션(Session): 사용자가 웹 브라우저로 앱에 접속하여 상호작용하는 동안 서버가 해당 사용자를 구분하기 위해 유지하는 연결 및 상태 정보입니다.

# Streamlit 앱을 브라우저에서 새로고침한다는 것은 클라이언트(브라우저)가 서버에게 웹 페이지를 처음부터 다시 요청한다는 의미입니다.
# 웹 페이지 새로고침은 Streamlit 세션(Session)을 종료했다가 A새로운 세션을 시작하는 것과 같습니다.

# Streamlit의 st.session_state는 각각의 고유한 사용자 세션에 독립적으로 묶여서 데이터를 저장합니다.
# 따라서 브라우저 새로고침을 하면 이전 세션의 메모리 상의 모든 정보(Session State 포함)가 해제되고, 새로운 빈 세션이 생성됩니다.