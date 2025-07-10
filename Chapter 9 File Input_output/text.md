# File Input/Output
```
The random-access memory is volatile, and all its contents are lost once a program terminates in order to persist the data forever, we use files.

A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.
```
```
RAM = Volatile / temporarily program load here
HDD = Non Volatile /slow memory
```


# TYPE OF FILES.
There are 2 types of files:

***1. Text files (.txt, .c etc)***

***2. Binary files (.jpg, .dat, etc)***

Python has a lot of functions for reading, updating, and deleting files.

# OPENING A FILE
```
Python has an open () function for opening files. It takes 2 parameters: filename and made.
```
```
#open("filename", "mode of opening(read mode)")
open("this.txt", "r")
```

# MODES OF OPENING A FILE
```
r-open for reading

w-bpen for writing

a- open for appending

+- open for updating.

'rb' will open for read in binary mode.

'rt' will open for read in text mode.
```

# WRITE FILES IN PYTHON
```
In order to write to a file, we first open it in write or append mode after which, we use the python's f.write() method to write to the file!
```