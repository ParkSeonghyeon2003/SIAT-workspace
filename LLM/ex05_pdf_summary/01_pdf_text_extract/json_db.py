# json_db.py

# JSON 데이터 처리를 위한 라이브러리
import json

# 파일 경로를 객체 형태로 다루기 위한 라이브러리
from pathlib import Path


# 분석 이력을 저장할 JSON 파일 경로
DB_FILE = Path("pdf_analysis_history.json")


# ------------------------------------------------
# 기본 데이터 구조 생성
# ------------------------------------------------
def get_default_data() -> dict[str, list]:

    # JSON 파일이 처음 생성될 때 사용할 기본 구조
    # history : 분석 이력을 저장하는 리스트
    return {
        "history": []
    }


# ------------------------------------------------
# JSON DB 초기화
# ------------------------------------------------
def init_db() -> None:

    # JSON 파일이 존재하지 않으면 새로 생성합니다.
    if not DB_FILE.exists():

        # 기본 데이터를 JSON 문자열로 변환하여 파일에 저장합니다.
        DB_FILE.write_text(

            # json.dumps()
            # Python 객체 → JSON 문자열로 변환
            json.dumps(
                get_default_data(),

                # 한글이 깨지지 않도록 설정
                ensure_ascii=False,

                # JSON을 보기 좋게 들여쓰기
                indent=2
            ),

            # 파일 저장 인코딩
            encoding="utf-8"
        )


# ------------------------------------------------
# JSON 데이터 읽기
# ------------------------------------------------
def load_data() -> dict[str, list]:

    # JSON 파일이 없으면 먼저 생성
    init_db()

    # JSON 파일 내용을 문자열로 읽기
    text = DB_FILE.read_text(encoding="utf-8")

    # 파일이 비어있는 경우 처리
    if not text.strip():

        # 기본 데이터 생성
        data = get_default_data()

        # JSON 파일에 저장
        save_data(data)

        # 기본 데이터 반환
        return data


    # JSON 문자열 → Python 객체(dict) 변환
    data = json.loads(text)

    # history 키가 없으면 생성
    if "history" not in data:
        data["history"] = []

    return data


# ------------------------------------------------
# JSON 데이터 저장
# ------------------------------------------------
def save_data(data: dict[str, list]) -> None:
    
    # Python 객체(dict)를 JSON 파일로 저장
    DB_FILE.write_text(

        json.dumps(
            data,

            # 한글을 그대로 저장
            ensure_ascii=False,

            # 보기 좋게 들여쓰기
            indent=2
        ),

        # 파일 인코딩
        encoding="utf-8"
    )


# ------------------------------------------------
# 분석 이력 가져오기
# ------------------------------------------------
def load_analysis_history() -> list:

    # JSON 데이터 읽기
    data = load_data()

    # history 리스트 반환
    return data["history"]


# ------------------------------------------------
# 분석 결과 저장
# ------------------------------------------------
def save_analysis_result(pdf_name: str, pdf_path: str, summary: str, image_paths: list[str], excel_path: str | None, table_count: int) -> None:

    # 현재 JSON 데이터 로드
    data = load_data()

    # 새로운 분석 결과를 history 리스트에 추가
    data["history"].append({
        "pdf_name": pdf_name,       # PDF 파일 이름
        "pdf_path": pdf_path,       # PDF 파일 경로
        "summary": summary,         # AI 요약 결과
        "image_paths": image_paths, # 추출된 이미지 경로 리스트
        "excel_path": excel_path,   # 추출된 표 Excel 파일 경로
        "table_count": table_count  # 추출된 표 개수
    })

    # JSON 파일에 저장
    save_data(data)


# ------------------------------------------------
# 분석 이력 초기화
# ------------------------------------------------
def clear_history() -> None:

    # 기본 데이터 구조로 JSON 파일을 다시 저장
    # 즉 history 리스트를 비우는 효과
    save_data(get_default_data())