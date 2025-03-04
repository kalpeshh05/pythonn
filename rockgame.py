import random

choices = ["stone", "paper", "scissor"]

user= input("Enter your choice (stone, paper, scissor): ")

com_choice = random.choice(choices)

print(f"Computer choice: {com_choice}")

if user == com_choice:
    print("It's a tie!")
elif (user == "stone" and com_choice == "scissor") or \
     (user == "paper" and com_choice == "stone") or \
     (user == "scissor" and com_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")