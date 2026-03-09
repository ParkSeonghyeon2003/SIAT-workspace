# 현재 위치에서 하위 폴더인 mypackage3 폴더를 만들고 calc.py를 복사합니다.

# [의미] mypackage3 폴더 안의 calc.py 모듈에 정의된 모든(*) 기능을 현재 파일로 가져옵니다.
# 1. 'calc.' 이라는 파일명을 앞에 붙이지 않고도 multiply(), sub() 등을 직접 호출할 수 있습니다.
# 2. 이 방식은 __init__.py 파일의 설정 유무와 관계없이 '파일(모듈)'에 직접 접근하여 작동합니다.
from mypackage3.calc import *

print(multiply(2, 10))
print(sub(2, 10))