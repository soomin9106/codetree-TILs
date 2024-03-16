n = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

if arr1.sort() == arr2.sort():
    print("Yes")
else:
    print("No")