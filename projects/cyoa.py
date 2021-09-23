"""Choose Your Own Adventure."""

__author__ = "730234891"

from random import randint


def main():
    global points
    global player
    global try_again
    try_again = "\U0001F917"
    points = 0 
    player = str("")
    greet()
    game()
    return None


def greet(): 
    global player 
    player = input("what is your name? ")
    print(f"Welcome to your fortune with a coin flip journey, {player}!")
    return None
    

def game():
    global try_again
    global points
    start_game: str = input("Let's begin, would you go heads, tails, coin bank or home? ")
    """Enter 1 for Heads and 2 for tails and 3 to go home"""
    if (start_game == 1):
        heads_flip()
    if (start_game == 2):
        tails_flip()
    if (start_game == 4): 
        print(" you have gotten zero fortune point(s).")
        print("Goodbye! " + try_again)
        

def heads_flip(): 
    i: int = 0 
    global player 
    global points
    while i < 20: 
        flip: int = randint(0, 20)
        if (flip == int(input((player) + " Guess a number? "))): 
            points = points + 1
            print(player + "The love of your life is more close than you think! Guess again")
        else: 
            i = i + 1
            print(f"{player}, you suck!")
        print(f'you have {points} total points') 
        game()
        return None


def tails_flip():
    global player 
    global points
    i: int = int(input(f"{player}, this is a different journey. Guess the number of coin flips: "))
    tails: int = randint(0, 15)
    if i == tails: 
        points = points + 1 
    print(f"{player}, you are correct" + "\U0001f981")
    print(f"you have {points} total fortune points(s).")
    game()
    return None


def home():
    global player
    """Ask if the player wants to play again. C for Yes or N for No"""
    answer: str = input(f"{player}, do you want play again. ")
    if answer == "C":
        game()
    if answer == "N":
        print("Adios! " + try_again)


if __name__ == "__main__":
    main()