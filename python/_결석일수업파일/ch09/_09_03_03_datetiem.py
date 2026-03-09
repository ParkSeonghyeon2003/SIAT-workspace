# datetime: 날짜와 시간을 모두 포함하는 객체입니다.
# date: 날짜(년, 월, 일) 정보만 다루는 객체입니다.
# time: 시간(시, 분, 초, 마이크로초) 정보만 다루는 객체입니다.
from datetime import datetime, date

now = datetime.now()    # 실행되는 순간의 년-월-일 시:분:초.마이크로초 정보를 가져옵니다.
print(now)

# 각 기호(포멧 코드)는 특정 날짜.시간 단위를 의미합니다.
# %Y: 년, %m: 월, %d: 일, %A: 요일(영문), %H: 시, %M: 분, %S: 초
formatted_now = now.strftime("%Y년 %m월 %d일 %A %H시 %M분 %S초")
print(formatted_now)

formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_now)

today = date.today()    # 실행되는 순간의 년-월-일 정보만 가져옵니다.
print("현재 날짜:", today)