# pdf.py

import io
from pathlib import Path

import fitz  # PyMuPDF
import pandas as pd

# img2table
from img2table.document import PDF as Img2TablePDF
from img2table.ocr import EasyOCR
import re

from openai_service import create_openai_client

# ---------------------------
# 업로드 파일 저장
# ---------------------------
from streamlit.runtime.uploaded_file_manager import UploadedFile

def save_uploaded_pdf(uploaded_file: UploadedFile, uploaded_dir: Path) -> Path:
    uploaded_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = uploaded_dir / uploaded_file.name

    # uploaded_file : 파일 자체가 아니라 메모리에 올라온 파일 데이터 객체입니다.
    # name에는 파일 이름, size에는 파일 크기, type에는 파일 타입, getbuffer()는 실제 파일 데이터가 있습니다.
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer()) # getbuffer() 는 파일의 바이너리 데이터를 가져오는 함수입니다.
        # 메모리에 있는 PDF 데이터를 디스크 파일에 그대로 저장합니다.

    return pdf_path


# ---------------------------
# PDF 텍스트 추출
# ---------------------------
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: Path) -> str:
    text_parts = []

    # PDF 파일을 context manager로 열기
    # with 블록이 끝나면 자동으로 doc.close()가 실행됩니다.
    with fitz.open(pdf_path) as doc:

        # PDF의 모든 페이지를 순회
        for i, page in enumerate(doc): # type: ignore

            # 페이지에서 텍스트 추출 후 앞뒤 공백 제거
            page_text = page.get_text().strip()

            # 페이지 구분을 위해 페이지 번호를 함께 저장
            text_parts.append(f"\n\n--- PAGE {i+1} ---\n\n{page_text}")

    # 모든 페이지 텍스트를 하나의 문자열로 합쳐서 반환
    return "\n".join(text_parts).strip()


# ---------------------------
# 텍스트만 요약
# ---------------------------
def summarize_pdf_text_only(pdf_text: str, api_key: str) -> str:
    client = create_openai_client(api_key)

    prompt = f"""
다음은 PDF에서 추출한 텍스트입니다.

텍스트만 기준으로 한국어 마크다운 형식으로 요점 정리해 주세요.

형식:
# PDF 요약
## 문서 주제
## 핵심 내용
## 중요 개념
## 결론
## 5줄 요약

주의:
- 이미지나 표는 해석하지 말고 텍스트만 기준으로 정리해 주세요.
- 내용이 불명확하면 추측하지 말고 '텍스트에서 명확하지 않음'이라고 적어 주세요.

[텍스트 시작]
{pdf_text[:120000]}
[텍스트 끝]
"""

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt}
                ]
            }
        ]
    )

    return response.output_text.strip()


# ---------------------------
# PDF 내 이미지 추출
# page.get_images() 사용
# pdf_path : 분석할 PDF 파일 경로
# 반환값 : 저장된 이미지 파일 경로 리스트
# ---------------------------
def extract_images_from_pdf(pdf_path: Path) -> list[str]:

    # 저장된 이미지 파일 경로를 저장할 리스트
    saved_images: list[str] = []

    # 저장된 이미지 파일 경로 리스트 반환
    return saved_images


# ---------------------------
# PDF 표 추출 후 Excel 저장
# img2table 사용
# ---------------------------

def clean_excel_illegal_chars(value):

    value=""

    # 문자열이 아닌 경우 (숫자, None 등)는 그대로 반환합니다.

def clean_dataframe_for_excel(df: pd.DataFrame) -> pd.DataFrame:
    return df.map(clean_excel_illegal_chars)

def extract_tables_to_excel(pdf_path: Path) -> tuple[str, int]:
    table_count = 0
    excel_path = ""
    # Excel 파일 경로와 추출된 표 개수 반환
    return str(excel_path), table_count