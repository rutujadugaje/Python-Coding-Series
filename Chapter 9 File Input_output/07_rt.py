f = open("myfile.txt", "rt")  # same as open("myfile.txt", "r")
data = f.read()
print(data)
f.close()


'''
Reads file as text (i.e., a string).

Default mode if you just use "r".

Suitable for files with readable characters, like .txt.


'''