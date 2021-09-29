"""List utility functions."""

__author__ = "730234891"


# TODO: Implement your functions here.
def main() -> None: 
    """Starterpoint of program."""
    list_1: list[int] = [5, 6, 7]
    list_2: list[int] = [5, 6, 7]
    max_list: list[int] = [5, 6, 7]
    print(max(max_list))
    print(all(list_1, 1))
    print(is_equal(list_1, list_2))


def all(list_1: list[int], begin: int) -> bool:
    i: int = 0 
    if len(list_1) == 0: 
        return False
    while i < len(list_1):
        numbers: int = list_1[i]
        if numbers != begin:
            return False
        i += 1

    return True


def is_equal(list_1: list[int], list_2: list[int]) -> bool: 
    a: int = 0 
    b: int = 0
    rolls: int = 0
    while a < len(list_1):
        numbers: int = list_1[a]
        numbers_2: int = list_2[b]
        if numbers == numbers_2:
            rolls += 1 
            a += 1 
            b += 1
            if rolls == len(list_1) or rolls == len(list_2):
                if a == len(list_1) and b == len(list_2): 
                    return True 
                else:
                    return False 
        else: 
            return False


def max(max_list: list[int]) -> int:
    if len(max_list) == 0: 
        raise ValueError("max() arg is an empty List")
    else: 
        i: int = 0
        reference: int = max_list[0]
        while i < len(max_list): 
            if max_list[i] > reference: 
                reference = max_list[i]
            i += 1

        return reference

        

