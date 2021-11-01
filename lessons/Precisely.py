def spooky() -> None: 
    b: dict[int, int] = {0: 5}
    o: dict[int, int] = b 
    b = sz(b)
    print(b[0] + o[0])


def sz(n: dict[int, int]) -> dict[int, int]:
    b: dict[int, int] = n 
    n = {0: 7}
    b[0] = 6 
    return n 


spooky()