numbers = [0, 1, 2, 3]

##### 삭제 #####
numbers.remove(2) # [0, 1, 3]
print(numbers)

removed = numbers.pop() # [0, 1]
print(numbers)
print("삭제된 값:", removed)

new_numbers = numbers.pop(1) # [0]
print(new_numbers)
print(numbers)

# 리스트 연결
a = [10, 20, 30]
b = [40, 50, 60]
c = a + b
print(c) # [10, 20, 30, 40, 50, 60]

# clear: 리스트 비우기
c.clear()
print(c) # []

# 아예 할당 해재하는 법: del
del c # None

numbers = [0, 1, 2, 3]
del numbers[1]
print(numbers) # [0, 2, 3]

numbers = [10, 20, 30, 40, 10]
result = numbers.index(40) # 3
print(result)

result = numbers.count(10) # 2
print(result)