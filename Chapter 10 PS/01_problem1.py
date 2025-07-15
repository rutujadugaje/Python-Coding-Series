# 1. Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Rutuja",30000,422209)
print(p.name, p.salary, p.pin)

r = Programmer("Risha",10000,422001)
print(r.name, r.salary, r.pin)

