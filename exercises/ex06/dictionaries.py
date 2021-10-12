"""Practice with dictionaries."""

__author__ = "730234891"

# Define your functions below


def invert(input_one: dict[str, str]) -> dict[str, str]: 
    """Inverting the key and the value of a dictionary."""
    input_one = dict()
    for x in input_one.keys():
        for y in input_one.keys():
            if input_one[x] == input_one[y] and x != y:
                raise KeyError("There is somthing wrong.")
    for i in input_one.keys():
        input_one[input_one[i]] = i 
        input_one.pop(i)
    return input_one


def favorite_color(input_one: dict[str, str]) -> str:
    """Common color of the dict."""
    new_input: dict[str, int] = {}
    max: int = 0 
    colour: str = ""
    for x in input_one:
        if input_one[x] in new_input:
            new_input[input_one[x]] += 1
        else:
            new_input[input_one[x]] = 1
    for item in new_input: 
        if new_input[item] > max: 
            colour = item
            max = new_input[item]
    print(max)
    return colour


def count(input_one: list[str]) -> dict[str, int]:
    """Counts the times a value is repeated."""
    xs = dict() 
    for x in input_one:
        xs[x] = 0 
    for x in xs.keys():
        for y in input_one:
            if list(y) == x:
                xs[x] = xs[x] + 1 
    return xs 
