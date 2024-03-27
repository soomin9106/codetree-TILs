n = int(input())

hashset = set()

for _ in range(n):
    command, num = map(str, input().split())
    num = int(num)
    if command == 'find':
        if num in hashset:
            print("true")
        else:
            print("false")
    elif command == 'add':
        hashset.add(num)
    else:
        hashset.remove(num)