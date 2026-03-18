# app.py




# 운영체제의 환경 변수 사용
import os

# 파일 및 폴더 경로를 객체 형태로 다루기 위한 모듈
from pathlib import Path

# Streamlit 웹 앱 라이브러리
import streamlit as st

# .env 파일의 환경 변수를 읽기 위한 라이브러리
from dotenv import load_dotenv

# ------------------------------------------------
# JSON 파일 기반 분석 이력 관리 모듈
# ------------------------------------------------
from json_db import (
    init_db,                # JSON DB 초기화
    load_analysis_history,  # 저장된 분석 이력 불러오기
    save_analysis_result,   # 분석 결과 저장
    clear_history           # 분석 이력 전체 삭제
)

# ------------------------------------------------
# PDF 분석 관련 기능 모듈
# ------------------------------------------------
from pdf import (
    summarize_pdf_text_only,    # PDF 텍스트르 OpenAI로 요약
    save_uploaded_pdf,          # 업로드된 PDF 파일 저장
    extract_text_from_pdf,      # PDF에서 텍스트 추출
    extract_images_from_pdf,    # PDF에서 이미지 추출
    extract_tables_to_excel     # PDF 표 추출 후 Excel 저장
)


# ------------------------------------------------
# 환경 설정
# ------------------------------------------------

# .env 파일 로드
load_dotenv(dotenv_path="C:/workspace/LLM/.env")

# JSON 파일 DB 초기화
# 파일이 없으면 새로 생성합니다.
init_db()

# 출력 폴더 설정
BASE_DIR = Path("output_streamlit_pdf")

# 업로드된 PDF 저장 폴더
UPLOAD_DIR = BASE_DIR / "uploads"

# 폴더가 없으면 자동 생성합니다.
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------
# 세션 상태 초기화
# ------------------------------------------------
# 현재 분석 결과 저장 변수
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# 마지막 업로드 파일 이름 저장
if "last_uploaded_filename" not in st.session_state:
    st.session_state.last_uploaded_filename = None

# st.file_uploader("PDF 파일을 업로드하세요", type=["pdf"], key=f"pdf_uploader_{st.session_state.uploader_key}")
# key=f"pdf_uploader_{st.session_state.uploader_key}" 의 값이 변경되면 "새로운 위젯"으로 인식합니다.
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0


# ------------------------------------------------
# 사이드바
# ------------------------------------------------
with st.sidebar:
    st.write("### 설정")
    st.write("업로드한 PDF를 분석하여 텍스트 요약, 표 추출, 이미지 저장을 수행합니다.")

    if st.button("분석 이력 초기화"):
        clear_history()                     # # JSON 파일에 저장된 분석 이력 삭제

        # 현재 분석 결과 제거
        st.session_state.analysis_result = None
        st.session_state.last_uploaded_filename = None

        # st.file_uploader("PDF 파일을 업로드하세요", type=["pdf"], key=f"pdf_uploader_{st.session_state.uploader_key}")
        # 파일 업로드 후 분석 이력 초기화 버튼 클릭 시 이전에 선택한 파일이 사라지지 않아 초기화를 할 때 key 값을 바꿔서 위젯 자체를 새로 만듭니다.
        # file_uploader 자체 초기화
        st.session_state.uploader_key += 1

        # 사용자에게 완료 메시지 표시
        st.success("분석 이력과 업로드 상태가 초기화되었습니다.")

        # 페이지 다시 실행
        st.rerun()


# ------------------------------------------------
# 제목
# ------------------------------------------------
st.title("PDF 논문 분석기")
st.caption("텍스트 요약 / 표 추출 Excel 저장 / 이미지 저장")

# API Key 확인
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.warning("OPENAI_API_KEY를 .env 파일에 설정해주세요.")
    st.stop()


# ------------------------------------------------
# 파일 업로드
# ------------------------------------------------
uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type=["pdf"], key=f"pdf_uploader_{st.session_state.uploader_key}")

# 새 파일이 업로드되면 이전 분석 결과를 지움
if uploaded_file is not None:
    if st.session_state.last_uploaded_filename != uploaded_file.name:
        st.session_state.analysis_result = None
        st.session_state.last_uploaded_filename = uploaded_file.name


# ------------------------------------------------
# 분석 실행
# ------------------------------------------------
if uploaded_file is not None:
    if st.button("PDF 분석 시작"):
        with st.spinner("PDF 분석 중입니다..."):
            try:
                # 업로드 파일 저장
                pdf_path = save_uploaded_pdf(uploaded_file, UPLOAD_DIR)

                # PDF 텍스트 추출
                full_text = extract_text_from_pdf(pdf_path)

                # 텍스트 요약
                summary_md = summarize_pdf_text_only(
                    pdf_text=full_text,
                    api_key=openai_api_key
                )

                # 이미지 추출
                image_paths = extract_images_from_pdf(pdf_path)

                # 표 추출 후 Excel 저장
                excel_path, table_count = extract_tables_to_excel(pdf_path)

                # JSON 이력 저장
                save_analysis_result(
                    pdf_name=uploaded_file.name,
                    pdf_path=str(pdf_path),
                    summary=summary_md,
                    image_paths=image_paths,
                    excel_path=str(excel_path) if excel_path else None,
                    table_count=table_count
                )

                # 세션 상태에 저장
                st.session_state.analysis_result = {
                    "pdf_name": uploaded_file.name,
                    "pdf_path": str(pdf_path),
                    "summary": summary_md,
                    "image_paths": image_paths,
                    "excel_path": str(excel_path) if excel_path else None,
                    "table_count": table_count
                }

                st.success("분석이 완료되었습니다.")

            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")


# ------------------------------------------------
# 현재 분석 결과 출력
# 다운로드 버튼을 눌러도 session_state 기반으로 유지됨
# ------------------------------------------------
result = st.session_state.analysis_result

if result is not None:
    st.divider()
    st.subheader("현재 분석 결과")

    st.write(f"파일명: {result['pdf_name']}")

    st.subheader("1. 텍스트 요약")
    st.markdown(result["summary"])