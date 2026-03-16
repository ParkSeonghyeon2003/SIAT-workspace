# 먼저 아홉 수의 합을 구한다.
# 두 수의 조합을 뽑아, 그 합을 아홉 수의 합에서 뺀다.
# 답은 유일하므로, 뺀 결과가 100으로 떨어지면 그 두 수만 제외한 일곱 수가 답이 된다.

import sys
input = sys.stdin.readline

def find_fake():
    for i in range(8):
        for j in range(i+1, 9):
            if sum_tup - tup[i] - tup[j] == 100:
                return i, j

tup = tuple(map(int, [input() for _ in range(9)]))
sum_tup = sum(tup)

fake_idx1, fake_idx2 = find_fake()

for i in range(9):
    if i == fake_idx1 or i == fake_idx2:
        continue
    print(tup[i])
