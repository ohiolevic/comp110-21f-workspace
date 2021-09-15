"""An exercise in remainders and boolean logic."""

__author__ = "730234891"


num: int = int(input("Enter an int: "))

if num % 2 and num % 7 != 0: 
    print("CAROLINA")
else: 
    if num % 2 == 0: 
        print("TAR")
    if num % 7 == 0: 
        print("HEELS") 
    if num % 28 == 0:
        print("TAR HEELS")