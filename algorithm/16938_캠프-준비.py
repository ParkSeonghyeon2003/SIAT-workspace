import sys
input = sys.stdin.readline

# L <= sum(문제들의 난이도) <= R
# X <= 어려운 문제 난이도 - 쉬운 문제 난이도

def recur_subset(depth=0):

    # 기저 조건: 모든 문제의 난이도를 고려하고 난 후
    if depth == N:
        return

    is_selected[depth] = True
    # 난이도 합 조건이 맞지 않으면 의미 없는 시행이다.
    # if sum_score < L or sum_score > R:
    #     is_selected[depth] = False
    #     recur_subset(depth+1)


N, L, R, X = map(int, input().split())
problem_diff = map(int, input().split())
is_selected = [False] * N