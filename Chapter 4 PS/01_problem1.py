#write a program to store the names of seven fruits in a list entered by the user.

fruits = []
for i in range(7):
    fruit = input(f"Enter the fruit name {i+1}: ")
    fruits.append(fruit)
print("Fruits List: ",fruits)







