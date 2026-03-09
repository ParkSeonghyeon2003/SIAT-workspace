# error = 1 / 0

print(False and (1/0)) # 에러 없이 False 출력

print(True or (1/0)) # 에러 없이 True 출력

print(10 and 20) # 20 평가되어 출력(and는 두개 모두 참이어야 하기 때문)
print(0 and 20)  # 0만 평가되어 출력(False가 나오면 뒤를 평가할 이유 없음)

print(0 or 20)   # 20 (둘 중 하나는 참이어야 하니까 뒤까지 평가)
print(10 or 20)  # 10 (앞에서 이미 참이 나왔으니까 뒤는 볼 필요가 없으니)