n, m = map(int, input().split())

T = list(map(int, input().split()))

sum = 0
for i in range(m):
    sum += T[i]

max_result = sum
for i in range(1, n-m+1):
    sum = sum - T[i-1] + T[i+m-1]
    max_result = max(max_result, sum)
    
print(max_result)