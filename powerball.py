#Robert Marsh
#July 7, 2020
#Program simulates a lottery drawing


##The game allows the player to enter 3 regular numbers and a powerball number
##and the input is validated 
##Regular numbers must be in the range 1 through 9 
##Regular numbers must be unique, there can be no duplicates
##The powerball number must be in the range 1 through 3
##The program then generates a random drawing 
##The player's ticket is compared against the random drawing and the winnings
##are calculated and printed 
##The player can choose to play multiple times 
##This program must use a list 
##It must have a list of three numbers for the player, and a list of three
##numbers for the computer. It must also have an integer variable for the player's
##powerball number, and an integer variable for the computer's powerball number



import random



print("Welcome to the Powerball Lottery drawing!\n")
print("A player will either select 3 numbers and a Powerball number on their own or select a quick pick.")


play = None

while play != "n":
    drawing = [] #empty drawing list
    ticket = [] #empty ticket list used for manual entry or quickpick
    dpowerball = None #drawing powerball 
    tpowerball = None #ticket powerball 
    matches = 0 #used for match check later
    pbmatch = 0 #used for powerball match later
    for i in range(3): #genreating random numbers for drawing
        randnum = random.randint(1, 9)
        while randnum in drawing:
            randnum = random.randint(1, 9)
        drawing.append(randnum)

    dpowerball = random.randint(1, 3)

##    print(drawing)
    print("""

    Please select an option below.

        1) Select your own numbers

        2) Quick pick selects randomly generated numbers

    """)
    #get user input for manual selection or quickpick
    option = int(input("Please enter a number from the above list: "))
    while option < 1 or option > 2: #validates entry 
        print("Invalid option!")
        option = int(input("Please enter a number from the above list: "))
    if option == 1: #user selects numbers
        print("\nPlease pick 3 unique numbers from 1 - 9 then a powerball number between 1 - 3.")
        for i in range(3): #player input loop and validation
            num = int(input("\nEnter number " + str(i + 1) + ":  "))
            while num < 1 or num > 10 or num in ticket:
                if num < 1 or num > 10:
                    num = int(input("\nEnter a number between 1 - 9 for #" + str(i + 1) + ": "))
                elif num in ticket:
                    num = int(input("\nEnter a unique number for #" + str(i + 1) + ": "))
            ticket.append(num)
        
        tpowerball = int(input("\nEnter your powerball number: "))    
        while tpowerball < 1 or tpowerball > 3: #player pb input and validation
            tpowerball = int(input("\nEnter your powerball number between 1 - 3: "))
        
        for d in drawing: #drawing and ticket comparison 
            for t in ticket:
                if d == t:
                    matches += 1
                else:
                    pass

        if dpowerball == tpowerball: #powerball comparison
            pbmatch += 1
        else:
            pass
                

    elif option == 2: #quickpick 
        for i in range(3): #loop for quickpick ticket and validation
            randnum = random.randint(1, 9)       
            while randnum in ticket:
                randnum = random.randint(1, 9)
            ticket.append(randnum)

        tpowerball = random.randint(1, 3)

        for d in drawing: #drawing and ticket comparison
            for t in ticket:
                if d == t:
                    matches += 1
                else:
                    pass

        if dpowerball == tpowerball: #powerball comparison
            pbmatch += 1
        else:
            pass

    print("\nYour ticket numbers:", end=" ") #ticket print out
    for i in range(3):
        print(ticket[i], end=" ")
    print("and PB:", tpowerball)

    print("\nThe drawing numbers:", end= " ") #drawing print out
    for i in range(3):
        print(drawing[i], end=" ")
    print("and PB:", dpowerball)

    #checks for matches 
    if matches == 1 and pbmatch == 0:
        print("\nYou matched 1 number, but not the powerball.")
        print("You won $1!")
    if matches == 1 and pbmatch == 1:
        print("\nYou matched 1 number and the powerball!")
        print("You won $2!")
    if matches == 2 and pbmatch == 0:
        print("\nYou matched 2 numbers, but not the powerball.")
        print("You won $10!")
    if matches == 2 and pbmatch == 1:
        print("\nYou matched 2 number and the powerball!")
        print("You won $20!")
    if matches == 3 and pbmatch == 0:
        print("\nYou matched 3 numbers, but not the powerball.")
        print("You won $100!")            
    if matches == 3 and pbmatch == 1:
        print("\nYou matched 3 numbers and the powerball!")
        print("You won $1000!")
    if matches == 0 and pbmatch == 1:
        print("\nSorry, you lost.")
    if matches == 0 and pbmatch == 0:
        print("\nSorry, you lost.")

    #asks if user wants to play again and validation
    play = input("\nPlay again? (y/n): ")#.lower()
##    while play not in ("y", "n"):
##        play = input("\nPlay again? (y/n): ").lower()
    #play = play.upper()
    while play != "Y" and play != "N":
        print("Invalid input!")
        play = input("\nPlay again? (y/n): ")
        play = play.upper()
input("\nPress Enter to exit")

    
    
