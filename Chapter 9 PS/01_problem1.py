#Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinklel


#first open the file
f = open("poem.txt")
content = f.read()

if "twinkle" in content:
    print("The word Twinkle is present in the content..")

else:
    print("The word Twinkle is not present in the content..")

f.close()