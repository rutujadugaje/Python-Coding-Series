f = open("myfile.txt", "rb")
data = f.read()
print(data)
f.close()



'''
Reads file as binary data (bytes), not a string.

Useful when reading non-text files, or if you want raw data.

You’ll get output like:

O/P: 
b'Hey!! Harry you are amazing'
'''