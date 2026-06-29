import random
print("ROCK, Paper, sescissor Game")
options = ["rock","paper","scissor"]
user = input("enter your choice: ").lower()
computer = random.choice(options)
print("computer: ",computer)

# tie case
if user == computer:
    print("it is tie")

# your win cases
elif user == "rock" and computer == "scissor":
    print("you win")
elif user == "paper" and computer == "rock":
    print("you win")
elif user == "scissor" and computer == "paper":
    print("you win")

# computer win cases
elif user == "scissor" and computer == "rock":
    print("computer wins")
elif user == "rock" and computer == "paper":
    print("computer wins")
elif user == "paper" and computer == "scissor":
    print("computer wins")



# invalid user
else:
    print("invalid choice")