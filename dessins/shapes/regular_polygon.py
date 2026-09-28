import math
import turtle


def draw_regular_polygon(
    CX: float = 240,
    CY: float = 240,
    K: int = 5,
    R: float = 240 * 0.45,
    AD: float = math.pi / 4,
    NP: int = 480,
) -> list[tuple[float, float]]:
    pts: list[tuple[float, float]] = []
    
    for i in range(K + 1):
        x = CX + R * math.cos((2 * math.pi * i / K) + AD)
        y = CY + R * math.sin((2 * math.pi * i / K) + AD)
        
        if i == 0:
            turtle.penup()
        else:
            turtle.pendown()
        
        pts.append((x, y))
        turtle.goto(x, y)
        
    return pts
