n = input()

words = dict()

for i in n:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

for word in words:
    # print(words[word])

    if words[word] == 1:
        print(word)
        exit(0)

print("None")
exit(0)