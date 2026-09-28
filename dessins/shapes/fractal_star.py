import math
import turtle


def draw_fractal_star(
    N: int = 5,
    K: int = 5,
    RA: float = 0.35,
    LL: int | None = None,
    AA: float = 4 * math.pi / 5,
    NP: int = 480,
) -> list[tuple[float, float]]:
    if LL is None:
        LL = NP

    X0 = (NP - LL) / 2
    Y0 = NP / 2.25
    A0 = -AA

    pts: list[tuple[float, float]] = []

    turtle.penup()
    pts.append((X0, Y0))
    turtle.goto(X0, Y0)
    turtle.pendown()

    NN = N * pow(N - 1, K - 1) - 1

    for I in range(NN + 1):
        I1 = I
        H = 0

        while (I1 % (N - 1) == 0) and (H < (K - 1)):
            I1 = I1 // (N - 1)
            H += 1

        L0 = LL * pow(RA, K - 1 - H)
        A0 = A0 + AA

        X0 = X0 + L0 * math.cos(A0)
        Y0 = Y0 + L0 * math.sin(A0)

        pts.append((X0, Y0))
        turtle.goto(X0, Y0)

    return pts

