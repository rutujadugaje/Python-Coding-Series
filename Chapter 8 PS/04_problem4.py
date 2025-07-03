# Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + 4.... (n-1) + n
sum(n) = sum(n-1) + n
'''

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# n = int(input("Enter a number: "))
# print(f"The sum of first {n} natural numbers is : {sum(n)}")
   





#The sum of first n natural numbers
def recursive_sum(n):
    if n<=0:
        return None
    elif n==1:
        return 1
    else:
        return recursive_sum(n-1) + n
    
n = int(input("Enter a number : "))
result = recursive_sum(n)

if result is None:
    print("Enter valid natural number(Greater than 0)")

else:
    print(f"The sum of first natural {n} numbers is : {result}")