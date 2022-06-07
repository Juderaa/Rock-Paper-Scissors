# Rock-Paper-Scissors game

import random

print("Hello Player, \nRock-Paper-Scissors")
print("  ¡CPU vs Player¡")
print('Rules; \n *Rock crushes scissors;\n *Paper covers rock; \n *Scissors cuts paper.\n')

while True:
    R = "rock"
    P = "paper"
    S = "scissors"
    options = [S,P,R]
    compChoice = random.choice(options)
    
    playerChoice = input("Pick (R,P or S): ").upper()
    
## To link the users choice with the defined options
    
    if playerChoice == "R":
        playerChoice = R
        print(f"\nPlayer({playerChoice}) :: CPU ({compChoice})\n")
    elif playerChoice =="P":
        playerChoice = P
        print(f"\nPlayer({playerChoice}) :: CPU ({compChoice})\n")
    elif playerChoice == "S":
        playerChoice = S
        print(f"\nPlayer({playerChoice}) :: CPU ({compChoice})\n")
    else:
        print("Error...")
        continue
        
## Decide the winner
    
    if playerChoice == compChoice:
        print("It is a Tie")
    elif playerChoice == R and compChoice == S:
        print("Player Wins!!!")
    elif playerChoice == S and compChoice == R:
        print("CPU Wins")
    elif playerChoice == S and compChoice == P:
        print("Player Wins")
    elif playerChoice == P and compChoice == S:
        print("CPU Wins")
    elif playerChoice == P and compChoice == R:
        print("Player Wins")
    elif playerChoice == R and compChoice == P:
        print("CPU Wins")

## This allows the player decide to continue or to quit
        
    go_again = input("Another round?(y/n)  ")
    
    if go_again.lower() =='y' or go_again.lower() =='yes':
        continue
    else:
        break

print("Bye...")
