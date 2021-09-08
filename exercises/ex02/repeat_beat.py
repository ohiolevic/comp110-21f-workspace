"""Repeating a beat in a loop."""

__author__ = "730234891"


beat: str = input("what beat do you want to repeat? ")
num_times: int = int(input("How many times do you want to repeat it? "))

x: int = 0
y: str = ""

while x < num_times:
    y = beat + " " + y
    x = x + 1

    print(y)