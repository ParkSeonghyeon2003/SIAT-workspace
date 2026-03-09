nums = [5, 2, 9, 1, 7]
sorted_nums = sorted(nums)
print(sorted_nums)
print(nums)

sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)

words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)

students = [("Kim", 82), ("Lee", 91), ("Park", 78)]

sorted_by_score = sorted(students, key=lambda x: x[1])
print(sorted_by_score)

sorted_by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_by_score_desc)