import math
import turtle
from typing import Callable


def default_compute_R1(i: int, NP: int) -> float:
    return NP / 4


def default_compute_R2(i: int, NP: int) -> float:
    return NP * 5 / 24


def default_compute_YD(NP: int, R1: float, R2: float, AN: float, K: int) -> float:
    return NP / 2 + R1 * math.sin(AN) + R2 * math.sin(K * AN)


def default_compute_YA(NP: int, R1: float, R2: float, AN: float, K: int) -> float:
    return NP / 2 + R1 * math.sin(AN) + R2 * math.sin(K * AN + math.pi)


def draw_linear_sticks(
    N: int = 100,
    M: int = 1,
    K: int = 5,
    compute_R1: Callable = default_compute_R1,
    compute_R2: Callable = default_compute_R2,
    compute_YD: Callable = default_compute_YD,
    compute_YA: Callable = default_compute_YA,
    NP: int = 480,
) -> None:
    for i in range(1, M + 1):
        R1 = compute_R1(i, NP)
        R2 = compute_R2(i, NP)

        for j in range(N):
            AN = 2 * j * math.pi / N

            XD = NP / 2 + R1 * math.cos(AN) + R2 * math.cos(K * AN)
            YD = compute_YD(NP, R1, R2, AN, K)

            XA = NP / 2 + R1 * math.cos(AN) + R2 * math.cos(K * AN + math.pi)
            YA = compute_YA(NP, R1, R2, AN, K)

            turtle.penup()
            turtle.goto(XD, YD)
            turtle.pendown()

            turtle.goto(XA, YA)

