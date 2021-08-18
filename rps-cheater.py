from random import *
import os

replay = "y"
picks = ["rock", "paper", "scissors"]
cheats = ["ro- I mean scissors", "pa- I mean rock", "sci- I mean paper"]
insults = ["you must have eaten a lot of paint chips as a kid",
"wow, did your mom drop you on your head?",
"you really suck at this, just give up",
"a monkey could play better, and smell better too",
"someone call an ambulance, this person's getting killed over here"]
tally = [0,0]


while replay.lower() == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    cpu = randint(0,2)
    user = "a"
    cheat = 0
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

    if randint(0,3) != 1:
        cheat += 1
    if randint(0,9) == 0 and tally[0] != 0:
        tally[0] -= 1

    if user == 0 and cpu == 2:
        if cheat == 0:
            print("I picked", picks[cpu], "so you win!")
            tally[0] += 1
        else:
            print("I picked", cheats[2], "so you lose!")
            tally[1] += 1
    elif user > cpu:
        if cheat == 0:
            print("I picked", picks[cpu], "so you win!")
            tally[0] += 1
        else:
            print("I picked", cheats[user - 1], "so you lose!")
            tally[1] += 1
    elif user < cpu:
            print("I picked", picks[cpu], "so you lose!")
            tally[1] += 1
    elif user == cpu:
        print("We both picked", picks[cpu], "so it's a tie...")

    print(tally[0], "wins,", tally[1], "losses")
    if tally[0] / tally[1] < .5:
        print(insults[randint(0,4)])
    replay = "x"
    while replay.lower() != "y" and replay.lower() != "n":
        replay = input("play again? [y/n]")

if tally[0] / tally[1] < .5:
    print("I win and you're terrible")
