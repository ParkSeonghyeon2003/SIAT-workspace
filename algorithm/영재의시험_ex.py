


# 영재가 10문제의 답을 찍기
# 중복 순열

import sys
input = sys.stdin.readline

def solve() -> None:
    pick_ans(0, 0, 0, 0)
    print(res)

# 현재 문제에 가능한 답 다 찍어보기
def pick_ans(idx: int, score: int, before: int, b_cnt: int): # 문제 index, 현재까지 얻은 점수, 직전 문제에 찍은 답, 직전 문제에 찍은 답의 연속 개수

    if score + (10-idx) < 5: return

    global res
    if idx == 10:
        res += 1
        return

    for i in range(1, 6): # i: 찍는 답
        if before == i and b_cnt == 2: continue # 가지치기
        pick_ans(idx + 1, score + (1 if ans[idx] == i else 0), i, b_cnt + 1 if before == i else 1)


ans = list(map(int, input().split()))
res = 0
solve()