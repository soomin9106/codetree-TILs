class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

students = []

for _ in range(5):
    name, height, weight = map(str, input().split())
    students.append(Student(name, int(height), float(weight)))

students_name = sorted(students, key = lambda x: x.name)
print("name")

for s in students_name:
    print(s.name, s.height, s.weight)

students_height = sorted(students, key = lambda x: -x.height)
print()
print("height")

for s in students_height:
    print(s.name, s.height, s.weight)