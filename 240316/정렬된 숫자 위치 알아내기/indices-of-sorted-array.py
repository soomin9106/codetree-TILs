class Number:
    def __init__(self, number, index):
        self.number = number
        self.index = index


n = int(input())
numbers = []
arr = list(map(int, input().split()))

numbers = [Number(num, i) for i, num in enumerate(arr)]

numbers.sort(key = lambda x: (x.number, x.index))


answer = [[0] for _ in range(n)]
for idx, number in enumerate(numbers):
    # print(idx, number.number, number.index)
    answer[number.index] = idx + 1

for a in answer:
    print(a, end = ' ')