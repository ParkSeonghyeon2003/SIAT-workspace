from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, "ko_KR.UTF-8")

now = datetime.now()
formatted_now = now.strftime("%Y년 %m월 %d일 %A %H시 %M분 %S초")
print(formatted_now)