import sys
input = sys.stdin.readline

# N^N
# 백트래킹 : 지수시간 복잡도

def solve():
    set_queen(1)
    print(res)

# 같은 행에는 퀸을 두지 않는 로직
def set_queen(row):

    global res
    if row > N: # 유망할 때만 계속 재귀호출이 일어났으므로 기저에 왔다는건 답
        res += 1
        return
    
    # 1열부터 N열까지 시도
    for c in range(1, N+1):
        if col[c] or slash[row+c] or bslash[row-c+N]: continue # 가지치기

        col[c] = slash[row+c] = bslash[row-c+N] = 1
        set_queen(row+1)
        col[c] = slash[row+c] = bslash[row-c+N] = 0

# 격자 크기 N
N = int(input())
col = [0] * (N+1) # 1열 ~ N열
slash = [0] * (2*N + 1)
bslash = [0] * (2*N + 1)
res = 0
solve()