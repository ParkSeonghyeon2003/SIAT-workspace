import sys
input = sys.stdin.readline

def solve():
    powerset(0, 0, 1e7, 0, 0)
    print(res)


def powerset(idx, max_ex, min_ex, total, pick_cnt):
    global res
    
    if total > R: return
    if idx == N:
        # 2문제 이상 선택, L<=난이도의합<=R, max_ex-min_ex >= X
        if pick_cnt >= 2 and L <= total <= R and max_ex - min_ex >= X:
            res += 1
        return
    
    # idx 문제 부분집합에 포함
    powerset(idx+1, max(max_ex, ex_list[idx]), min(min_ex, ex_list[idx]), total+ex_list[idx], pick_cnt+1)
    # idx 문제 부분집합에 비포함
    powerset(idx+1, max_ex, min_ex, total, pick_cnt)


def powerset2(idx, max_ex, min_ex, total, ):
    global res
    
    if total > R: return
    if idx == N:
        # 2문제 이상 선택, L<=난이도의합<=R, max_ex-min_ex >= X
        if L <= total <= R and max_ex - min_ex >= X:
            res += 1
        return
    
    # idx 문제 부분집합에 포함
    powerset2(idx+1, max(max_ex, ex_list[idx]), min(min_ex, ex_list[idx]), total+ex_list[idx])
    # idx 문제 부분집합에 비포함
    powerset2(idx+1, max_ex, min_ex, total)

N, L, R, X = map(int, input().split())
ex_list = list(map(int, input().split()))
pick_list = []
res = 0
solve()