# Write a program to find whether a given number is prime or not.
# prime number : the number which is divisible either by itself or 1.


n = int(input("Enter a number: "))
if(n<=1):
    print("Number is not prime")
else:
    for i in range(2, n):
        if(n%i)==0:
            print("Number is not prime")
        break
    else:
        print("Number is prime")
    