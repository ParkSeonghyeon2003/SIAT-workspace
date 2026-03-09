##### 문자열 정렬 #####
fruits = ["Apple", "pineapple", "banana", "cherry"]

# 정렬
fruits.sort() # ["Apple", "banana", "cherry", "pineapple"]
print(fruits)

fruits.reverse() # ["pineapple", "cherry", "banana", "Apple"]
print("최종 리스트:", fruits)

errors = [1, "1", 2]
# errors.sort() : 에러 발생한다.