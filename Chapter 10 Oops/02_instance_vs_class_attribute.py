class Employee:
    language = "Python"
    salary = 1400000


reva = Employee()
reva.language = "Javascript"
print(reva.language, reva.salary)

# OP 
# Javascript 1400000

# Here, first check the instance attribute is present or not, if yes then print instance attribute , otherwise prints class attributes