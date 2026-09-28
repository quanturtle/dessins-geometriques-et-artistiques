"""Le programme POLYGONES RÉGULIERS (designs 1-6)."""

import math
import turtle


def draw_regular_polygon(
    CX: float = 240,
    CY: float = 240,
    K: int = 4,
    R: float = 480 * 0.45,
    AD: float = math.pi / 4,
    NP: int = 480,
) -> None:
    for i in range(K + 1):
        x = CX + R * math.cos((2 * math.pi * i / K) + AD)
        y = CY + R * math.sin((2 * math.pi * i / K) + AD)

        if i == 0:
            turtle.penup()
        else:
            turtle.pendown()

        turtle.goto(x, y)

    return
