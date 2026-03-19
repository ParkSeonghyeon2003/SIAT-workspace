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
    # 문자열 경로를 Path 객체로 변환합니다.
    # Path 객체를 사용하면 파일 경로 조작이 편리합니다.
    pdf_path = Path(pdf_path)

    # pdf_path.name은 파일 전체 이름
    # pdf_path.stem은 확장자 제외 이름
    # pdf_path.suffix는 확장자

    # 이미지 저장 폴더를 생성합니다.
    # 예: output_streamlit_pdf/images/crop-model
    output_dir = pdf_path.parent.parent / "images" / pdf_path.stem
    
    # 폴더가 없으면 자동 생성합니다.
    # parnets=True : 상위 폴더까지 함께 생성
    # exists_ok=True : 폴더가 이미 있어도 오류 발생하지 않음
    output_dir.mkdir(parents=True, exist_ok=True)

    # PyMuPDF(fitz)를 이용하여 PDF 파일을 엽니다.
    # with 블록이 끝나면 자동으로 doc.close()가 실행됩니다.
    with fitz.open(pdf_path) as doc:

        # 저장된 이미지 파일 경로를 저장할 리스트
        saved_images: list[str] = []

        # 전체 이미지 번호를 관리하기 위한 변수
        image_index: int = 1

        # enumerate(..., start=1) → 페이지 번호를 1부터 시작
        for page_num, page in enumerate(doc, start=1): # type: ignore
            
            # 현재 페이지에 포함된 이미지 목록을 가져옵니다.
            # full=True : 이미지의 전체 정보 가져오기
            image_list = page.get_images(full=True)

            # 페이지 안의 모든 이미지를 반복합니다.
            for img in image_list:

                # img 튜플의 첫 번째 값은 이미지의 xref ID 입ㄴ디ㅏ.
                # xref는 PDF 내부에서 이미지 객체를 식별하는 번호입니다.
                xref = img[0]

                # xref를 이용하여 실제 이미지 데이터를 추출합니다.
                base_image: dict = doc.extract_image(xref)

                # 이미지의 바이너리 데이터 (실제 이미지 파일 데이터)
                image_bytes = base_image["image"]

                # 이미지 확장자 (png, jpg 등)
                image_ext = base_image["ext"]

                # 저장할 이미지 파일 경로 생성
                # page_001_img_001.png 같은 형식으로 저장합니다.
                # :03d → 숫자를 3자리로 표현 (예: 1 → 001)
                image_path: Path = output_dir / f"page_{page_num:03d}_img_{image_index:03d}.{image_ext}"

                # 이미지 파일을 바이너릴 모드로 저장합니다.
                with open(image_path, "wb") as f:

                    # 이미지 데이터를 파일로 기록합니다.
                    f.write(image_bytes)

                # 저장된 이미지 경로를 리스트에 추가합니다.
                saved_images.append(str(image_path))

                # 다음 이미지를 위해 번호 증가
                image_index += 1

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