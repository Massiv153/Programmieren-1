import random
user_action=input("Enter a choice (rock, paper, scissors): ")
possible_action=["rock","paper","scissors"]
computer_action=random.choice(possible_action)
print("You chose "+user_action+", computer chose "+computer_action)
if user_action=="rock":
    if computer_action=="rock":
        print("Its a tie")
    elif computer_action=="paper":
        print("You lose")
    else:
        print("You win")
elif user_action=="paper":
    if computer_action=="paper":
        print("Its a tie")
    elif computer_action=="scissors":
        print("You lose")
    else:
        print("You win")
else:
    if computer_action=="scissors":
        print("Its a tie")
    elif computer_action=="rock":
        print("You lose")
    else:
        print("You win")
        