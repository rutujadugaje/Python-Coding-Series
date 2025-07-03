friends = ["Apple", "Banana", 5 , 55.4, False, "Akash"]
print(friends[0])   # Apple Accessing the first element of the list

friends[0] = "Mango"    # Changing the first element of the list
print(friends[0])


# List are mutable, meaning we can change their content
# String are immutable, meaning we cannot change their content

print(friends[1:4]) #['Banana', 5, 55.4] # Slicing the list from index 1 to 3 (4 is not included)