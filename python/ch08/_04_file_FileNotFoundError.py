try:
    with open("info.txt", "r") as file:
        data = file.read()
except FileNotFoundError as e:
    print("파일이 존재하지 않습니다.\n", e)