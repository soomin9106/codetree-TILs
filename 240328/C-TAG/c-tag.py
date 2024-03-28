from itertools import combinations

n, m = map(int, input().split())

ag = []
for _ in range(n):
    ag.append(input())

bg = []

for _ in range(n):
    bg.append(input())

answer = 0

# 가능한 인덱스 조합 생성
combs = combinations(range(m), 3)

for selected_idxs in combs:
    aset = set()
    bset = set()
    
    for a in ag:
        new_a = ''
        for s in selected_idxs:
            new_a += a[s]
        aset.add(new_a)

    for b in bg:
        new_b= ''
        for s in selected_idxs:
            new_b += b[s]
        bset.add(new_b)

    alen = len(aset)
    blen = len(bset)
    if len(aset | bset) == alen + blen:
        answer += 1

print(answer)