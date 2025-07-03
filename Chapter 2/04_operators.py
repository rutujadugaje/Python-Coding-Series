# Arithmetic operator 
a = 4
b = 5
c = a + b
print(c)

# Assingment operator
a = 7-8
print(a)
b = 6
# b += 8  # increment the value of b by 8 and then assign it back to b
b -= 2    # decrement the value of b by 9 and then assign it back to b
print(b)

# Comparison operator
a = 5
b = 6
print(a == b)  # equal to
print(a != b)  # not equal to
print(a > b)   # greater than
print(a < b)   # less than
print(a >= b)  # greater than or equal to
print(a <= b)  # less than or equal to

# Logical operator
a = True
b = False
print(a and b)  # logical AND
print(a or b)   # logical OR
print(not(True))  # logical NOT


# Identity operator
# a = [1, 2, 3]
# b = a
# print("identity operator", a is b)  # checks if both variables point to the same object
# print(a is not b)  # checks if both variables do not point to the same object


# Membership operator
# a = [1, 2, 3, 4, 5]
# print(1 in a)  # checks if 1 is in the list a
# print(6 not in a)  # checks if 6 is not in the list a


# Bitwise operator
a = 5  # 0101 in binary
b = 3  # 0011 in binary
print("Bitwise And operator",a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)  # Bitwise NOT
print(a << 1)  # Bitwise left shift
print(a >> 1)  # Bitwise right shift


# Ternary operator
a = 5
b = 10
c = a if a > b else b  # if a is greater than b, c will be a, otherwise c will be b
print(c)  # prints 10 since 10 is greater than 5


# # Operator precedence
# a = 5
# b = 10
# c = 15
# d = a + b * c  # multiplication has higher precedence than addition
# print(d)  # prints 5 + (10 * 15) = 5 + 150 = 155


# # Chained operators
# a = 5
# b = 10
# c = 15
# d = 20
# result = a < b < c < d  # checks if a is less than b, b is less than c, and c is less than d
# print(result)  # prints True since 5 < 10 < 15 < 20 is True


# # Augmented assignment operators
# a = 5
# b = 10
# a += b  # equivalent to a = a + b
# print(a)  # prints 15
# b -= 3  # equivalent to b = b - 3
# print(b)  # prints 7


# # Floor division operator
# a = 10
# b = 3
# print(a // b)  # prints 3, which is the floor division of 10 by 3


# # Exponentiation operator
# a = 2
# b = 3
# print(a ** b)  # prints 8, which is 2 raised to the power of 3
