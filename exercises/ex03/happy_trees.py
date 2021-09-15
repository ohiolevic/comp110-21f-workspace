"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
times: int = int(input("Depth: "))

cycles: int = 1 

while cycles <= times:
    print(TREE * cycles)
    cycles = cycles + 1