n, t = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

def do_simulate():
    temp1 = first[n-1]

    for i in range(n-1, 0, -1):
        first[i] = first[i - 1]
    
    first[0] = third[n-1]

    temp2 = second[n-1]

    for i in range(n-1, 0, -1):
        second[i] = second[i-1]
    
    second[0] = temp1

    for i in range(n-1, 0, -1):
        third[i] = third[i - 1]

    third[0] = temp2


for _ in range(t):
    do_simulate()

for i in range(n):
    print(first[i], end = ' ')
print()
for i in range(n):
    print(second[i], end = ' ')
print()
for i in range(n):
    print(third[i], end = ' ')