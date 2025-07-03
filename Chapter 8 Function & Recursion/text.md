# Function
```
A function is a group of statements performing a specific task.
```

```
When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!
```
```
A function can be reused by the programmer in a given program any number of
```

***syntax of a function***
```
def fun():
    print("Hello")

This function can be called any number of times, anywhere in the program
```


# Function call
Whenever we want to call a function, we put the name of the function followed by parentheses as follows
```
func1() 
```
This is called function call.

# FUNCTION DEFINITION
```
The part containing the exact set of instructions which are executed during the function call.
```

Quick Quiz: Write a program to greet a user with "Good day" using functions.

# TYPES OF FUNCTIONS IN PYTHON
There are two types of functions in python:
```
1. Built in functions (Already present in python)

2. User defined functions (Defined by the user)
```
Examples of built in functions includes len(), print(), range() etc.

***The func1() function we defined is an example of user defined function.***

# FUNCTIONS WITH ARGUMENTS
```
A function can accept some value it can work with.

We can put these values in the parentheses.

A function can also return value as shown below:
```
```
def goodDay(name, ending):
    print(" Have a Good Day!" + name)
    print(ending)
    return "done"

abc = goodDay("Harry", "Thankyou")
print(abc)

```
in above code,
***"Harry" is the argument passed to the name parameter.***

***"Thankyou" is the argument passed to the ending parameter.***
```
Function name: goodDay

Parameters: name, ending

Arguments (at call site): "Harry", "Thankyou"
```

# return
return: function tu ek value lekar jaa aur jo bhi variable mange usko de dena


# DEFAULT PARMETER VALUE
```
We can have a value as default as default argument in a function.


def goodDay(name="Harry"):
    print("Good Day!!", name)

goodDay()

If we specify name = "Harry" in the line containing def, this value is used when no argument is passed.
```

# RECURSION
```
Recursion is a function which calls itself.
It is used to directly use a mathematical formula as function.
```