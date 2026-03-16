import streamlit as st

count = 0
if st.button("Click me"):
    count += 1
    st.write(f"{count}번 click")



# Streamlit은 웹 앱의 상태를 간단하게 유지하기 위해
# 사용자의 입력이 발생할 때마다 전체 스크립트를 위에서부터 다시 실행하는 구조를 사용합니다.
# 즉 사용자 인터랙션(사용자가 무언가를 입력하거나 조작하는 행동)이 발생하면 재실행(rerun) 됩니다.

# Streamlit에서 전체 코드가 다시 실행되는 경우
# 1. 버튼을 클릭했을 때


# 2. 입력 위젯 값이 변경될 때
# 위젯(Widget)은 사용자가 값을 입력하거나 선택할 수 있게 해주는 화면 요소(UI 구성 요소)입니다.
# Streamlit에서 사용자가 조작할 수 있는 모든 입력 요소를 입력 위젯이라고 합니다.
# st.text_input("이름")
# st.number_input("나이")
# st.slider("값 선택", 0, 100)
# st.checkbox("동의")
# st.selectbox("과일 선택", ["사과", "배", "포도"])
# 값이 바뀌는 순간 전체 코드 재실행됩니다.


# 3. 파일 업로드
# st.file_uploader("파일 업로드")
# 파일을 업로드하면 전체 코드가 다시 실행됩니다.

# 4. 폼 제출
# st.form_submit_button("Submit")
# Submit 버튼을 누르면 재실행


# 그래서 상태를 유지하려면 st.session_state를 사용합니다.
# Streamlit은 사용자 인터랙션이 발생할 때마다 전체 Python 스크립트를 다시 실행하여 UI를 갱신하는 프레임워크입니다.