# mypackage3 폴더를 복사해서 mypackage4 폴더를 만들고 __init__.py 작성합니다.

# __all__ = ["multiply"] 설정 때문에 sub()를 사용할 수 없습니다.
from mypackage4 import *

print(multiply(2,10))   # 20
print(sub(2, 10))     
# NameError: name 'sub' is not defined. Did you mean: 'sum'?