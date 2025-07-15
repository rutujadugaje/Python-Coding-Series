# 4. Add a static method in problem 2, to greet the user with hello.


# Write a class "calculator" capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.n = n

    def sqaure(self):
        print(f"THe square is: {self.n*self.n}")

    def cube(self):
        print(f"THe cube is: {self.n*self.n*self.n}")

    def sqaureroot(self):
        print(f"THe squareroot is: {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello there")
obj = Calculator(4)
obj.hello()
obj.sqaure()
obj.cube()
obj.sqaureroot()