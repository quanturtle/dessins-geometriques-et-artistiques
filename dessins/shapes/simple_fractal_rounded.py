import math
import turtle


def draw_rounded_corner(X0: int, 
                        Y0: int, 
                        X1: int, 
                        Y1: int, 
                        X2: int, 
                        Y2: int, 
                        S: int, 
                        I: int):
    UX = X1 - X0
    UY = Y1 - Y0
    WX = X2 - X1
    WY = Y2 - Y1

    for K4 in range(S + 1):
        AN = math.pi / 2 * K4 / S
        CO = math.cos(AN)
        SI = math.sin(AN)
        X = (X0 + X2 + CO * (-WX) + SI * UX) / 2
        Y = (Y0 + Y2 + CO * (-WY) + SI * UY) / 2

        if I == 0 and K4 == 0:
            turtle.penup()
            turtle.goto(int(X), int(Y))
            turtle.pendown()

        else:
            turtle.goto(int(X), int(Y))


def draw_simple_fractal_rounded(M: int = 1,
                                N: int = 7,
                                K: int = 2,
                                S: int = 5,
                                X: list | None = None,
                                Y: list | None = None,
                                L: list | None = None,
                                A: list | None = None) -> None:
    if X is None:
        X = [0, 1]
    if Y is None:
        Y = [480, -480]
    if L is None:
        L = [1/2, 1/4, 1/4, 1/4, 1/4, 1/2, 1/2]
    if A is None:
        A = [0, math.pi / 2, -math.pi, 0, math.pi / 2, -math.pi / 2, 0]
    for II in range(M):
        XD = X[II]
        YD = Y[II]
        XA = X[II + 1]
        YA = Y[II + 1]

        X0 = XD
        X1 = X0
        X2 = X0
        Y0 = YD
        Y1 = Y0
        Y2 = Y0

        if XA != XD:
            A0 = math.atan((YA - YD)/(XA - XD))

        else:
            A0 = math.pi / 2 * math.copysign(1, YA - YD)

        if (XA - XD) < 0:
            A0 += math.pi

        L0 = math.sqrt((XA - XD)**2 + (YA - YD)**2)

        for I in range(0, N**K):
            LL = L0
            AA = A0
            T = I

            for J in range(K - 1, -1, -1):
                R = N**J
                T2 = T // R
                AA += A[T2]
                LL *= L[T2]
                T -= T2 * R

            X0 = X1
            X1 = X2
            X2 = X2 + LL * math.cos(AA)
            Y0 = Y1
            Y1 = Y2
            Y2 = Y2 + LL * math.sin(AA)

            draw_rounded_corner(X0, Y0, X1, Y1, X2, Y2, S, I)