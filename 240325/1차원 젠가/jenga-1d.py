n = int(input())
arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = int(input())

# print(arr)

def in_range(idx, s, e):
    return s <= idx <= e

def remove_elements(s, e):
    global arr
    temp = []
    for idx in range(len(arr)):
        if not in_range(idx, s, e):
            temp.append(arr[idx])
    
    arr = temp
    
for _ in range(2):
    s, e = map(int, input().split())
    remove_elements(s - 1, e - 1)

print(len(arr))
for a in arr:
    print(a)