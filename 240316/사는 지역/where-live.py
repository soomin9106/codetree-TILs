class Place:
    def __init__(self, name, number, region):
        self.name = name
        self.number = number
        self.region = region

n = int(input())
arr = []
for _ in range(n):
    name, number, region = map(str, input().split())
    arr.append(Place(name, number, region))

arr = sorted(arr, key = lambda x: x.name, reverse = True)

print("name {}".format(arr[0].name))
print("addr {}".format(arr[0].number))
print("city {}".format(arr[0].region))