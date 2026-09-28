import math
import turtle
from typing import Callable


def default_AN_func(i: int, N: int) -> float:
    return 2 * math.pi * i / N


def default_Y_func(NP: int, YY: float) -> int:
    return int(NP / 2 * (1 + YY))


def draw_spiraling_curves(
    N: int = 2000,
    T: float = 40,
    R: float = 0.8,
    L: float = 0.1,
    AN_func: Callable = default_AN_func,
    Y_func: Callable = default_Y_func,
    NP: int = 480,
) -> None:
    for i in range(N):
        RR = L ** (i / N)
        AN = AN_func(i, N)

        X = RR * math.cos(T * AN)
        Y = RR * R * math.sin(T * AN)

        CO = math.cos(AN)
        SI = math.sin(AN)

        XX = X * CO - Y * SI
        YY = X * SI + Y * CO

        X_ = int(NP / 2 * (1 + XX))
        Y_ = Y_func(NP, YY)

        if i == 0:
            turtle.goto(X_, Y_)
            turtle.pendown()
        else:
            turtle.goto(X_, Y_)

