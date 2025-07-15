# Create a class with a class attribute a; create an object from it and set 'a' directly using object.a=0. Does this change the class attribute?


class Demo:     
    a = 4           #class Atrribute

obj = Demo()        # Create an object of Demo
print(obj.a)        #print 4 . Prints the class attribute becasuse instance attribute is not present
obj.a = 0           #create a new "instance/object attribute"
print(obj.a)        #print 0. #prints the instance attribute because instance attribute is present
print(Demo.a)       #prints 4. prints the class attribute