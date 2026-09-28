import math
import turtle
from typing import Callable


def default_r2_func(N: float, i: int, NP: int) -> float:
    return NP * 0.2 * (1 - i / N)


def default_x_func(NP: int, A1: float, A2: float, R1: float, R2: float, K1: int, K2: int) -> int:
    return int(NP * 0.5 + R1 * math.cos(K1 * A1) + R2 * math.cos(A2))


def default_y_func(NP: int, A1: float, A2: float, R1: float, R2: float, K1: int, K2: int) -> int:
    return int(NP * 0.5 + R1 * math.sin(K2 * A1) + R2 * math.sin(A2))


def draw_orbiting_curves(
    N: int = 2000,
    T1: int = 2,
    T2: int = 100,
    K1: int = 1,
    K2: int = 1,
    R1: float = 480 * 0.25,
    R2_func: Callable = default_r2_func,
    X_func: Callable = default_x_func,
    Y_func: Callable = default_y_func,
    NP: int = 480,
) -> None:
    for i in range(N):
        R2 = R2_func(N, i, NP)

        A1 = 2 * math.pi * i / N * T1
        A2 = 2 * math.pi * i / N * T2

        X = X_func(NP, A1, A2, R1, R2, K1, K2)
        Y = Y_func(NP, A1, A2, R1, R2, K1, K2)

        if i == 0:
            turtle.penup()
            turtle.goto(X, Y)
            turtle.pendown()
        else:
            turtle.goto(X, Y)

