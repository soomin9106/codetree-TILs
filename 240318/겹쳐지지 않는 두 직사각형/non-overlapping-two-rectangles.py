n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

matches = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# matches 에 추가
def add_match(w, h, x, y):
    match_points = []
    flag = True
    for i in range(w):
        for j in range(h):
            temp_x, temp_y = x + i, y + j
            if in_range(temp_x, temp_y):
                match_points.append((temp_x, temp_y))
            else:
                flag = False # 만들 수 없는 경우

    if not flag:
        return []

    return match_points


# matches 채워넣기
for w in range(1, n + 1):
    for h in range(1, m + 1):
        for x in range(n):
            for y in range(m):
                match_points = add_match(w, h, x, y)
                if len(match_points) != 0:
                    matches.append(match_points)

# 중복 검사
def check_duplicates(result_list):
    # 빈 세트를 만들어서 중복을 검사할 값들을 저장합니다.
    seen = set()

    # 주어진 리스트를 순회하면서 중복 여부를 확인합니다.
    for sublist in result_list:
        # 첫 번째 요소와 두 번째 요소를 모두 세트에 추가합니다.
        for item in sublist:
            if item in seen:
                # 이미 세트에 있는 경우 중복이므로 True를 반환합니다.
                return True
            seen.add(item)

    # 중복이 발견되지 않은 경우 False를 반환합니다.
    return False

# 한 리스트 안에 있는 요소들 합 계산
def calc_sum(match_point):
    res = 0
    for point in match_point:
        res += arr[point[0]][point[1]]

    return res

# 두 조합이 안겹치는지 확인하고, 안겹친다면 합 계산
def calc(selected_matches):
    res = 0
    if check_duplicates(selected_matches):
        # 겹치는 경우임
        return None
    else:
        for m in selected_matches:
            res += calc_sum(m)

    return res

# matches 에서 2개의 조합 선택 후 비교 + 합 구하기
selected_matches = []
max_res = -int(1e9)

def choose_matches(L, start):
    global max_res
    if L == 2:  # 2개를 선택했을 때 동작을 수행
        temp = calc(selected_matches)
        if temp:
            max_res = max(max_res, temp)
        return

    for i in range(start, len(matches)):
        selected_matches.append(matches[i])
        choose_matches(L + 1, i + 1)  # 다음 매치를 선택하기 위해 재귀 호출
        selected_matches.pop()  # 선택된 매치 다시 제거

# print(matches)
choose_matches(0, 0)
print(max_res)