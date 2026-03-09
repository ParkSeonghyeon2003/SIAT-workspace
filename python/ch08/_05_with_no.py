file = None

try:
    file = open("info.txt", "r")
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
finally:
    if file is not None:
        file.close()