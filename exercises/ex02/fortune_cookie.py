"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730234891"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says....")
fortune = randint(5, 8)

if fortune == 5:
    print("love, because it is the only true adventure.")
else:
    if fortune == 6:
        print("you have a secret admirer")
    else: 
        if fortune == 7:
            print("your love life will soon be happy and harmonious.")
        else:
            if fortune == 8:
                print("The love of your life is right in front of your eyes.")

print("Now, go spread positive vibes!")
