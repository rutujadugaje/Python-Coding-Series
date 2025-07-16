class Employee:
    company = "ANC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# Instead of doing this
#          |
# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")



class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)