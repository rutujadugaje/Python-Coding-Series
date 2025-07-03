# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter username : ")

if len(username)==0:
    print("You didn't enter any username")

elif(len(username)<10):
    print("the username contain less than 10 charecters")

else:
    print("the username has 10 or more characters")