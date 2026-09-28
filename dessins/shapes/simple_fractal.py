import math
import turtle


def draw_simple_fractal(
    M: int = 3,
    N: int = 4,
    K: int = 4,
    X: list[float] | None = None,
    Y: list[float] | None = None,
    L: list[float] | None = None,
    A: list[float] | None = None,
    translateX: float = 0.0,
    translateY: float = 0.0,
) -> None:
    if X is None:
        X = [0, 480, 480 * 0.5, 0]
    if Y is None:
        Y = [math.sqrt(3) / 2 * 480, math.sqrt(3) / 2 * 480, 0, math.sqrt(3) / 2 * 480]
    if L is None:
        L = [1 / 3, 1 / 3, 1 / 3, 1 / 3]
    if A is None:
        A = [0, math.pi / 3, -math.pi / 3, 0]
    for II in range(M):
        XD = X[II]
        YD = Y[II]
        XA = X[II + 1]
        YA = Y[II + 1]

        X0 = XD
        Y0 = YD

        turtle.goto(int(X0 + translateX), int(Y0 + translateY))
        turtle.pendown()

        A0 = math.atan2(YA - YD, XA - XD)
        L0 = math.sqrt((XA - XD) ** 2 + (YA - YD) ** 2)

        for I in range(N**K):
            LL = L0
            AA = A0

            T1 = I

            if K == 0:
                X0 += LL * math.cos(AA)
                Y0 += LL * math.sin(AA)
                turtle.goto(int(X0 + translateX), int(Y0 + translateY))

            else:
                for J in range(K - 1, -1, -1):
                    R_val = N ** J
                    T2 = T1 // R_val
                    AA += A[T2]
                    LL *= L[T2]
                    T1 -= T2 * R_val

                X0 += LL * math.cos(AA)
                Y0 += LL * math.sin(AA)
                turtle.goto(int(X0 + translateX), int(Y0 + translateY))

