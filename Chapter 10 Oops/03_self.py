class Employee:
    language = "Python"
    salary = 1400000
        
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")

reva = Employee()
reva.language = "Javascript"

reva.greet()
reva.getInfo()        #Or
# Employee.getInfo(reva)
