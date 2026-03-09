fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])

##### Slicing #####
print(fruits[0:2])

##### List 수정 및 삭제 #####
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)

##### 삭제 #####
del fruits[0]
print(fruits)

del fruits

##### in 연산자 #####
data = [23, 49, 29, 20]
print(0 in data)
print(20 in data)

print(0 not in data)