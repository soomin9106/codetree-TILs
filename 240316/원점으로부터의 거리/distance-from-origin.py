class Point:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number =number

points = []

n = int(input())

for num in range(1, n+1):
    x, y = map(int, input().split())
    points.append(Point(x, y, num))

points = sorted(points, key = lambda k: abs(0 - k.x) + abs(0 - k.y))

for p in points:
    print(p.number)