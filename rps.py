from random import *

replay = "y"
picks = ["rock", "paper", "scissors"]
tally = [0,0]

while replay.lower() == "y":
    cpu = randint(0,2)
    user = "a"
    while (user.lower() != "rock" and
    user.lower() != "paper" and
    user.lower() != "scissors" and
    user.lower() != "r" and
    user.lower() != "p" and
    user.lower() != "s"):
        user = input("enter [r]ock, [p]aper, or [s]cissors: ")

    if user == "rock" or user == "r":
        user = 0
    elif user == "paper" or user == "p":
        user = 1
    elif user == "scissors" or user == "s":
        user = 2

    if user == 0 and cpu == 2:
        print(picks[user], "beats", picks[cpu], "so you win!")
        tally[0] = tally[0] + 1
    elif user > cpu:
        print(picks[user], "beats", picks[cpu], "so you win!")
        tally[0] = tally[0] + 1
    elif user < cpu:
        print(picks[user], "loses to", picks[cpu], "so you lose!")
        tally[1] = tally[1] + 1
    elif user == cpu:
        print("you both picked", picks[cpu], "so it's a tie...")

    print(tally[0], "wins,", tally[1], "losses")
    replay = "x"
    while replay.lower() != "y" and replay.lower() != "n":
        replay = input("play again? [y/n]")
