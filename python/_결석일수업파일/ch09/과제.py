
from datetime import datetime, date
import locale                   # 요거
from datetime import datetime   # 요거 추가


now = datetime.now()   
print(now)


locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')  # 요거
formatted_now = now.strftime("%Y년 %m월 %d일 %A %H시 %M분 %S초")
print(formatted_now)
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')  # 요거
now = datetime.now()
formatted_now = now.strftime("%Y년 %m월 %d일 %A %H시 %M분 %S초")
print(formatted_now)

today = date.today()  
print("현재 날짜:", today)