import sys

n, m, c = map(int, input().split())
weights = []

for _ in range(n):
    weights.append(list(map(int, input().split())))


all_matches = [] # 가능한 조합 모두 담는 리스트

for i in range(n):
    for j in range(n):
        if j + m - 1 < n:
            all_matches.append(weights[i][j: j+m])


def isPossibleMatch(m1, m2):
    return m1[-1] < m2[0] or m2[-1] < m1[0]

# 가치 계산
def calc_val(m):
    val = 0
    if sum(m) <= c:
        for item in m:
            val += (item * item)
    else:
        max_item = max(m)
        val += (max_item * max_item)
    return val

selected_matches = []


res = -int(1e9)
def dfs(cnt, i):
    global res
    if cnt == 2:
        if isPossibleMatch(selected_matches[0], selected_matches[1]):
            return
        match_res = 0
        for match in selected_matches:
            match_res += calc_val(match)
        res = max(res, match_res)
        return

    for idx in range(i, len(all_matches)):
        selected_matches.append(all_matches[idx])
        dfs(cnt + 1, idx + 1)
        selected_matches.pop()

dfs(0, 0)
print(res)