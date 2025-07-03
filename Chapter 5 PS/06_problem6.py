# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter your name : ")
language = input("Enter your language : ")
d.update({name : language})

name = input("Enter your name : ")
language = input("Enter your language : ")
d.update({name : language})

name = input("Enter your name : ")
language = input("Enter your language : ")
d.update({name : language})

name = input("Enter your name : ")
language = input("Enter your language : ")
d.update({name : language})

print(d)


# Enter your name : Rutu
# Enter your language : python
# Enter your name : neha
# Enter your language : java
# Enter your name : rina
# Enter your language : js
# Enter your name : tiya
# Enter your language : c
# {'Rutu': 'python', 'neha': 'java', 'rina': 'js', 'tiya': 'c'}