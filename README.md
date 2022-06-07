# Rock-Paper-Scissors
Hello and welcome,
This is a simple Rock-Paper-Scissors game, between the player (Human) and the computer (CPU).
# How it Works
When the program is run the user picks between "R", "P" or "S". 
If user input is not amongst the set options, an error is printed and it asks for an input again.
With the `choice` function from the inbuilt Python `random` module a choice is made for the computer.
Both player's moves  are printed in the format: `Player (Rock) : CPU (Paper)`
It then checks both player's moves: 
If there is a winner, the winner is printed. 
If it's a tie (the computer and player pick the same move), it restarts the game.
