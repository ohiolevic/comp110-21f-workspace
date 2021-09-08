"""Repeating a beat in a loop."""

__author__ = "730234891"


beat: str = input("what beat do you want to repeat? ")
num_of_repeats: int = int(input("How many times do you want to repeat it? "))

num_of_repeats: int = (num_of_repeats - 1)

print((beat + " ") * (num_of_repeats) + beat)

if num_of_repeats <= 0: 
    print("No beat...")