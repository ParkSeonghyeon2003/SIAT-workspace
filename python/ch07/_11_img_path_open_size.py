from pathlib import Path

cur_file_path = Path(__file__).resolve()
base_dir = cur_file_path.parent

src_dir = base_dir / "original"
dst_dir = base_dir / "target"
original_filename = "tree.jpg"
src_path = src_dir / original_filename

# 복사본 디렉토리 없으면 생성
dst_dir.mkdir(parents=True, exist_ok=True)

if src_path.is_file():
    # 읽기
    with open(src_path, "rb") as f_src:
        with open(dst_dir / original_filename, "wb") as f_dst:
            while True:
                chunk = f_src.read(1024 * 1024) # 1MB
                if not chunk:
                    break
                f_dst.write(chunk)

print("성공적으로 이미지를 복사했습니다.")