n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

works = [i for i in range(1, n + 1)]
selected_works = []

def calc():
    sum1 = 0
    sum2 = 0

    remained_works = list(set(works) - set(selected_works))

    for i in range(len(selected_works)):
        for j in range(i + 1, len(selected_works)):
            val1 = selected_works[i] - 1
            val2 = selected_works[j] - 1
            sum1 += (arr[val1][val2] + arr[val2][val1])

    for i in range(len(remained_works)):
        for j in range(i + 1, len(remained_works)):
            val1 = remained_works[i] - 1
            val2 = remained_works[j] - 1
            sum2 += (arr[val1][val2] + arr[val2][val1])

    return abs(sum1 - sum2)


answer = int(1e9)
def choose_pairs(idx):
    global answer
    if len(selected_works) == n // 2:
        # 최솟값 구하는 연산 수행
        answer = min(answer, calc())
        return

    if idx >= n:
        return 

    choose_pairs(idx + 1)

    selected_works.append(works[idx])
    choose_pairs(idx + 1)
    selected_works.pop()

choose_pairs(0)
print(answer)