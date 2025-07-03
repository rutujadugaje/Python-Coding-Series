'''
2. Write a python program using function to convert Celsius to Fahrenheit

formula =      c/5 = (f-32)/9
'''



# Celsius to Fahrenheit

def c_to_f(c):
    return (c * 9/5) + 32

c = float(input("Enter the temperature in celcius :"))
print(f" Celsius to Fahrenheit : {c_to_f(c)} °F")





# Fahrenheit to celsius
'''
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in Fahrenheit : "))
print(f"temperature is = {round(f_to_c(f), 2)} °C")

'''


















