# Define a class named 'Employee'
class Employee:
    # Class variables (shared by all instances of the class)
    name = "Harry"  #class attribute
    language = "Py"
    salary = "1200000"

# Create an object/instance of the Employee class
harry = Employee()
harry.name = "Harry"    #object/instance attribute
print(harry.name, harry.language, harry.salary)  # Output: Harry Py

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
# rohan.salary = 150000
print(rohan.name,rohan.salary, rohan.language)  # Output: Harry Py


# Here name is object attribute.. and salary and language are class attributes as they directly belongs to the class