hashmap = dict()

n = int(input())

for _ in range(n):
    commands = list(map(str, input().split()))

    if commands[0] == 'add':
        k = int(commands[1])
        v = int(commands[2])
        hashmap[k] = v

    elif commands[0] == 'remove':
        k = int(commands[1])
        hashmap.pop(k)

    else:
        k = int(commands[1])
        if k in hashmap:
            print(hashmap[k])
        else:
            print("None")