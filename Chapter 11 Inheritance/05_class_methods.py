# class Employee:
#     a = 1
#     def show(self):
#         print(f"The class value of 'a' is {self.a}")

# e = Employee()
# e.a = 45

# e.show()    #The class value of 'a' is 45.. It shows instance attribute



class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of 'a' is {cls.a}")

e = Employee()
e.a = 45

e.show()    #using @classmethod , the output become 1..The class value of 'a' is 1