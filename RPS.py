import random

try_again = 0
try_again_track = 0  

while try_again == try_again_track:
    Rock = "r"
    Paper = "p"
    Scissors = "s"

    options = [Rock,Paper,Scissors]
    comp_choice = random.choice(options)
    comp_win_left = 2
    user_win_left = 2
    comp_score = 0
    user_score = 0

    try_again = 0
    try_again_track = 0    
    print("Play a best of 3 against the Computer.")
    while comp_win_left and user_win_left > 0:

        comp_choice = random.choice(options)
        print(comp_choice)
        print(f"comp_score = {comp_score}")
        print(f"user_score = {user_score}")
        print(f"comp_win_left = {comp_win_left}")
        print(f"user_win_left = {user_win_left}")
        user_choice = input("Please Enter Your Choice (R for Rock, P for Paper, S for Scissors: ").lower()
        
        if user_choice == comp_choice: #Same Combination
            print(f"Tie. Please Try Again.\nYou - {user_score}.\nComputer - {comp_score}.\n")
        elif user_choice == Rock and comp_choice == Paper: #Rock vs Paper
            comp_win_left += - 1
            comp_score += 1
            print(f"Round 1 goes to Computer.\nYou - {user_score}.\nComputer - {comp_score}.\n")
        elif user_choice == Rock and comp_choice == Scissors: #Rock vs Scissors
            user_win_left += - 1
            user_score += 1
            print(f"Round 1 goes to You. One more to go!\nYou - {user_score}.\nComputer - {comp_score}.\n")
        elif user_choice == Paper and comp_choice == Rock: #Paper vs Rock
            user_win_left += - 1
            user_score += 1
            print(f"Round 1 goes to You. One more to go!\nYou - {user_score}.\nComputer - {comp_score}.\n")
        elif user_choice == Paper and comp_choice == Scissors: #Paper vs Scissors
            comp_win_left += - 1
            comp_score += 1
            print(f"Round 1 goes to Computer.\nYou - {user_score}.\nComputer - {comp_score}.\n")
        elif user_choice == Scissors and comp_choice == Rock: #Scissors vs Rock
            comp_win_left += - 1
            comp_score += 1
            print(f"Round 1 goes to Computer.\nYou - {user_score}.\nComputer - {comp_score}.\n")
        elif user_choice == Scissors and comp_choice == Paper: #Scissors vs Paper
            user_win_left += - 1
            user_score += 1
            print(f"Round 1 goes to You. One more to go!\nYou - {user_score}.\nComputer - {comp_score}.\n")

    if comp_score == 2:
        print("You Lost. Please Try Again!")
        try_again_response = input("Would you like to play again? (Y/N)").lower()
        if try_again_response == "n":
            try_again_track += 1

    else:
        print("You Won!")
        try_again_response = input("Would you like to play again? (Y/N)").lower()
        if try_again_response == "n":
            try_again_track += 1

print("\nThank you for playing.")