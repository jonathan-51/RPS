import random

Rock = "r"
Paper = "p"
Scissors = "s"
options = [Rock,Paper,Scissors]

def IsOdd(n): #Checks if number is odd or even
    return n % 2 == 0

while True: #Loops the Game
    best_of = input("Choose a format: best of 3, best of 5, best of 7....")
    num_rounds = 0 #Tracks the number of rounds (Excluding ties)
    comp_score = 0 #Tracks the score
    user_score = 0 #Tracks the score

    while True: #filters out all possible responses except for odd numbers
        try: #Converts input into an integer
            best_of = int(best_of)
        except:
            best_of = input("Encountered an error.\nPlease enter an odd number: ")

        if type(best_of) == int and IsOdd(best_of) == False: #Filters out the odd numbers
            break
        else: #filters out everything else like strings and even numbers
            best_of = input("Encountered an error.\nPlease enter an odd number: ")

    num_win_req = (best_of + 1)/2 #number of wins to win the game    
    while user_score < num_win_req and comp_score < num_win_req: #loops the rounds
        comp_choice = random.choice(options)
        print(comp_choice)
        #print(f"comp_score = {comp_score}")
        #print(f"user_score = {user_score}")
        #print(f"comp_win_left = {comp_win_left}")
        #print(f"user_win_left = {user_win_left}")
        user_choice = input("Please Enter Your Choice (R for Rock, P for Paper, S for Scissors: ").lower()

        while True: #Checks to see if player entered a valid choice (r/p/s)
            if user_choice != "r" and user_choice != "p" and user_choice != "s":
                user_choice = input("Please try again. Enter (r/p/s): ").lower()
            else:
                break

        if user_choice == Rock and comp_choice == Paper: #Rock vs Paper
            comp_score += 1 #Updates score
            num_rounds += 1 #updates number of rounds effective rounds played
            print(f"Round {num_rounds} goes to Computer.\nYou: {user_score}\nComputer: {comp_score}\n")

        elif user_choice == Rock and comp_choice == Scissors: #Rock vs Scissors
            user_score += 1 #Updates score
            num_rounds += 1
            print(f"Round {num_rounds} goes to You.\nYou: {user_score}\nComputer: {comp_score}\n")

        elif user_choice == Paper and comp_choice == Rock: #Paper vs Rock
            user_score += 1 #Updates score
            num_rounds += 1
            print(f"Round {num_rounds} goes to You.\nYou: {user_score}\nComputer: {comp_score}\n")

        elif user_choice == Paper and comp_choice == Scissors: #Paper vs Scissors
            comp_score += 1 #Updates score
            num_rounds += 1
            print(f"Round {num_rounds} goes to Computer.\nYou: {user_score}\nComputer: {comp_score}\n")

        elif user_choice == Scissors and comp_choice == Rock: #Scissors vs Rock
            comp_score += 1 #Updates score
            num_rounds += 1
            print(f"Round {num_rounds} goes to Computer.\nYou: {user_score}\nComputer: {comp_score}\n")

        elif user_choice == Scissors and comp_choice == Paper: #Scissors vs Paper
            user_score += 1 #Updates score
            num_rounds += 1
            print(f"Round {num_rounds} goes to You.\nYou: {user_score}\nComputer: {comp_score}\n")

        else: #Same Combination
            print(f"Tie. Please Try Again.\nYou: {user_score}\nComputer: {comp_score}\n")
                
    if comp_score == (best_of + 1)/2 : #Checks to see if Computer won, else player won
        print("You Lost. Please Try Again!")
        try_again_response = input("Would you like to play again? (Y/N): ").lower()

        while True: #Checks if they entered something other than y or n
            if try_again_response == "n" or try_again_response == "y":
                break
            else:
                try_again_response = input("Please try again: ").lower()
        if try_again_response == "n":
            break
    else:
        print("You Won!")
        try_again_response = input("Would you like to play again? (Y/N): ").lower()

        while True: #Checks if they entered something other than y or n
            if try_again_response == "n" or try_again_response == "y":
                break
            else:
                try_again_response = input("Please try again: ").lower()

        if try_again_response == "n":
            break
        

print("\nThank you for playing.\n")