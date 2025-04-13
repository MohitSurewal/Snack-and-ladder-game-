import random 

computer = random.choice([1, -1, 0])
youstr =input("Enter your Choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You Choose {reverseDict[you]} and Computer choose {reverseDict[computer]}")

if (computer == you ):
    print("Its a Draw")

if ((computer - you == -1 and computer - you == 2 )):
    print("You Lose!!")

else:
    print("You Win!")

