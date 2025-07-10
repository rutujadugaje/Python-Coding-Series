st = "Hey!! Harry you are amazing"

f = open("myfile.txt", "a")

f.write(st)

f.close()

'''
"a" stands for append mode.

If the file doesn’t exist, it will be created.

If the file already exists, the content will be added at the end of the file (without removing existing content).
'''


'''
If you want to add the new content on a new line, you should do:

python
Copy code
f.write("\n" + st)
'''