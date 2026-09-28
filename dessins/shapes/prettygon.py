import math
import turtle


def draw_prettygon(
    K: int = 200,
    AN: float = 15 * (math.pi / 31),
    RA: float = 0.98,
    AA: float = 0.0,
    RR: float = 480 * 0.80,
    initial_y: float = 0,
    NP: int = 480,
) -> list[tuple[float, float]]:
    X = (NP - RR) / 2
    Y = initial_y

    pts: list[tuple[float, float]] = []

    turtle.penup()
    pts.append((X, Y))
    turtle.goto(X, Y)
    turtle.pendown()

    for _ in range(K + 1):
        X += RR * math.cos(AA)
        Y += RR * math.sin(AA)
        # TODO: add alternative function for design_33

        pts.append((X, Y))
        turtle.goto(X, Y)

        AA += AN
        RR *= RA

    return pts

