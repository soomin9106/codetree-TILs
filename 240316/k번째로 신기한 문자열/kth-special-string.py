n, k, t = map(str, input().split())
n = int(n)
k = int(k)


arr = []
t_len = len(t)
for _ in range(n):
    input_str = input()

    if input_str[:t_len] == t:
        arr.append(input_str)

arr.sort()

print(arr[k-1])