import math
import turtle
from typing import Callable, Optional


def sgn(x: float) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def default_compute_z(x: float, y: float, NP: int) -> float:
    return NP / 3 * math.sin(math.pi * y) * math.sin(math.pi * x)


def draw_surface(
    N: int = 6,
    PA: Optional[float] = None,
    E1: int = 2,
    E2: int = 1,
    E3: int = 0,
    NP: int = 480,
    XA: float = None,
    YA: float = None,
    XB: float = None,
    YB: float = None,
    XC: float = None,
    YC: float = None,
    XD: float = None,
    YD: float = None,
    compute_z: Callable = default_compute_z,
    translate_x: float = 0.0,
    translate_y: float = 0.0,
) -> None:
    if PA is None:
        PA = NP / 16
    if XA is None:
        XA = NP / 2
    if YA is None:
        YA = NP / 16
    if XB is None:
        XB = NP * 7 / 8
    if YB is None:
        YB = NP / 4
    if XC is None:
        XC = NP / 2
    if YC is None:
        YC = NP * 5 / 8
    if XD is None:
        XD = NP / 8
    if YD is None:
        YD = NP * 7 / 16

    M = int(NP / PA)
    MA = [-5 * NP] * (M + 1)
    MI = [5 * NP] * (M + 1)

    X = Y = Z = 0.0

    while True:
        for I in range(M + 1):
            MA[I] = -5 * NP
            MI[I] = 5 * NP

        for I in range(N + 1):
            XP = (I * XD + (N - I) * XA) / N
            YP = (I * YD + (N - I) * YA) / N
            XQ = (I * XC + (N - I) * XB) / N
            YQ = (I * YC + (N - I) * YB) / N

            if E3 == 1:
                Y = I / N
            else:
                X = I / N

            I1 = int(XP / PA)
            I2 = int(XQ / PA)
            G = sgn(I2 - I1)

            if G == 0:
                continue

            J = I1
            while (G > 0 and J <= I2) or (G < 0 and J >= I2):
                skip = False

                if E3 == 1:
                    X = (J - I1) / (I2 - I1) if I2 != I1 else 0
                else:
                    Y = (J - I1) / (I2 - I1) if I2 != I1 else 0

                Z = compute_z(X, Y, NP)

                XF = int(J * PA)

                if I2 != I1:
                    YF = int(((J - I1) * YQ + (I2 - J) * YP) / (I2 - I1) + Z)
                else:
                    YF = int(YP + Z)

                XF_t = XF + translate_x
                YF_t = YF + translate_y

                if 0 <= J <= M:
                    if J == I1:
                        turtle.penup()
                        turtle.goto(XF_t, YF_t)

                    elif E2 == 1:
                        turtle.pendown()
                        turtle.goto(XF_t, YF_t)

                        skip = True

                    elif not skip:
                        if YF > MI[J] and YF < MA[J]:
                            turtle.penup()
                            turtle.goto(XF_t, YF_t)
                        else:
                            if YF > MA[J]:
                                MA[J] = YF

                            if YF < MI[J]:
                                MI[J] = YF

                            turtle.pendown()
                            turtle.goto(XF_t, YF_t)

                J += G

        if E1 == 1:
            break

        E3 = 1
        E1 = 1

        XD, XB = XB, XD
        YD, YB = YB, YD

