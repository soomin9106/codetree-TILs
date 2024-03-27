n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

setArr1 = set(arr1)

for a in arr2:
    if a in setArr1:
        print(1)
    else:
        print(0)