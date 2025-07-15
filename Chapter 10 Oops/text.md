#  1. Class and Object
```
Class is a blueprint for creating objects.

Object is an instance of a class.
```
# 2. Encapsulation
```
“Encapsulation means hiding the internal details of an object and only showing what is necessary through methods.
```
```
Encapsulation = Data hiding + Access control through methods
```

# 3. Abstraction
```
Abstraction is the process of hiding the internal implementation details of a class or function and showing only the essential features to the user.

It allows you to focus on what an object does, rather than how it does it.
```

# 4. Inheritance
```
One class (child) can inherit the properties and methods of another (parent).
```
```
Inheritance is an object-oriented programming principle that allows a class (child class or subclass) to acquire the properties and behaviors (methods and variables) of another class (parent class or superclass).

It enables code reusability, extensibility, and hierarchical relationships between classes.
```

# 5. Polymorphism
```
Polymorphism = Same method name, different behavior based on the object.(behave differently)
```



# MODELLING A PROBLEM IN OOPS
We identify the following in our problem.
```
Noun Class → Employee

Adjective + Attributes name, age, salary

Verbs + Methods + getSalary(), increment()
```

# Class Attribute
```
A class attribute is a variable that belongs to the class itself, and is shared by all objects created from that class.
```

# INSTANCE ATTRIBUTES
An attribute that belongs to the Instance (object). Assuming the class from the previous
```
example:
harry.name = "harry"
harry.salary = "30k" # Adding instance attribute
```
```
Note: Instance attributes, take preference over class attributes during assignment & retrieval.

When looking up for harry.attribute it checks for the following:

1) Is attributes present in object?
2) Is attributes present in class?
```


# SELF PARAMETER
```
self refers to the instance of the class. It is automatically passed with a function call from an object.
```

#  @staticmethod
```
    Does not receive the self or cls parameter.
```

# _INIT__() CONSTRUCTOR
```
_init() is a special method which is first run as soon as the object is created.

_init() method is also known as constructor.

It takes self-argument and can also take further arguments
```