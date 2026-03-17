import sys
input = sys.stdin.readline

# depth : 재귀 깊이 (겸 문제 번호)
# correct : 현재 맞은 문제 수
def recursive(depth=0, correct=0):
    global cnt

    # 기저 조건 : 10문제까지 풀고 온 경우
    if depth == 10:
        # 5문제 이상 맞으면 경우의 수 +1
        if correct >= 5:
            cnt += 1
        return

    # 오지선다 돌리기
    for answer in range(1, 6):
        # 연달아 3개를 같은 답을 적을 경우는 배제한다.
        if depth >= 2 and answers[-2] == answer and answers[-1] == answer: continue
        
        # 지금까지의 답은 answer 리스트에 저장한다.
        answers.append(answer)
        # 재귀 호출로 다음 문제로 넘어간다.
        next_correct = correct + (1 if solutions[depth] == answer else 0)
        recursive(depth + 1, next_correct)
        # 다음 선지를 담기위해 하나 뽑아 버린다.
        answers.pop()

# 정답 10개 리스트
solutions = list(map(int, input().split()))

# 답변 기록용 리스트
answers = []

# 경우의 수 카운터
cnt = 0

# 재귀 호출 시작
recursive()
print(cnt)
