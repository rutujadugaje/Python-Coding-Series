
# Accessing elements by indexing(starting from 0)
my_tuple = ('a', 'b', 'c', 'd', 'e')
print(my_tuple[0])  # Output: 'a'
print(my_tuple[2])  # Output: 'c'

#negative indexing
print(my_tuple[-1])  # Output: 'e'

# Slicing tuples
print(my_tuple[1:4])    # Output: ('b', 'c', 'd')
print(my_tuple[:3])    # Output: ('a', 'b', 'c') 0 to 2
print(my_tuple[2:])    # Output: ('c', 'd', 'e') 2 to end
print(my_tuple[-3:])   # Output: ('c', 'd', 'e') -3 to end



# t = (1, 2, 3, 4, 5)
# t[0] = 100  # This will raise a TypeError because tuples are immutable


my_tuple2 = ('apple', 'banana', 'cherry')

for item in my_tuple2:
    print(item)             # apple
                            # banana
                            # cherry

# Tuple methods
t = (1, 2, 3, 1, 4, 1)
print(len(t))   # Length of the tuple    #6
print(t.count(1))   # How many times 2 appears    #3
print(t.index(3))   #2 # Find the index of the first occurrence of 3
print(5 in t)   #False # Check if 5 is in the tuple
print(4 in t)   #True # Check if 4 is in the tuple
print(sorted(t))    # Sorted tuple: [1, 1, 1, 2, 3, 4] (returns a list)



a = (1, 45, 342, 3424, False, 45,"Amit","Rishi")
print(a)

no = a.count(45)
print(f"The number 45 appears {no} times in the tuple.")  # Output: The number 45 appears 2 times in the tuple.



# Concatenation and repetition Membership
t1 = (1, "rutu", 3)
t2 = (4, 5, 6)
t3 = t1 + t2    # Concatenation of tuples
print(t3)       # Output: (1, 'rutu', 3, 4, 5, 6)


# repetition
repeated = t1 * 3  # Repeating the tuple 3 times
print(repeated)


# Membership
print(5 in t1)   #False # Check if 5 is in the tuple
print(3 in t1)   #True # Check if 3 is in the tuple


# min and max in the tuple 
t4 = (10, 20, 30, 40, 50)
print(min(t4))  # Output: 10 (minimum value in the tuple)
print(max(t4))  # Output: 50 (maximum value in the tuple)

# unpacking
t5 = (1, 2, 3)
a, b, c = t5  # Unpacking the tuple into variables
print(a, b, c)  # Output: 1 2 3