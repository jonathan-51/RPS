import random,datetime,csv

combinations = [[0,-1,1],[1,0,-1],[-1,1,0]] #Create matrix for all combinations
numtoword = {0:"r",
             1:"p",
             2:"s"}

time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

#Checks if number is odd or even
def IsOdd(n): 
    return n % 2 == 0

#gets format for current game
def get_format(best_of_local): 
    while True: #filters out all possible responses except for odd numbers
        try: #Converts input into an integer
            best_of_local = int(best_of_local)
        except:
            best_of_local = input("Encountered an error.\nPlease enter an odd number: ")

        if type(best_of_local) == int and IsOdd(best_of_local) == False: #Filters out the odd numbers
            break
        else: #filters out everything else like strings and even numbers
            best_of_local = input("Encountered an error.\nPlease enter an odd number: ")

    return  best_of_local

#gets the user choice for each round and verifies it
def verify_user_choice(user_choice_local):
    while True: #Checks to see if player entered a valid choice (r/p/s)
        if user_choice_local != "r" and user_choice != "p" and user_choice != "s":
            user_choice_local = input("Please Try Again. Enter (r/p/s): ").lower()
        else:
            return 

#gets outcome of the round in the form of a number
def get_outcome_round (user_input,combinations_local,comp_choice):
    if user_input == "r":
        return combinations_local[0][comp_choice] #assigns the outcome of the round to a variable
    elif user_input == "p":
        return combinations_local[1][comp_choice] #assigns the outcome of the round to a variable
    else:
        return combinations_local[2][comp_choice] #assigns the outcome of the round to a variable    

#Determines the winner of a round
def determine_round_winner (outcome_local,dictionary_local):
    if outcome_local == 0:
        dictionary_local["Round Winner"] = "tie" #Updates winner of the round
        dictionary_local["Total Rounds"] += 1 #Updates TOTAL number of rounds played
        print(f"Tie. Please Try Again.\nYOU: {dictionary_local["User Score"]} | COMPUTER: {dictionary_local["Computer Score"]}\n")

        return dictionary_local
    elif outcome_local == 1:
        dictionary_local["User Score"] += 1  #Updates User score
        dictionary_local["Round Number"] += 1 #Updates number of rounds effectively played
        dictionary_local["Total Rounds"] += 1 #Updates the TOTAL number of rounds played (including ties)
        dictionary_local["Round Winner"] = "player" #Updates winner of the round
        print(f"Round {dictionary_local["Round Number"]} goes to YOU.\nYOU: {dictionary_local["User Score"]} | COMPUTER: {dictionary_local["Computer Score"]}\n")
        return dictionary_local
    else:
        dictionary_local["Computer Score"] += 1  #Updates computer score
        dictionary_local["Round Number"] += 1 #Updates number of rounds effectively played
        dictionary_local["Total Rounds"] += 1 #Updates the TOTAL number of rounds played (including ties)
        dictionary_local["Round Winner"] = "computer" #Updates winner of the round
        print(f"Round {dictionary_local["Round Number"]} goes to the COMPUTER.\nYOU: {dictionary_local["User Score"]} | COMPUTER: {dictionary_local["Computer Score"]}\n")
        return dictionary_local

#Determines if the user wants to play again
def verify_play_again (try_again_response_local):
    while True: #Checks if they entered something other than y or n
        if try_again_response_local == "n" or try_again_response_local == "y":
            break
        else:
            try_again_response_local = input("Please try again: ").lower()
    return try_again_response_local

#Executes Play again
def exe_play_again(comp_score_local,num_win_req_local):
    if comp_score_local == num_win_req_local : #Checks to see if Computer won, else player won
        try_again_response_local = input("You Lost.\nWould you like to play again? (Y/N): ").lower()

        #Verifies the user input and then determines if they want to play again.
        if verify_play_again(try_again_response_local) == "n":
            return False
    else:
        try_again_response_local = input("You Won.\nWould you like to play again? (Y/N): ").lower()

        #Verifies the user input and then determines if they want to play again.
        if verify_play_again(try_again_response_local) == "n":
            return False
    return    

#Start Game
while True: 
    #Gets gameid for current game by assign final row on to variable rows.
    with open("game_log.csv","r") as f:
        for rows in csv.DictReader(f):
            pass
        gameid = int(rows["gameid"]) + 1

    user_score = 0
    comp_score = 0
    dictionary = {"Round Number":0, # Storing number of rounds played (excl ties)
                  "Computer Score":0, #Storing Computer score
                  "User Score":0, #Storing Player score
                  "Total Rounds":0, #Storing Total rounds played (incl ties)
                  "Round Winner":""} #initializing key:value for game winner
    
    #Determines Format
    best_of = input("Choose a format: best of 3, best of 5, best of 7....")

    #number of wins to win the game
    num_win_req = (get_format(best_of) + 1)/2  

    #loops the rounds
    while user_score < num_win_req and comp_score < num_win_req:
        #randomizes computer's choice
        comp_choice = random.choice([0,1,2])

        #Gets User Choice
        user_choice = input("Please Enter Your Choice (R for Rock, P for Paper, S for Scissors: ").lower()

        #Verifies User Choice
        verify_user_choice(user_choice)

        #converts whatever the user inputted into a specific number
        outcome = get_outcome_round(user_choice,combinations,comp_choice)
        comp_choice_letter = numtoword[comp_choice]
        #Determines who won the round
        dictionary = determine_round_winner(outcome,dictionary)

        num_rounds = dictionary["Round Number"] #updates round # (excl ties)
        comp_score = dictionary["Computer Score"] #updates computer score
        user_score = dictionary["User Score"] #updates player score
        tot_rounds = dictionary["Total Rounds"] #updates TOTAL round # (incl ties)

        #Logs current round results: Game ID | Round #(incl ties) | Round #(excl ties) | Round Winner | Computer's Choice | Player Choice | Computer Score | Player Score
        with open("match_report.csv","a") as f:
            f.write(f"\n{gameid},{tot_rounds},{num_rounds},{dictionary["Round Winner"]},{comp_choice_letter},{user_choice},{comp_score},{user_score}")

    if comp_score == num_rounds:
        winner = "computer"
    else:
        winner = "player"
    #Logs Game Result: Date + Time | Game Id | Winner | Best Of | Computer's Score| Player Score
    with open("game_log.csv","a") as f:
        f.write(f"\n{time},{gameid},{winner},{best_of},{comp_score},{user_score}")

    #Asks Player if they want to play again
    if exe_play_again(comp_score,num_win_req) == False:
        break

  
print("\nThank you for playing.\n_____________________________________\n")