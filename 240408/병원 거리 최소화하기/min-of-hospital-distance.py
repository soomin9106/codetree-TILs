def get_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

persons = []
hospitals = []
selected_hospitals = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            persons.append((i, j))
        elif arr[i][j] == 2:
            hospitals.append((i, j))

def calc():
    distance = 0
    for xp, yp in persons:
        temp_distance = int(1e9)
        for xsh, ysh in selected_hospitals:
            temp_distance = min(temp_distance, get_distance(xp, yp, xsh, ysh))

        distance += temp_distance

    return distance

answer = int(1e9)

def choose_hospitals(idx):
    global answer
    if len(selected_hospitals) == m:
        # print(selected_hospitals)
        answer = min(answer, calc())
        return
    
    if idx >= len(hospitals):
        return 

    choose_hospitals(idx + 1)

    selected_hospitals.append(hospitals[idx])
    choose_hospitals(idx + 1)
    selected_hospitals.pop()

choose_hospitals(0)

print(answer)