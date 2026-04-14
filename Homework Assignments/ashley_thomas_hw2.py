#--------------------------------------------------------------------------------------------------------
#                                        BEGIN INITIALIZATION
#--------------------------------------------------------------------------------------------------------

import random  #import random module for losing coin function

#initialize variables--
state = "idle"

cost = 7
money = 0

inv_soda = 4
inv_snack = 2
inv_candy = 3

item = 0
x = ""
#----------------------

#--------------------------------------------------------------------------------------------------------
#                                        END INITIALIZATION
#--------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------
#                                            BEGIN FSM
#--------------------------------------------------------------------------------------------------------
while state != "quit": #FSM will end if state changes to 'quit'
#--------------------------------------------------------------------------------------------------------    
#                                          state A: idle
#--------------------------------------------------------------------------------------------------------
    if state == "idle":
        valid = False
        while not valid:               #will loop until valid input
            x = input("Enter 'start' to begin, 'restock' to restock the vending machine, and 'quit' to exit: ")
            if x == "start" or x == "restock" or x == "quit":
                valid = True           #lets while-loop know a valid input has been entered 
                state = x              #changes state accordingly          
            else:
                print("Invalid input") #lets user know invalid input was entered
                
#--------------------------------------------------------------------------------------------------------                
#                                          state B: start
#--------------------------------------------------------------------------------------------------------                
    elif state == "start":
        valid = False
        while not valid:                    #will loop until valid input
            x = input("Enter amount of coins needed or 'change' to cancel your transactions: ")
            if x == "change":               #checks if input is change
                valid = True                 
                state = x                    
            elif x.isdigit and int(x) >= 0: #checks if input is a valid number
                if (random.random() > 0.3): #logic for 30% chance for vending machine to lose money                       
                    money = int(x)          #sets money to user input
                    valid = True             
                    state = "select"        #changes state to state C
                else:
                    print("Oops, I lost you money")
            else:
                print("Invalid input")      #lets user know invalid input was entered

#--------------------------------------------------------------------------------------------------------
#                                          state C: select
#--------------------------------------------------------------------------------------------------------       
    elif state == "select":
        valid = False
        while not valid: #will loop until valid input which is soda, snack, candy, or change
            x = str(input("Enter 'soda' to select soda, 'snack' to select a snack, 'candy' to select a candy, and 'change' to refund your transaction: "))
            if x == "soda": 
                item = 1               #sets item to users selected item 
                valid = True
                state = "dispense"     #changes state to state D
            elif x == "snack":
                item = 2
                valid = True
                state = "dispense"
            elif x == "candy":
                item = 3
                valid = True
                state = "dispense"
            elif x == "change":        #checks if input is change
                state = x
                valid = True
            else:
                print("Invalid input") #lets user know invalid input was entered   

#--------------------------------------------------------------------------------------------------------                
#                                          state D: dispense
#--------------------------------------------------------------------------------------------------------   
    elif state == "dispense":
        if money < cost:                 #checks if user has enough money, and if not-
            print("Not enough money")    #-lets user know and changes state to change
            state = "change"
        elif item == 1 and inv_soda > 0: #checks if selected item is in stock
            print("Dispensing soda")
            money -= cost                #subtracts cost of item from user's money
            inv_soda -= 1                #subtracts one from select item's stock
            state = "change"             #changes state to state E
        elif item == 2 and inv_snack > 0:
            print("Dispensing snack")
            money -= cost
            inv_snack -= 1
            state = "change"
        elif item == 1 and inv_candy > 0:
            print("Dispensing candy")
            money -= cost
            inv_candy -= 1
            state = "change"
        else:                             #lets user know selected product is out of stock
            print("Not enough product")

#--------------------------------------------------------------------------------------------------------
#                                          state E: change
#--------------------------------------------------------------------------------------------------------    
    elif state == "change":
        print(f"Returning {money} amount of change")           
        money = 0      #sets money to zero which "refunds" user's money
        state = "idle" #changes state to state A

#--------------------------------------------------------------------------------------------------------      
#                                          state F: restock
#--------------------------------------------------------------------------------------------------------
    elif state == "restock": 
        inv_soda = 4   #\
        inv_snack = 2  # |--reset inventory to original values
        inv_candy = 3  #/
        print("Items have been restocked")
        state = "idle" #changes state to state A   

#--------------------------------------------------------------------------------------------------------
#                                            END FSM
#--------------------------------------------------------------------------------------------------------
print("Goodbye") #program end
