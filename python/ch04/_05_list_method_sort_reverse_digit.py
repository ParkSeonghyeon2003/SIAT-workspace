##### 숫자 정렬 (정수형) #####
numbers = [0, 1, 3, 2]
numbers.reverse() # [2, 3, 1, 0]
print(numbers)

numbers.sort() # [0, 1, 2, 3]
print(numbers)

numbers.reverse() # [3, 2, 1, 0]
print("최동 리스트:", numbers)

##### 숫자 정렬 (실수형 포함) #####
numbers = [0.2, 9, 3.5, 8]

numbers.sort() # [0.2, 3.5, 8, 9]
print(numbers)

numbers.reverse() # [9, 8, 3.5, 0.2]
print("최종 리스트:", numbers)