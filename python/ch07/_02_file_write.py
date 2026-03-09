from pathlib import Path

data_folder = Path(__file__).resolve().parent / "data" / "write"
if not data_folder.exists():
    data_folder.mkdir(parents=True)
    print(f"{data_folder} 폴더를 생성했습니다.")
else:
    print("이미 폴더가 존재하므로 생성하지 않습니다.")

f = open(data_folder / "example.txt", "w", encoding="utf-8")
f.write("Hello, Python!\n")
f.write("파일 입출력 예제입니다.\n")
f.close()