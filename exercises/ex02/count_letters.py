"""Counting letters in a string."""

__author__ = "730234891"


letter: str = str(input("what letter do you want to search for?: "))
word: str = str(input("Enter a word: "))

count: int = 0
i: int = 0 
length: int = len(word)
while count < length:
    if word[count] == letter:
        i = i + 1
    count = count + 1
print("count: " + str(i))
