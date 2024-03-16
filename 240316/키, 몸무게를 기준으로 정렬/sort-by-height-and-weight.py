class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

students = []
for _ in range(n):
    name, height, weight = map(str, input().split())

    students.append(Student(name, int(height), int(weight)))

students = sorted(students, key = lambda x: (x.height, -x.weight))

for s in students:
    print(s.name, s.height, s.weight)