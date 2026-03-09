class MyList:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, newValue):
        self.items[index] = newValue

lst = MyList([1, 2, 3])

# 1. lst[1] = 99 코드가 실행되면
# 2. 파이썬은 내부적으로 lst.__setitem__(1, 99)를 호출합니다.
# 3. self.items[1]의 값이 2에서 99로 교체됩니다.
lst[1] = 99

# 결과 확인
print(lst.items)