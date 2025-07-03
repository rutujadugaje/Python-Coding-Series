# string is immutable in python , it cannot be changed

a = 'harry'         #Single Quoted string
a = "harry"         #double Quoted string
a = '''harry'''     #triple Quoted string


# String Slicing

a = 'harry'
name = a[0:4]   #slicing the string from index 0 to 3
print(name)

name = a[:4 ]   #slicing the string from index 0 to 3 , [0:4]
print(name)
name = a[2:]    #slicing the string from index 2 to end, [2:4], black means length
print(name)


