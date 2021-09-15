"""Finding duplicate letters in a word."""

__author__ = "730234891"
word: str = input("Enter a word: ")

x: int = 0 
y: int = 0 

while x < len(word): 
    i: int = x + 1 
    while i < len(word): 
        if word[x] == word[i]: 
            y = y + 1 
        i = i + 1
    x = x + 1

print("Found duplicate: " + str(y > 0))