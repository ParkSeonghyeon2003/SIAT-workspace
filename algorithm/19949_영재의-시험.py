import sys
input = sys.stdin.readline

# depth : 재귀 깊이 (겸 문제 번호)
# correct : 현재 맞은 문제 수
def recursive(depth=0, correct=0):
    global cnt

    if depth == 10:
        if correct >= 5:
            cnt += 1
        return

    for answer in range(1, 6):
        if depth >= 2 and answers[-2] == answer and answers[-1] == answer: continue
        answers.append(answer)
        next_correct = correct + (1 if solutions[depth] == answer else 0)
        recursive(depth + 1, next_correct)
        answers.pop()

solutions = list(map(int, input().split()))
answers = []
cnt = 0
recursive(0, 0)
print(cnt)
