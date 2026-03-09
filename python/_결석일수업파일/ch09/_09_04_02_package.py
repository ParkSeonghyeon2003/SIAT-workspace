# 이번 실습을 위한 과정
"""
[구조 요약]
1. mypackage2/calc.py     :multiply 정의
2. mypackage2/__init__.py : 'from .calc import multiply'작성(입구 역할)
3. main,py           : 패키지 사용(현재 파일)
"""

# --- 패키지(Package) 개념 ---
# 여러 개의 모듈(.py)을 폴더 단위로 묶어 관리하는 구조입니다.

# --- __init__.py의 역할 ---
# 1. 패키지 인식:Python 3.3+부터는 없어도 자동으로 인식되지만, 관례상/기능상 여전히 사용합니다.
# 2. 초기화: 패키지가 import 될 때 가장 먼저 자동 실행됩니다.
# 3. 경로 단축(Expose API): 내부 모듈은 기능을 패키지 수준으로 끌어올려 사용을 편리하게 합니다.

# [원래 방식] 상세 경로를 다 적어야함
# from mypackage2.calc import multiply

# [__init__.py 활용 방식]
# __init__.py가 내부의 multiply를 미리 import 했기 때문에,
# 파일명(calc)을 생략하고 패키지 이름에서 바로 가져와 사용할 수 있습니다.
from mypackage2 import multiply

# --- 실행 결과 ---
# __init__.py를 통해 multiply를 패키지의 네임스페이스에 등록하여, 하위 모듈 참조 없이 즉시 호출 가능하게 합니다.
print(multiply(10,20))  # 결과: 200