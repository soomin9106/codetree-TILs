class Weather:
    def __init__(self, day, date, w):
        self.day = day
        self.date = date
        self.w = w


n = int(input())
w_info = []

for _ in range(n):
    date, day, w = map(str, input().split())

    w_info.append(Weather(day, date, w))

w_info = sorted(w_info, key = lambda x: x.date)

for w in w_info:
    if w.w == 'Rain':
        print(w.date, w.day, w.w)
        exit(0)