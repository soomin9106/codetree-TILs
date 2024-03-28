alen, blen = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 식으로는 이거임
# set(a-b | b-a)

# a - b 
ab = []
for item in a:
    if item not in b:
        ab.append(item)

# b - a
ba = []
for item in b:
    if item not in a:
        ba.append(item)

print(len(set(ab + ba)))