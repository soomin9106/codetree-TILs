n = int(input())


word_dict = dict()

for _ in range(n):
    word = ''.join(sorted(input()))
    
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

word_dict = sorted(word_dict.items(), key = lambda x: -x[1])

print(word_dict[0][1])