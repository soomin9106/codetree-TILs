alen, blen = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(len(set(a) - set(b)) + len(set(b) - set(a)))