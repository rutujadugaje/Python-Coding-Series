# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

messange = input("Enter message here : ")

if((spam1 in messange) or (spam2 in messange) or (spam3 in messange) or (spam4 in messange)):
    print("Spam msg detected")

else:
    print("This is not spam")