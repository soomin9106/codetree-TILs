class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())

students = []
for i in range(1, n + 1):
    height, weight = map(int, input().split())
    students.append(Student(height, weight, i))

students = sorted(students, key = lambda x: (-x.height, -x.weight, x.number))

for s in students:
    print(s.height, s.weight, s.number)