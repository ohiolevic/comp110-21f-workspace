"""CQ1) Scopes."""


def f(x: float) -> float: 
    x += 1.0
    y: float = x + 2.0
    return x + y


def g() -> None: 
    global y 
    X: float = f(3.0)
    y = f(x + 4.0)


x: float = 0.0
y: float = 0.0
g()