class Employee:
    language = "Python"
    salary = 1400000
        
    def __init__(self, name, salary, language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")

reva = Employee("Reva", 1300000, "Javascript")
# reva.name = "Reva"
print(reva.name, reva.salary)


# reva.greet()
# reva.getInfo()        











'''
#init Example code




class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def display(self):
    print(f"Name: {self.name}, Age: {self.age}")

p1 = person("Rutuja", 23)
p1.display()
'''