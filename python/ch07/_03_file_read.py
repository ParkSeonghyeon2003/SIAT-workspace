from pathlib import Path

data_folder = Path(__file__).resolve().parent / "data" / "write"
if not data_folder.exists():
    data_folder.mkdir(parents=True)
    print(f"{data_folder} 폴더를 생성했습니다.")
else:
    try:
        f = open(data_folder / "example.txt", "r", encoding="utf-8")
        content = f.read()
        f.close()

        print(content)
    except FileExistsError:
        print("파일이 존재하지 않습니다.")