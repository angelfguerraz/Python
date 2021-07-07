import random
import os
from time import sleep

DATA = []

def run():
    read()
    word_2_guess = list(random.choice(DATA))  # Word to guess as a list
    # All chars turn to lower-case
    word_2_guess = [i.lower() for i in word_2_guess]
    word_found = ["_"]*len(word_2_guess)

    print("Start guessing...")
    print(word_found)
    print(word_2_guess)

    while word_2_guess != word_found:
        c = input("Insert a character: ")
        
        for index, char in enumerate(word_2_guess):
            if c.lower() == char:
                word_found[index] = word_2_guess[index]

                sleep(0.5)
                screen_clear()
                print(word_found)

# The screen clear function
def screen_clear():
    if os.name == 'posix': 
        _ = os.system('clear') # unix
    else:
        _ = os.system('cls') # windows

def read():
    with open("/Volumes/Mec/AFGZB/Documents/Portofolio/Python/Basics/Hangman/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            # replace deletes the 'newline' char
            DATA.append(line.replace("\n", ""))

if __name__ == '__main__':
    run()
