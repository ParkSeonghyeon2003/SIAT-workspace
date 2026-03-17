# Streamlit 라이브러리를 st라는 이름으로 불러옵니다.
# Streamlit은 Python 코드로 웹 애플리케이션을 쉽게 만들 수 있는 라이브러리입니다.
import streamlit as st

# JSON 데이터를 읽고 쓰기 위한 표준 라이브러리입니다.
# Python의 객체 ↔ JSON 문자열 변환에 사용됩니다.
import json

# pathlib 라이브러리의 Path 클래스를 불러옵니다.
# 파일 경로를 객체 형태로 다루기 위해 사용합니다.
# (파일 존재 확인, 읽기, 쓰기 등을 수비게 할 수 있습니다.)
from pathlib import Path

# 저장할 JSON 파일의 경로를 지정합니다.
# count.json 파일을 현재 프로그램 폴더에서 사용합니다.
DB_FILE = Path("count.json")

# session_state의 count 값을 0으로 초기화합니다.
st.session_state.count = 0

# JSON 파일이 존재하는지 확인합니다.
if DB_FILE.exists():

    # 파일 내용을 문자열로 읽어옵니다.
    # 예: '{"count": 5}'
    json_text = DB_FILE.read_text()

    # JSON 문자열을 Python 딕셔너리롤 변환합니다.
    # 결과 예: {"count": 5}
    data = json.loads(json_text)

    # "count"라는 키가 데이터 안에 있는지 확인합니다.
    if "count" in data:
        # JSON에서 count 값을 가져와 session_state에 저장합니다.
        st.session_state.count = data["count"]

# "증가" 버튼을 화면에 생성합니다.
# 사용자가 버튼을 클릭하면 True가 반환됩니다.
if st.button("증가"):

    # 버튼이 눌리면 count 값을 1 증가시킵니다.
    st.session_state.count += 1

    # 현재 count 값을 JSON 형식의 딕셔너리로 만듭니다.
    data = {"count": st.session_state.count}
    
    # Python 딕셔너리를 JSON 문자열로 변환합니다.
    # 예: {"count": 6} → '{"count": 6}'
    json_text = json.dumps(data)

    # JSON 문자열을 파일에 저장합니다.
    # count.json 파일이 없으면 새로 생성하고 있으면 내용을 덮어쓰기 합니다.
    DB_FILE.write_text(json_text)

# 현재 count 값을 웹 화면에 출력합니다.
st.write("현재 값:", st.session_state.count)