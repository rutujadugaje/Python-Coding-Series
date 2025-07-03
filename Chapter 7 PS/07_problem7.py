# Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3

'''
#1] For n = 3

   *
  ***
 *****

'''

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print()



'''
-----------------------------------------------------------------
2]
*
***
*****
*******
*********
'''

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print("*" * (2*i-1), end="")
#     print("")


''' 
-----------------------------------------------------------------
3] Write a program to print the following star pattern:
*
**
***
for n = 3
'''

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print("*" * i, end="")
#     print("")


'''
-----------------------------------------------------------------
4] Write a program to print the following star pattern.

***
* *       for n = 3
***
'''

# n = int(input("Enter a number: "))

# for i in range(n):
#    for j in range(n):
#       if i == 0 or i == n-1 or j == 0 or j == n-1:
#          print("*", end="")
#       else:
#          print(" ", end="")
#    print()


'''
----------------------------------------------------------------- 
5] Write a program to print the following star pattern.

*****
*   *       for n = 5
*   *       
*   *       
*****
'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print()




'''
-----------------------------------------------------------------
*****
****
***
**
*
'''

# rows = 5
# for i in range(rows, 0, -1):
#     print("*" * i)
    

'''
-----------------------------------------------------------------
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

# n = int(input("Enter the number :"))

# for i in range(1, n+1):
#     print(" " * (n-i), "*" * (2*i-1) , end=(""))
#     print("")

# for i in range(n-1 , 0 ,-1):
#     print(" " * (n-i), "*" *(2*i -1))


'''
-----------------------------------------------------------------
     *********
      *******
       *****
        ***
         *
        ***
       *****
      *******
     *********
'''

# n = int(input("Enter the number : "))

# for i in range(n, 0, -1):
#     print(" "*(n-i), "*"*(2*i-1), end="")
#     print("")
# for i in range(2, n+1):
#     print(" "*(n-i), "*"*(2*i-1))
    

'''
-----------------------------------------------------------------

'''