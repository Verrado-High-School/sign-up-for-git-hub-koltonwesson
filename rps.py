# Kolton Wesson
# Rock, paper, sissores
# Rock, Paper, Scissors
##########################################
# Welcome Message
# 1. Print a welcome message
# 2. Prompts for a name
# changed this
# Game Loop
# print score
# prompt for player choice
# get the computer choice (random)
# compare
# print results
# change score variable

# Score Screen
# Print "Score: "
# Print the player score using the name
# print the computer score
import random
# VARIABLES
pScore = 0
cScore = 0
ties = 0
computerChoices = ["rock", "paper", "scissors"]


#WELCOME MESSAGE
print("Welcome to Rock, Paper, Scissors")
playerName = input("What is your name?: ")


# PRINT SCORE
def printScore():
print("Score: ")
print(playerName + ": " + str(pScore))
print("Computer Score: " + str(cScore))
print("Ties: " + str(ties))

# GAME LOOP
while True:
# print the score
printScore()
# prompt for player choice
pChoice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' to quit: ")
# get the computer choice (random)
cChoice = random.choice(computerChoices)
# compare
# compare pChoice to "q"
# 1. break out of the list
if pChoice == "q":
break
# compare pChoice to "r"
# compare rock to computer choice
elif pChoice == "r":
print("You picked rock")
if cChoice == "rock":
print("Computer picked rock")
print("This is a tie")
ties = ties + 1
elif cChoice == "paper":
print("Computer picked paper")
print("Paper beats rock")
cScore = cScore + 1
else: # scissor is only one left
print("Computer picked scissors")
print("Rock beats scissors")
pScore = pScore + 1
# compare pChoice to "p"
elif pChoice == "p": #player picks paper
print("You picked paper")
if cChoice == "rock":
print("Computer picked rock")
print("Paper covers Rock")
pScore += 1
elif cChoice == "paper":
print("Computer picked paper")
print("This is a tie")
ties += 1
else: # scissor is only one left
print("Computer picked scissors")
print("scissors cut paper")
cScore += 1
# compare pChoice to "s"
elif pChoice == "s": # player picks scissors
print("You picked Scissors")
if cChoice == "rock":
print("Computer picked rock")
print("Rock Breaks Scissors")
cScore += 1
elif cChoice == "paper":
print("Computer picked paper")
print("Scissors cut Paper")
pScore += 1
else: # scissor is only one left
print("Computer picked scissors")
print("This is a tie")
ties += 1
# compare pChoice to everything else
else:
print("You picked something not on the list")


# print results
# change score variable