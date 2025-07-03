# Write a python program to print  the contents of a directory using the os module. Search online for the function  which does that.

import os

# To list contents of the current directory, you can use os.getcwd()
# os.getcwd() stands for Get Current Working Directory.
directory_path = '/Code_With_Harry_MERN_Series'

try:
    # Get the list of all files and directories
    entries = os.listdir(directory_path)

    print(f"Contents of the directory '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")


# *****************OR******************** 
# import os
# directory_path = '/Code_With_Harry_MERN_Series'
# entries = os.listdir(directory_path)
# for item in entries:
#     print(item)
