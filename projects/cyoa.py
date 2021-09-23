"""Choose Your Own Adventure."""

__author__ = "730234891"

from random import randint

points: int
player: str


def main() -> None:
    """Welcome to the game of the century."""
    global points
    global player
    global try_again
    points = 0 
    player = str("")
    greet()
    game()
    

def greet() -> None: 
    """Greets the player and ask for name."""
    global player
    player = input("what is your name? ")
    print(f"Welcome to your fortune with a coin flip journey, {player}!")
    
    
def game() -> None:
    """Defining parameters of the game."""
    global points
    start_game: str = input("Let's begin, would you go heads, tails, coin bank or home? ")
    """Enter X for Heads and Y for tails and Z to go home."""
    if (start_game == "X"):
        heads_flip()
    if (start_game == "Y"):
        tails_flip()
    if (start_game == "Z"): 
        print(" you have gotten zero fortune point(s).")
        print("Goodbye! " + "\U0001F917")
        

def heads_flip() -> None: 
    """A game that sees how good you can guess."""
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


def tails_flip() -> None:
    """How good are you in guessing in sequences."""
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
    

def home() -> None:
    """End of game."""
    global player
    """Ask if the player wants to play again C for Yes or N for No."""
    answer: str = input(f"{player}, do you want play again. ")
    if answer == "C":
        game()
    if answer == "N":
        print("Adios! " + "\U0001F917")


if __name__ == "__main__":
    main()