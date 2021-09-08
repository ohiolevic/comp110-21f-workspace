"""Counting letters in a string."""

__author__ = "730234891"


letter: str = str(input("what letter do you want to search for?: "))
word: str = str(input("Enter a word: "))

count: int = 0
i: int = 0 

while i < (len(word) - 1):
    if word[i] == letter:
        count = count + 1
    i = i + 1
print("count: " + str(count))
