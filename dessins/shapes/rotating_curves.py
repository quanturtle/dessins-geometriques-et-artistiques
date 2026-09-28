import math
import turtle
from typing import Callable


def default_S_func(i: int, N: int) -> float:
    return math.cos(4 * math.pi * i / N) * 0.4 + 0.6


def default_Y_func(NP: int, C1: float, C2: float, R1: float, R2: float, S1: float, S2: float) -> float:
    return NP / 2 + R1 * S1 + R2 * (S1 * C2 + C1 * S2)


def draw_rotating_curves(
    N: int = 2000,
    T1: int = 1,
    T2: int = 100,
    K1: int = 1,
    K2: int = 1,
    H1: int = 1,
    H2: int = 1,
    R1: float = 480 / 6,
    R2: float = 480 / 4,
    S_func: Callable = default_S_func,
    Y_func: Callable = default_Y_func,
    NP: int = 480,
) -> None:
    for i in range(N):
        S_ = S_func(i, N)
        AN = 2 * math.pi * i / N

        C1 = math.cos(H1 * AN * T1)
        S1 = math.sin(H2 * AN * T1)

        C2 = S_ * math.cos(K1 * AN * T2)
        S2 = S_ * math.sin(K2 * AN * T2)

        X = NP / 2 + R1 * C1 + R2 * (C1 * C2 - S1 * S2)
        Y = Y_func(NP, C1, C2, R1, R2, S1, S2)

        if i == 0:
            turtle.penup()
            turtle.goto(int(X), int(Y))
            turtle.pendown()
        else:
            turtle.goto(int(X), int(Y))

