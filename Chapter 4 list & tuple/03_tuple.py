a = (1,2,3,4,5)
print(type(a))  #<class 'tuple'> 

# Tuples are immutable
# a[0] = 10  # This will raise a TypeError and it is unorderd 
# Tuples can contain mixed data types


t1 = ()
print(type(t1))  # <class 'tuple'>

t2 = (10,)
print(type(t2))  # <class 'tuple'>

t3 = (10, 20, 30)
print(type(t3))  # <class 'tuple'>

t4 = ("apple", 3.14, True)
print(type(t4))  # <class 'tuple'>

t5 = 1, 2, 3
print(type(t5)) # <class 'tuple'> tuple without parenthesis