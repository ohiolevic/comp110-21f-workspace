"""List utility functions part 2."""

__author__ = "730234891"

# Define your functions below


def only_evens(list_1: list[int]) -> list[int]:
    """Returns list only containing even numbers."""
    i: int = 0
    xs: list[int] = []
    while i < len(list_1): 
        if list_1[i] % 2 == 0: 
            xs.append(list_1[i])
        i += 1
    return xs


def sub(list_1: list[int], start_index: int, end_index: int) -> list[int]:
    """Starting from the starting index to the end returning a sublist."""
    if len(list_1) == 0 or start_index > len(list_1) or end_index <= 0:
        return []
    if start_index < 0: 
        start_index = 0 
    i: int = start_index 
    if end_index > len(list_1):
        end_index = len(list_1)
    set: list[int] = []
    while i < end_index:
        set.append(list_1[i])
        i += 1 
    return set


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Return list containing all elements in one."""
    x: int = 0 
    y: int = 0 
    xs: list[int] = []
    while x < len(list_1): 
        xs.append(list_1[x])
        x += 1 
    while y < len(list_2): 
        xs.append(list_2[y])
        y += 1 
    return xs        