from pathlib import Path

print(__file__)
print(type(__file__))

current_file_path = Path(__file__).resolve()
print(f"현재 파일의 전체 경로: {current_file_path}")

# Parent
base_dir = current_file_path.parent
print(f"1. 현재 파일이 위치한 폴더: {base_dir}")
print(f"2. 상위의 상위 폴더: {base_dir.parent}")

# 파일 이름 및 확장자
print(f"3. 파일명 전체: {current_file_path.name}")
print(f"4. 파일명만(확장자 제외): {current_file_path.stem}")
print(f"5. 확장자만: {current_file_path.suffix}")

# 새로운 경로 생성
data_folder = base_dir / "data" / "write"
print(f"6. 합쳐진 경로: {data_folder}")

# 실제 파일/폴더 존재 여부 및 생성
if not data_folder.exists():
    data_folder.mkdir(parents=True)
    print(f"7. {data_folder} 폴더를 생성했습니다.")
else:
    print("7. 이미 폴더가 존재하므로 생성하지 않습니다.")

# 폴더 내 파일 목록 가져오기
print("8. 현재 폴더 내 파이썬 파일 목록")
for py_file in base_dir.glob("*.py"):
    print(f"    - {py_file.name}")