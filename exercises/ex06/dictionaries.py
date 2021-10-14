"""Practice with dictionaries."""

__author__ = "730234891"

# Define your functions below


def invert(input_one: dict[str, str]) -> dict[str, str]: 
    """Inverting the key and the value of a dictionary."""
    new_invert: dict[str, str] = {}
    for a in input_one: 
        if input_one[a] in new_invert: 
            raise KeyError("There is somthing wrong")
        new_invert[input_one[a]] = a 
    return new_invert


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
    print(colour)
    return colour


def count(input_one: list[str]) -> dict[str, int]:
    """Counts the times a value is repeated."""
    xs = dict() 
    for x in input_one:
        xs[x] = 0 
    for x in xs.keys():
        for y in input_one:
            if y == x:
                xs[x] = xs[x] + 1 
    return xs