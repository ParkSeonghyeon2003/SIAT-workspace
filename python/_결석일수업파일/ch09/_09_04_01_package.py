# 패키지(Package)
# 패키지는 여러 개의 모듈을 폴더(디렉터리)로 묶은 것입니다.

# 실습을 위한 과정
# 1. 현재 폴더에서 mypackage를 만듭니다.
# 2. mypackage 폴더에서 calculator.py 와 geometry.py를 만듭니다.

# 패키지 이름만 사용
from mypackage import calculator
#from mypackage.calculator import add
print(calculator.add(2,3))

# 패키지.모듈 사용
from mypackage.geometry import area_circle

print(area_circle(5))