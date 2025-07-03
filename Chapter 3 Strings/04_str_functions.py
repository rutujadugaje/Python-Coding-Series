#string Functions

name = "Harry"

print(len(name))
print(name.endswith("rry"))     #True
print(name.startswith("Har"))     #True
print(name.startswith("har"))     #False case-sensitive
print(name.capitalize())            #Harry.. it capitalized only one starting letter in the string

print(name.lower())              #harry
print(name.upper())              #HARRY

word = "  Hello world  "
print(word.title())              #H Hello World ..it capitalized the first letter of each word
print(word.swapcase())              #hELLO WORLD ..Swaps lowercase to uppercase and vice versa

print(word.find("w"))          #8 ..finds the index of the first occurrence of the substring
print(word.rfind("d"))         #12 ..finds the index of the last occurrence of the substring
print(word.replace("world", "Python"))  #  Hello Python  ..replaces the first occurrence of the substring with another substring
print(word.strip())             #Hello world ..removes leading and trailing whitespace
print(word.index("w"))          #8 ..finds the index of the first occurrence of the substring, raises ValueError if not found
# print(word.index("x"))          #Raises ValueError if not found
print(word.count("o"))        #2 ..counts the number of occurrences of the substring
print(word.split())         #['Hello', 'world'] ..splits the string into a list of substrings based on whitespace
