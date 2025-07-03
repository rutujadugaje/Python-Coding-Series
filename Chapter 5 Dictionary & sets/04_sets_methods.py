s = {1, 4, 3, 5, 2,2, 1, "Harry"}
print(s, type(s))   #{1, 2, 3, 4, 5, 'Harry'} <class 'set'>

s.add(566)
print(s, type(s))   #{1, 2, 3, 4, 5, 566, 'Harry'} <class 'set'>
    #Adds a single element to the set.

s.update([358, 4567])
print(s)    #{1, 2, 3, 4, 5, 'Harry', 4567, 358, 566}
    #Adds multiple elements (from iterable) to the set.

s.remove(5)
print(s)    #{1, 2, 3, 4, 4567, 358, 'Harry', 566}
    #Removes a specific element; raises error if element not found.

s.discard(10)
print(s)    #{1, 2, 3, 4, 4567, 358, 'Harry', 566}
    #Removes a specific element; does NOT raise error if not found.

elem = s.pop()
print(elem) #1
    #Removes and returns a random element.

s.clear()
print(s)    #set()
    #Removes all elements from the set.


a = {1, 2}
b = {2, 4}
print(a.union(b))   #{1, 2, 4}
print(a | b)        #{1, 2, 4} same result
    #Returns a new set with elements from both sets.


print(a.intersection(b))    #{2}
print(a & b)    #{2} same result
    #Returns a new set with only common elements.

print(a.difference(b))  #{1}
print(a - b)        #{1}
    #Returns elements in the first set but not in the second.

print(a.issubset(b))    #False
    #True if all elements of a are in b.

print(a.issuperset(b))  #False
    #True if a contains all elements of b.