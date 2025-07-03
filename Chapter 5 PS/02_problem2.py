#Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set()

n = input("Enter a number 1: ")
s.add(int(n))
n = input("Enter a number 2: ")
s.add(int(n))
n = input("Enter a number 3: ")
s.add(int(n))
n = input("Enter a number 4: ")
s.add(int(n))
n = input("Enter a number 5: ")
s.add(int(n))
n = input("Enter a number 6: ")
s.add(int(n))
n = input("Enter a number 7: ")
s.add(int(n))
n = input("Enter a number 8: ")
s.add(int(n))

print(s)

#Enter a number 1: 3
# Enter a number 2: 2
# Enter a number 3: 3
# Enter a number 4: 2
# Enter a number 5: 5
# Enter a number 6: 6
# Enter a number 7: 5
# Enter a number 8: 1
# {1, 2, 3, 5, 6}