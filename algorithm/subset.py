import sys
input = sys.stdin.readline

# N개의 입력된 수로 이루어진 집합의 모든 가능한 부분 집합을 생성
# 2 4 5

def subset(idx):
    
    if idx == N: # 해당 원소가 없는, 즉 모든 원소를 다 고려했다면 부분집합 완성!!
        result = [ numbers[i] if is_selected[i] else 'X' for i in range(N) ]
        print(*result)
        return

    # 이 원소를 부분집합에 포함시킴
    is_selected[idx] = True
    # 다음 원소로 가기
    subset(idx+1)
    # 이 원소를 부분집합에 포함시키지 않음
    is_selected[idx] = False
    # 다음 원소로 가기
    subset(idx+1)

def subset2(idx, pick_list):
    
    if idx==N:
        if len(pick_list):
            print(pick_list)
        return
    
    # 부분집합에 포함
    subset2(idx+1, pick_list+[numbers[idx]])
    # 부분집함에 비포함
    subset2(idx+1, pick_list)

N = int(input()) # 원소 수
numbers = list(map(int, input().split()))
is_selected = [False] * N # idx에 해당하는 numbers[idx] 수가 부분집합에 구성에 선택되었는지 여부

# subset(0)
subset2(0, [])