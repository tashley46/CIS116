#--------------------------------------------------------------------------------------------------------------------
#File name: tommy_ashley_homework3.py
#Author: Tommy Ashley
#Section: A
#Description: This program is a game two player game where players take turns taking 1 to 3 sticks from a pile of 20. 
# After each turn, there is a 60% chance the wizard may add 1-3 sticks to the pile. The player who takes the last 
#stick loses. The user can choose to play against an 'AI' that uses a strategy to win.
#--------------------------------------------------------------------------------------------------------------------


import random # import random library to use for random number generation in the not_quite_right function

#--------------------------------------------------------------------------------------------------------------------
#                                                 START: not_quite_right
#--------------------------------------------------------------------------------------------------------------------
def not_quite_right(sticks): #function for wizard randomly adding sticks
    chance = random.randint(1,10)
    added_sticks = 0    
    
    if chance <= 6: #<6 means theres 60% chance the wizard will add sticks
        added_sticks = random.randint(1,3) #random int [1,3]
        
    if sticks + added_sticks > 20: #checks and corrects if the wizard adds too many sticks and goes over 20
        added_sticks = 20 - sticks
        
    return added_sticks
#--------------------------------------------------------------------------------------------------------------------
#                                                 END: not_quite_right
#--------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------
#                                                 START: display_board
#--------------------------------------------------------------------------------------------------------------------
def display_board(sticks): #prints the game board based on number of sticks remaining
    print()                                                                                #\                 
    print()                                                                                # |- padding for scoreboard
    print("------------------------------------------------------------------------------")#/
    for i in range(1,5): #5 rows of '|', each collumn represents a stick remaining
        for j in range(1,sticks + 1):
            print("|", end = "   ")
        print()
    for j in range(1,sticks + 1): #print a number underneath each stick, extra padding for numbers with less than 2 digits
        if j <10:
            print(j, end = "   ")
        else:
            print(j, end="  ")
    print()                                                                                #\
    print("------------------------------------------------------------------------------")# |
    print()                                                                                # |- padding for scoreboard                                
    print()                                                                                #/   
#--------------------------------------------------------------------------------------------------------------------
#                                                 END: display_board
#--------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------
#                                                 START: get_sticks_to_take
#--------------------------------------------------------------------------------------------------------------------
def get_sticks_to_take(p, sticks): #gets the number of sticks that player will take
    take = 0 # int for number of sticks the player will take
    valid = False # bool varible to check for valid input
    while not valid:
        take = input(f"How many sticks are you taking player {p}? ")
        if take.isdigit(): #checks if the input is a number
            take = int(take) #converts input to an integer
            if take < 1 or take > 3 or take > sticks: #checks for valid amount to take
                print("Invalid input, try again")
            else:
                valid = True
                return take   
        else:
            print("Invalid input, try again")
#--------------------------------------------------------------------------------------------------------------------
#                                                 END: get_sticks_to_take
#--------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------
#                                                 START: display_summary
#--------------------------------------------------------------------------------------------------------------------
def display_summary(p, sticks_taken, sticks_added, sticks): # displays the summary of the turn
    print(f"Player {p} took {sticks_taken}. The wizard added {sticks_added} leaving {sticks}") 
#--------------------------------------------------------------------------------------------------------------------
#                                                 END: display_summary
#--------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------
#                                                 START: ai_get_sticks_to_take
#--------------------------------------------------------------------------------------------------------------------
def get_sticks_to_take_AI(sticks): #logic for how many sticks 'AI' will take
    if sticks % 4 == 0: #take 3 sticks if number of sticks is a multiple of 4
        return 3
    elif sticks % 4 == 1 or sticks % 4 == 2: #take only 1 sticks if the number of sticks is 1 or 2 more than a multiple of 4
        return 1
    elif sticks % 4 == 3: # take 2 sticks if the number of sticks is 3 more than a multiple of 4
        return 2    
#--------------------------------------------------------------------------------------------------------------------
#                                                 END: ai_get_sticks_to_take
#--------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------
#                                                 START: main
#--------------------------------------------------------------------------------------------------------------------
def main(): #main function to run the game
    total_sticks = 20 #initial amount of sticks on the board
    player = 1 #player can either be 1 or 2, player 1 always goes first
    
    ai = False #bool to check if user is playing agaisnt AI
    valid = False
    while not valid: #asks user if they want to play against an AI, checks for valid input
        inp = input("Do you want to play against an AI? (y/n) ").lower()
        if inp == "y":
                ai = True
                valid = True
        elif inp == "n":
            valid = True
        else:
            print("Invalid input")

    while total_sticks != 0:#game loop, only ends when no sticks are left on the board
        if player == 1: #player 1's turn/user's turn logic
            display_board(total_sticks) #display the board at the start of the turn
            sticks_taken = get_sticks_to_take(player, total_sticks)# get sticks taken from user input
            sticks_added = not_quite_right(total_sticks - sticks_taken) #get sticks added from wizard
            display_summary(player, sticks_taken, sticks_added, total_sticks - sticks_taken + sticks_added) #display summary without changing total_sticks
            total_sticks = total_sticks - sticks_taken + sticks_added #update total sticks, after summary so the loop can end if the player takes the last stick
            player = 2 # changes turn to player 2/AI if total sticks isn't already 0
        elif player == 2 and ai:#ai turn logic, also counts as player two for simplicity
            display_board(total_sticks)
            sticks_taken = get_sticks_to_take_AI(total_sticks) #get sticks from AI logic
            sticks_added = not_quite_right(total_sticks - sticks_taken)    
            display_summary(player, sticks_taken, sticks_added, total_sticks - sticks_taken + sticks_added)    
            total_sticks = total_sticks - sticks_taken + sticks_added
            player = 1 # changes turn to player 1 if total sticks isn't already 0
        else: #player 2 turn logic, if not playing against AI
            display_board(total_sticks)
            sticks_taken = get_sticks_to_take(player, total_sticks)
            sticks_added = not_quite_right(total_sticks - sticks_taken)
            display_summary(player, sticks_taken, sticks_added, total_sticks - sticks_taken + sticks_added)    
            total_sticks = total_sticks - sticks_taken + sticks_added
            player = 1 #changes turn to player 1 if total sticks isn't already 0
    print(f"Player {player} wins!")
#--------------------------------------------------------------------------------------------------------------------
#                                                 END: main
#--------------------------------------------------------------------------------------------------------------------

main() #call main function to start the program