import math
import turtle


def draw_regular_star(
    CX: float = 240,
    CY: float = 240,
    K: int = 5,
    H: int = 3,
    R: float = 480 * 0.45,
    AD: float = math.pi / 2,
    NP: int = 480,
) -> None:
    for I in range(K):
        X = CX + R * math.cos(2 * I * H * math.pi / K + AD)
        Y = CY + R * math.sin(2 * I * H * math.pi / K + AD)

        if I == 0:
            turtle.penup()

        else:
            turtle.pendown()

        turtle.goto(X, Y)

    X = CX + R * math.cos(0 + AD)
    Y = CY + R * math.sin(0 + AD)

    turtle.pendown()
    turtle.goto(X, Y)

    return
