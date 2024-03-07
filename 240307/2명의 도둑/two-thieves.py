import sys

n, m, c = map(int, input().split())
weights = []

for _ in range(n):
    weights.append(list(map(int, input().split())))

all_matches = []  # 가능한 조합 모두 담는 리스트


for i in range(n):
    for j in range(n):
        if j + m - 1 < n:
            all_matches.append([i, j + m - 1, weights[i][j: j + m]])

# print(all_matches)

def isPossibleMatch(mx1, my1, mx2, my2):
    if mx1 != mx2:
        return True
    if my1 < mx2 or my2 < mx1:
        return True
    return False

# 가치 계산
def calc_val(mm):
    val = 0
    if sum(mm) <= c:
        for item in mm:
            val += (item * item)
    else:
        for i in range(2 ** m):  
            selected_items = [mm[j] for j in range(m) if (i & (1 << j)) > 0]
            if sum(selected_items) <= c:
                temp = sum([x * x for x in selected_items])
                val = max(val, temp)
    return val

selected_matches = []

res = -int(1e9)

def dfs(cnt, i):
    global res
    if cnt == 2:
        # print(selected_matches)
        if not isPossibleMatch(selected_matches[0][0], selected_matches[0][1], selected_matches[1][0], selected_matches[1][1]):
            return
        match_res = 0
        for match in selected_matches:
            match_res += calc_val(match[-1])
        res = max(res, match_res)
        return

    for idx in range(i, len(all_matches)):
        selected_matches.append(all_matches[idx])
        dfs(cnt + 1, idx + 1)
        selected_matches.pop()

dfs(0, 0)
print(res)