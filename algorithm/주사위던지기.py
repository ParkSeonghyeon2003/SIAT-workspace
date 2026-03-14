import sys
input = sys.stdin.readline

def dice1(depth): # 중복 순열
    # 기저 파트 : 더 이상 재귀가 실행될 수 없는 기본 파트
    if depth == N:
        print(numbers)
        return
    
    # 유도 파트 : 재귀가 유도되는 (파생되는 파트)
    # 모든 주사위의 눈이 나올 수 있다고 시도
    for i in range(1, 7):
        # 해당 수 선택
        numbers[depth] = i
        # 다음 주사사위 던지러 가기
        dice1(depth + 1)

def dice2(depth): # 순열, cnt: 던진 주사위의 횟수
    # 기저 파트 : 더 이상 재귀가 실행될 수 없는 기본 파트
    if depth == N:
        print(numbers)
        return
    
    # 유도 파트 : 재귀가 유도되는 (파생되는 파트)
    # 모든 주사위의 눈이 나올 수 있다고 시도
    for i in range(1, 7):
        # 먼저 나온 주사위의 눈과 겹치는지 확인
        if is_selected[i]: continue
        
        # 해당 수 선택
        numbers[depth] = i
        is_selected[i] = True
        
        # 다음 주사사위 던지러 가기
        dice2(depth + 1)
        
        # 다음 반복 전에 (다른 주사위 눈을 시도하기 전에) 현재 주사위 눈의 결과를 지우기
        is_selected[i] = False

def dice3(depth, start): # 중복 조합
    if depth == N:
        print(numbers)
        return
    
    for i in range(start, 7):
        numbers[depth] = i
        dice3(depth+1, i)

def dice4(depth, start): # 조합
    if depth == N:
        print(numbers)
        return
    
    for i in range(start, 7):
        numbers[depth] = i
        dice4(depth+1, i+1)

# 주사위 던지는 횟수, 모드(던지기1, 던지기3, ...)
N, M = map(int, input().split())
numbers = [0] * N # 던져진 주사위의 눈을 저장
is_selected = [False] * 7  # 인덱스에 해당하는 주사위 눈이 나왔는지 flag 저장

if M == 1:
    dice1(0)
elif M == 2:
    dice2(0)
elif M == 3:
    dice3(0, 1)
elif M == 4:
    dice4(0, 1)