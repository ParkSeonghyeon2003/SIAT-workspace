from pathlib import Path

file_path = Path(__file__).resolve().parent / "original" / "gugudan.txt"

if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
        print(data)
else:
    print("파일이 존재하지 않습니다. 먼저 저장 코드를 실행해 주세요.")
