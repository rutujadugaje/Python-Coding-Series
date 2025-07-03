friends = ["Aple", "Banana", 5, 55.4, False, "Akash"]
print(friends)  #['Aple', 'Banana', 5, 55.4, False, 'Akash']

friends.append("Harry") # Adding an element to the end of the list
print(friends)  #['Aple', 'Banana', 5, 55.4, False, 'Akash', 'Harry']



l1 = [1, 32, 54, 45, 67, 65,21, 12, 4]
# l1.sort()   #[1, 4, 12, 21, 32, 45, 54, 65, 67] # Sorting the list in ascending order
# print(l1)

# l1.reverse()    #[4, 12, 21, 65, 67, 45, 54, 32, 1] # Reversing the list
# print(l1)

# l1.insert(2, 100)   #[1, 32, 100, 54, 45, 67, 65, 21, 12, 4] # Inserting an element at index 2
# print(l1)

# value = (l1.pop(3))    #45 # Removing and returning the element at index 3
# print(value)         #45
# print(l1)           #[1, 32, 54, 67, 65, 21, 12, 4] # The element at index 3 is removed


l1.remove(67)   #[1, 32, 54, 45, 65, 21, 12, 4] # Removing the first occurrence of the element 67
print(l1)