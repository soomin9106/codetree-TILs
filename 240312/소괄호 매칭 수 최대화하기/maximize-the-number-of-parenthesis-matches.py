n = int(input())

arr = []

for _ in range(n):
    s = input()
    arr.append([s.count("("), s.count(")"), s])

arr = sorted(arr, key = lambda x: (-x[0], x[1]))

new_str = ""
for i in range(len(arr)):
    new_str += arr[i][2]

stack = []
ans = 0
for i in range(len(new_str)):
    if new_str[i] == "(":
        stack.append("(")
    else:
        ans += len(stack)

print(ans)