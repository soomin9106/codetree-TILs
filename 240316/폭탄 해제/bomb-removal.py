class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec


code, color, sec = map(str, input().split())

bomb = Bomb(code, color, int(sec))

print("code : {}".format(bomb.code))
print("color : {}".format(bomb.color))
print("second : {}".format(bomb.sec))