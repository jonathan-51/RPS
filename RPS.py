import random

Rock = "r"
Paper = "p"
Scissors = "s"

options = [Rock,Paper,Scissors]
comp_choice = random.choice(options)
print(comp_choice)
user_choice = input("Enter Your Choice (R for Rock, P for Paper, S for Scissors: ").lower()
print(user_choice)


if user_choice == comp_choice: #Same Combination
    print("Tie. Please Try Again")
elif user_choice == Rock and comp_choice == Paper: #Rock vs Paper
    print("You Lose. Please Try Again")
elif user_choice == Rock and comp_choice == Scissors: #Rock vs Scissors
    print("You Win. Good Job!")
elif user_choice == Paper and comp_choice == Rock: #Paper vs Rock
    print("You Win. Good Job!")
elif user_choice == Paper and comp_choice == Scissors: #Paper vs Scissors
    print("You Lose. Please Try Again")
elif user_choice == Scissors and comp_choice == Rock: #Scissors vs Rock
    print("You Lose. Please Try Again")
elif user_choice == Scissors and comp_choice == Paper: #Scissors vs Paper
    print("You Win. Good Job!")
