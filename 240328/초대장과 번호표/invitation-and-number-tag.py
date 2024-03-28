from collections import deque

n, g = map(int, input().split())

invited = [False] * n
# 각 그룹마다 초대장 받지 못한 사람
groups = [set() for _ in range(g)]
# 각 사람이 어떤 그룹에 속하는지
people_groups = [[] for _ in range(n)]

q = deque()
ans = 0

for i in range(g):
    nums = list(map(int, input().split()))[1:]

    for num in nums:
        num -= 1
        groups[i].add(num)
        people_groups[num].append(i)


q.append(0)
invited[0] = True

while q:
    cur = q.popleft()
    ans += 1

    for g_num in people_groups[cur]: # cur 이 소속된 그룹 번호들
        groups[g_num].remove(cur) # cur 을 삭제 해줌

        if len(groups[g_num]) == 1: # 해당 그룹 사람이 1명이 되었을 경우 => 초대
            p_num = list(groups[g_num])[0]

            if not invited[p_num]:
                invited[p_num] = True
                q.append(p_num)

print(ans)