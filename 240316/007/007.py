class Information:
    def __init__(self, code, space, time):
        self.code = code
        self.space = space
        self.time = time


c, s, t = map(str, input().split())
info1 = Information(c, s, int(t))

print("secret code : {}".format(info1.code))
print("meeting point : {}".format(info1.space))
print("time : {}".format(info1.time))