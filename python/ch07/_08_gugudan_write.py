from pathlib import Path

dir_path = Path(__file__).resolve().parent / "original"
if not dir_path.exists():
    dir_path.mkdir(parents=True)
    print(f"{dir_path} 폴더를 생성했습니다.")

with open(dir_path / "gugudan.txt", "w", encoding="utf-8") as f:
    f.write("=== 파이썬 구구단 프로그램 ===\n")
    for dan in range(2, 10):
        f.write(f"\n--- {dan}단 ---\n")
        for i in range(1, 10):
            f.write(f"{dan} x {i} = {dan * i}\n")

print()
print(f"{dir_path}에 gugudan.txt가 성공적으로 생성되었습니다.")
print()