#Rock-Paper-Scissors
import random
player_choice=0
choices=["rock","paper", "scissors"]
while player_choice!="exit":
    player_choice=input("Enter rock, paper or scissors(or exit):  ").lower()
    comp_choice=random.choice(choices)
    print("Computer choice is: ",comp_choice)
    if player_choice=="exit":
        print("Thanks for playing")
        break
    if player_choice not in choices:
        print("Invalid choice, please play again")
    if player_choice==comp_choice:
        print("It's a tie!!!")
    elif (player_choice=="rock" and comp_choice=="scissors") or (player_choice=="scissors" and comp_choice=="paper") or (player_choice=="paper" and comp_choice=="rock"):
        print("You Win!!!")
    else:
        print("Computer Wins!!!")

    
    

