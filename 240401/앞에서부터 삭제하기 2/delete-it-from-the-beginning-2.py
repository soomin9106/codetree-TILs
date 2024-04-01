import heapq

n = int(input())
arr = list(map(int, input().split()))

answer = -int(1e9)
for k in range(1, n - 1):
    temp_arr = arr[k:]
    heapq.heapify(temp_arr)

    temp_ans = sum(temp_arr[1:]) / (len(temp_arr) - 1)

    answer = max(answer, temp_ans)

formatted_number = f"{answer:.2f}"
print(formatted_number)