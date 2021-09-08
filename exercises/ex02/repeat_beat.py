"""Repeating a beat in a loop."""

__author__ = "730234891"


beat: str = input("what beat do you want to repeat? ")
num_times: int = int(input("How many times do you want to repeat it? "))

num_times: int = (num_times - 1)

print((beat + " ") * (num_times) + beat)

if num_times <= 0: 
    print("No beat...")