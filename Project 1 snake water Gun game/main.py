import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])    # Computer's random choice
youstr = input("Enter your Choice: ")   # Get user input
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake🐍", -1: "Water💧", 0: "Gun🔫"}

# Input validation
if youstr not in youDict:
    print("Invalid input! Please choose 's' for Snake, 'w' for Water, 'g' for Gun.")
    exit()

# Convert input
you = youDict[youstr]

# Show choices
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


# Game logic
if computer == you:
    print("It's a draw")

else:
    if(computer==1 and you==-1):
        print("You lose")

    elif(computer==1 and you==0):
        print("You Win")

    elif(computer==-1 and you==1):
        print("You Win")

    elif(computer==-1 and you==0):
        print("You lose")

    elif(computer==0 and you==1):
        print("You lose")

    elif(computer==0 and you==-1):
        print("You Win")

    else:
        print("Something went wrong..")