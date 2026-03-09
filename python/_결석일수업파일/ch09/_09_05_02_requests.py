# pip install requests

# requests 패키지는 파이썬에서 HTTP 요청(HTTP Requests)을 사람이 읽기 편하고 다루기 쉽게 만들어 주는 라이브러리 입니다.
import requests

# get 함수를 호출하여 서버에 데이터를 요청합니다.
response = requests.get("https://api.github.com")
print(response.status_code) # 200

# 데이터를 파이썬 딕셔너리로 변환합니다.
print(response.json())      # JSON 형식 응답 출력


# 패키지 제거
# pip uninstall requests