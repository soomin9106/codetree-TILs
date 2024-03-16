s1 = input()
s2 = input()

s1 = sorted(s1)
s2 = sorted(s2)

if len(s1) != len(s2):
    print("No")
    exit(0)

for i in range(len(s1)):
    if s1[i] != s2[i]:
        print("No")
        exit(0)

print("Yes")