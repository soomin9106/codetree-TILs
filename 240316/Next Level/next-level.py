class Level:
    def __init__(self, user_id = 'codetree', level = 10):
        self.user_id = user_id
        self.level = level



l1 = Level()
print("user {} lv {}".format(l1.user_id, l1.level))

user_id, level = map(str, input().split())

# 변경
l1.user_id = user_id
l1.level = int(level)

print("user {} lv {}".format(l1.user_id, l1.level))