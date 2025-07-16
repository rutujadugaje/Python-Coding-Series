# INHERITANCE & MORE ON OOPS
```
Inheritance is a way of creating a new class from an existing class.
```
Syntax:
```
class Employee: # Base class
# Code

class Programmer (Employee): # Derived or child class
# Code
```
We can use the method and attributes of 'Employee' in 'Programmer' object.

Also, we can overwrite or add new attributes and methods in 'Programmer' class.

# TYPES OF INHERITANCE
Single inheritance

Multiple inheritance

Multilevel inheritance

# SINGLE INHERITANCE
```
Single inheritance occurs when child class inherits only a single parent class.

from Base class , a simple derived class is made
```
```
Parent--to--child
```

# MULITPLE INHERITANCE
```
Multiple Inheritance occurs when the child class inherits from more than one parent classes
```
```
Multiple Parents---to---child
```

# MULTILEVEL INHERITANCE
```
When a child class becomes a parent for another child class
```
```
parent ---child 1 --- chaild2
```


# Super
```
```

# CLASS METHOD
```
A class method is a method which is bound to the class and not the object of the class.

@classmethod decorator is used to create a class method.

It receives the class itself as the first argument (cls), not the instance (self).

You can use it to access or modify class variables shared by all instances.
```

```
Employee.a = 1 is a class variable.

Even if you do e.a = 45, you're creating a new instance variable that hides the class variable.

So, when you call e.show(), it uses the class variable, not the instance one, and prints 1.
```

# PROPERTY DECORATORS
```
@property makes a method behave like an attribute.

You can access e.name without calling it like a function (e.name instead of e.name()).

It’s useful for creating computed attributes.
```

# @<property>.setter
```
A @property.setter lets you define how to set a value to the property.

You don't call it directly — it’s triggered automatically when you assign a value to the property.
```
# OPERATOR OVERLOADING IN PYTHON
```
Operators in Python can be overloaded using dunder methods.

These methods are called when a given operator is used on the objects.

Operators in Python can be overloaded using the following methods:

p1+p2       # p1.__add__(p2)
p1-p2       # p1.__sub__(p2)
p1*p2       # p1.__mul__(p2)
p1/p2       # p1.__truediv__(p2)
p1//p2      # p1.__floordiv__(p2)
```
Other dunder/magic methods in Python:
```
__str__()       #used to set what gets displayed upon calling str(obj)
__len__()       #used to set what gets displayed upon calling.__len__() or len(obj)
```