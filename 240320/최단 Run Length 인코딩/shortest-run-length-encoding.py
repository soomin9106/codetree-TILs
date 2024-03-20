a = input()
n = len(a)

def shift(a_list):
    temp = a_list[-1]

    for i in range(n - 2, -1, -1):
        a_list[i+1] = a_list[i]

    a_list[0] = temp

    return ''.join(a_list)

def calc_encoding(str_n):
    temp = str_n[0]
    count = 1
    res = ''
    for i in range(1, n):
        if str_n[i] == temp:
            count += 1
        else:
            res += str(count)
            res += temp
            temp = str_n[i]
            count = 1

    res += str(count)
    res += temp
        
    
    return res

answer = int(1e9)
for _ in range(n):
    a_list = list(a)
    a = shift(a_list)
    res = calc_encoding(a)
    # print(a, res)
    if answer > len(res):
        answer = len(res)

print(answer)