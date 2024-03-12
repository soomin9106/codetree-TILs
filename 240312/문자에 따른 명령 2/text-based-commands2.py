n = input()
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0
direction = 3


for s in n:
    if s == 'F':
        x, y = x + dx[direction], y + dy[direction]
    
    if s == 'L':
        direction = (direction - 1 + 4) % 4
    
    if s == 'R':
        direction = (direction + 1) % 4

print(x, y)