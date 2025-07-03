a = int(input("Enter your age: "))

if(a%2==0):
    print("The Age is even")

if(a>=18):
    print("You are illigible for voting👍")

elif(a<0):
    print("Do not Enter negative age🤬")

elif(a==0):
    print("So Sorry, 0 cannot be age😞")

else:
    print("You are not illigible for voting👎😠")
