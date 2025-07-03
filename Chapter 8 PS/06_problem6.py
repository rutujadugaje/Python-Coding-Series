# Write a python function which converts inches to cms.

def inch_to_cm(inch):
    return inch * 2.54

n = int(input("Enter a number : "))
print(f"The corresponding value in {n} is : {inch_to_cm(n)}")