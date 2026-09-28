import math
import turtle
from typing import Callable


def sgn(x: float) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def default_deformation_subroutine(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        return DI ** 0.3, AN

    return DI, AN


def default_xy_transform(I: float, J: float) -> tuple[float, float]:
    return I / 10 - 1, J / 10 - 1


def draw_elastic_grid(
    deformation_subroutine: Callable = default_deformation_subroutine,
    xy_transform: Callable = default_xy_transform,
    L_range: int = 2,
    I_range: int = 21,
    J_range: int = 21,
    NP: int = 480,
) -> None:
    for L in range(L_range):
        for I in range(I_range):
            for J in range(J_range):
                X, Y = xy_transform(I, J)

                if L == 1:
                    X, Y = Y, X

                DI = math.sqrt(X * X + Y * Y)

                if abs(X) > 1e-12:
                    AN = math.atan(Y / X)
                else:
                    AN = (math.pi / 2) * sgn(Y)

                if X < 0:
                    AN += math.pi

                DI, AN = deformation_subroutine(DI, AN)

                X = DI * math.cos(AN)
                Y = DI * math.sin(AN)

                X_ = int(NP / 2 * (1 + 0.95 * X))
                Y_ = int(NP / 2 * (1 + 0.95 * Y))

                if J == 0:
                    turtle.penup()
                    turtle.goto(X_, Y_)
                else:
                    turtle.pendown()
                    turtle.goto(X_, Y_)

