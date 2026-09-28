import math
import turtle
from typing import Callable


def default_compute_X(NP: int, K1: float, i: int, N: int) -> int:
    return int(NP * 0.5 * (1 + math.sin(K1 * i * math.pi / N)))


def default_compute_Y(NP: int, K2: float, i: int, N: int) -> int:
    return int(NP * 0.75 * (1 + math.cos(K2 * i * math.pi / N)))


def default_I1_func(i: int, H: int, N: int) -> int:
    return i % N


def default_I2_func(i: int, H: int, N: int) -> int:
    return (H * i) % N


def draw_linear_modulo(
    N: int = 400,
    M: int = 400,
    K1: float = 4,
    K2: float = 5,
    H: int = 2,
    compute_X: Callable = default_compute_X,
    compute_Y: Callable = default_compute_Y,
    I1_func: Callable = default_I1_func,
    I2_func: Callable = default_I2_func,
    NP: int = 480,
) -> None:
    X: list[int] = []
    Y: list[int] = []

    for i in range(N):
        x = compute_X(NP, K1, i, N)
        y = compute_Y(NP, K2, i, N)

        X.append(x)
        Y.append(y)

    for i in range(M):
        I1 = I1_func(i, H, N)
        I2 = I2_func(i, H, N)

        turtle.penup()
        turtle.goto(X[I1], Y[I1])
        turtle.pendown()

        turtle.goto(X[I2], Y[I2])

