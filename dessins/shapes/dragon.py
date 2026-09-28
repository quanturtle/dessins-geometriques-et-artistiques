import math
import turtle
from typing import Callable


def default_A_func(N: int) -> list[int]:
    return [0] * (N + 1)


def draw_dragon(
    N: int = 10,
    A_initializer: Callable[[int], list[int]] = default_A_func,
    initial_values: list[float] = [480 / 3, 480 / 2, -math.pi / 4 * (10 - 2), 480 / math.sqrt(2) ** 10],
    NP: int = 480,
) -> list[tuple[float, float]]:
    pts: list[tuple[float, float]] = []
    A = A_initializer(N)

    X0, Y0, A0, L0 = initial_values
    X1 = X0
    Y1 = Y0
    X2 = X0
    Y2 = Y0

    def gosub() -> None:
        nonlocal X0, Y0, X1, Y1, X2, Y2
        X0 = X1
        Y0 = Y1
        X1 = X2
        Y1 = Y2
        X2 = X2 + L0 * math.cos(A0)
        Y2 = Y2 + L0 * math.sin(A0)

    turtle.penup()
    turtle.goto(X0, Y0)
    turtle.pendown()

    NN = pow(2, N) - 1

    for I in range(NN + 1):
        if I == 0:
            gosub()
        else:
            II = I
            J = 0

            while II % 2 == 0:
                II = II // 2
                J += 1

            AA = (A[N - J] * 2 - 1) * (((II - 1) // 2) % 2 * 2 - 1) * math.pi / 2
            A0 += AA

            gosub()

        mid_x1 = (X0 + 3 * X1) / 4
        mid_y1 = (Y0 + 3 * Y1) / 4
        mid_x2 = (X2 + 3 * X1) / 4
        mid_y2 = (Y2 + 3 * Y1) / 4

        turtle.goto(mid_x1, mid_y1)
        pts.append((mid_x1, mid_y1))

        turtle.goto(mid_x2, mid_y2)
        pts.append((mid_x2, mid_y2))

    return pts

