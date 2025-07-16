class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = Number(1)
m = Number(2)

print(n + m)        #addition of two objects/Instance of a Number class...thats why __add__ method used here