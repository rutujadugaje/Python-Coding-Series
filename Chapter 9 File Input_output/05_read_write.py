f = open("myfile.txt", "r+")
print(f.read())
f.seek(0)
f.write("nikal jao\n")
f.close()



'''
r+ is useful when you want to update part of an existing file.

Use seek() to control where in the file you read or write.

Be cautious: it will overwrite characters without clearing the file.
'''