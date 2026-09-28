import math
import turtle


def draw_regular_star(
    CX: float = 240,
    CY: float = 240,
    K: int = 8,
    H: int = 3,
    R: float = 130,
    AD: float = math.pi / 2,
    NP: int = 480,
) -> list[tuple[float, float]]:
    pts: list[tuple[float, float]] = []

    for I in range(K):
        X = CX + R * math.cos(2 * I * H * math.pi / K + AD)
        Y = CY + R * math.sin(2 * I * H * math.pi / K + AD)
        
        if I == 0:
            turtle.penup()
        
        else:
            turtle.pendown()
        
        pts.append((X, Y))
        turtle.goto(X, Y)
    
    X = CX + R * math.cos(0 + AD)
    Y = CY + R * math.sin(0 + AD)
    
    turtle.pendown()
    pts.append((X, Y))
    turtle.goto(X, Y)

    return pts
