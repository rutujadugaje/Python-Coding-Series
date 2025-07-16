class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)

ab = Programmer()
print(ab.a, ab.b)

o = Manager()
print(o.a, o.b, o.c, ab.a)