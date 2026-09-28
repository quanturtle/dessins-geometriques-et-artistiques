"""Designs drawn from data tables (designs 34-49) from the book."""

import math
import turtle

from dessins.shapes import draw_bird_fish, draw_horse, draw_lion, draw_smurf

from .spec import Design

HORSE_DATA = [
    1000, 10,10, 8,12, 9,16, 12,17, 13,18, 14,20,
    1000, 13,18, 12,19, 9,21, 9,20, 10,19, 9,17, 7,20, 8,22, 12,22,
    1000, 12,20, 12,22, 13,26, 16,31, 18,31, 19,32,
    1000, 16,31, 14,31, 14,32,
    1000, 14,31, 10,30, 12,31, 10,32, 10,34, 11,34, 11,33, 10,33,
    1000, 12,32, 13,31,
    1000, 10,34, 16,36,
    1000, 16,35, 16,37, 18,35, 17,34,
    1000, 17,36, 20,36, 22,32, 19,26,
    1000, 20,36, 22,36, 22,34, 24,32, 24,30, 19,26, 18,23, 21,22, 21,24,
    30,30, 34,31, 36,31, 33,26, 32,22, 28, 22, 27,20, 29,17, 30,19, 29,20,
    29,21, 32,19, 33,18, 32,17, 29,16, 28, 12, 30,10, 21,4, 21,2,
    18,3, 19,6, 24,10, 24,12, 22,14, 22,16, 23,17,
    1000, 22,16, 17,16, 16,17, 17,18,
    1000, 16,17, 16,16, 10,14, 10,12, 12,11, 10,10,
    1000, 21,21, 22,24, 30,30,
    1000, 24,24, 34,28,
    1000, 25,23, 33,26,
    1000, 25,21, 27,20,
    1000, 23,21, 24,19,
    1000, 27,20, 22,19, 22,21,
    1000, 22,19, 21,20,
    1000, 13,34, 15,35, 16,34, 16,33,
    1000, 15,35, 15,34, 16,34, 15,34, 15,35,
    1000, 24,12, 26,10, 19,5, 19,3,
    1000, 28,22, 25,22,
    2000
]


def sgn(x: float) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def design_35(NP: int = 480) -> None:
    i = 0
    B1 = 0

    for I in range(6):
        AN = 2 * I * math.pi / 6 + math.pi / 12
        CO = math.cos(AN)
        SI = math.sin(AN)

        while True:
            A = HORSE_DATA[i % len(HORSE_DATA)]
            i += 1

            if A == 2000:
                break

            if A == 1000:
                B1 = 0
                A = HORSE_DATA[i % len(HORSE_DATA)]
                i += 1
                B = HORSE_DATA[i % len(HORSE_DATA)]
                i += 1

            else:
                B = HORSE_DATA[i % len(HORSE_DATA)]
                i += 1

            X = int(NP * (0.5 + CO * A/90.0 - SI * B/90.0))
            Y = int(NP * (0.5 + SI * A/90.0 + CO * B/90.0))

            if B1 == 0:
                turtle.penup()
                turtle.goto(X - NP // 2, Y - NP // 2)
                B1 = 1

            else:
                turtle.pendown()
                turtle.goto(X - NP // 2, Y - NP // 2)


def design_36(NP: int = 480) -> None:
    i = 0
    B1 = 0

    for I in range(6):
        for J in range(2):
            while True:
                A = HORSE_DATA[i % len(HORSE_DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1
                    B = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1

                else:
                    B = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1

                X = int(NP/2 + (1-2*J) * NP*A/80 * (0.5**I))
                Y = int(NP - NP*0.5**I + NP*B/80 * (0.5**I))

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1

                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)


def design_37(NP: int = 480) -> None:
    i = 0
    B1 = 0

    for I in range(16):
        i = 0
        B1 = 0

        while True:
            A = HORSE_DATA[i]
            i += 1

            if A == 2000:
                break

            if A == 1000:
                B1 = 0
                A = HORSE_DATA[i]
                i += 1

            B = HORSE_DATA[i]
            i += 1

            AN = 2.0 * I * math.pi / 6.0 + math.pi / 12.0
            CO = math.cos(AN)
            SI = math.sin(AN)
            R = (0.87) ** I

            X_ = 0.15 + A / 110.0
            Y_ = 0.15 + B / 110.0

            X = int(NP * (0.5 + R * (CO * X_ - SI * Y_)))
            Y = int(NP * (0.5 + R * (SI * X_ + CO * Y_)))

            if B1 == 0:
                turtle.penup()
                turtle.goto(X, Y)
                B1 = 1

            else:
                turtle.pendown()
                turtle.goto(X, Y)


def design_38(NP: int = 480) -> None:
    i = 0
    B1 = 0

    for I in range(6):
        for J in range(2**I-1):
            while True:
                A = HORSE_DATA[i % len(HORSE_DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1
                    B = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1

                else:
                    B = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1

                X = int((J+A/20) * NP*(0.5**I))
                Y = int((2-2*.5**I) * NP+B/40 * NP*(0.5**I))

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1

                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)


def design_39(NP: int = 480) -> None:
    i = 0
    B1 = 0

    for I in range(3):
        for J in range(3):
            while True:
                A = HORSE_DATA[i % len(HORSE_DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1
                    B = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1

                else:
                    B = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1

                X = int(NP * (A+J*20) / 80)
                Y = int(NP * (B+I*20) / 80)

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1

                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)


def design_40(NP: int = 480) -> None:
    i = 0
    B1 = 0

    N = 4
    for I in range(-N, N+1):
        for J in range(-abs(I), abs(I)+1):
            while True:
                A = HORSE_DATA[i % len(HORSE_DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1
                    B = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1

                else:
                    B = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1

                XX = (A+ J*20 -20) / 100
                YY = (B+ I*20 -20) / 100

                X = int(NP/2 * (XX+1))
                Y = int(NP/2 * (YY+1))

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1

                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)


def design_41(NP: int = 480) -> None:
    N = 4

    for I in range(-N, N + 1):
        for J in range(-N, N + 1):
            i = 0

            while True:
                A = HORSE_DATA[i % len(HORSE_DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = HORSE_DATA[i % len(HORSE_DATA)]
                    i += 1

                B = HORSE_DATA[i % len(HORSE_DATA)]
                i += 1

                XX = (A + J * 20 - 20) / 100.0
                YY = (B + I * 20 - 20) / 100.0

                X = int((XX * abs(XX) + 1) * NP / 2)
                Y = int((YY * abs(YY) + 1) * NP / 2)

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1

                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)


def design_42(NP: int = 480) -> None:
    N = 4

    for I in range(-N, N + 1):
        for J in range(-N, N + 1):
            i = 0
            B1 = 0

            while True:
                A = HORSE_DATA[i]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = HORSE_DATA[i]
                    i += 1

                B = HORSE_DATA[i]
                i += 1

                X_ = NP * (A + J * 20 - 20) / 80.0
                Y_ = NP * (B + I * 20 - 20) / 80.0

                DI = math.sqrt(X_ ** 2 + Y_ ** 2)

                if X_ != 0:
                    AN = math.atan(Y_ / X_) + math.pi * (1 - sgn(X_)) / 2

                else:
                    AN = (math.pi / 2) * sgn(Y_)

                DI = (DI / NP) * 3.0
                DI = DI / (1 + DI) * NP * 0.65

                X = int(NP / 2 + DI * math.cos(AN))
                Y = int(NP / 2 + DI * math.sin(AN))

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X, Y)
                    B1 = 1

                else:
                    turtle.pendown()
                    turtle.goto(X, Y)


def design_43(NP: int = 480) -> None:
    N = 4

    for I in range(-N, N + 1):
        for J in range(-N, N + 1):
            i = 0
            B1 = 0

            while True:
                A = HORSE_DATA[i]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = HORSE_DATA[i]
                    i += 1

                B = HORSE_DATA[i]
                i += 1

                XX = (A + J * 20 - 20) / 100.0
                YY = (B + I * 20 - 20) / 100.0

                X_val = (abs(XX) ** 0.7) * sgn(XX) + 1
                Y_val = (abs(YY) ** 0.7) * sgn(YY) + 1

                X = int(X_val * NP / 2)
                Y = int(Y_val * NP / 2)

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1

                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)


LION_DATA = [
        1000, -2.5,0, -2,1, - 1,2, 0,7, 1,7, 2,8, 2,11, 3,14, 3.5,13.5,2.5,11, 2.5,9,
        1000, 3.5,13.5, 4,13, 3,11, 3,9, 3,11, 4,13, 5,12, 3.5,11, 3.5,9,3.5,11, 5,12, 5,11, 4,10, 4,9,8,9, 7,11, 8,13, 10,14, 12,13, 13, 11, 12, 11,11,10, 12,8, 13,7, 14,2,15,2, 16,1, 16,0, 12,0, 12,2, 11,5, 11.5,6, 11,5, 9,3, 9,2, 10,1,10,0, 6,0, 7,2, 8,6, 7,2, 6,4, 4,5, 5,7, 4,8,5,7, 4,5, 2,4, 1,2, 2,2, 3,1, 2.5,0, -2.5,0,
        1000, 6,4, 7.5,3.5,
        1000, 12,11, 10,10.5, 9,10.5,
        1000, 12.5,12, 12,12, 11,11.5,12,12, 12,12.5, 11.5,12.5, 10.5,13,10, 13, 10,13.5, 10.5,13.5, 10.5,13, 11.5,12.5,12,12.5, 12,13,
        1000,7.5,12, 8.5,12, 8.5,11.5,
        2000
    ]


def design_45(NP: int = 480) -> None:
    i  = 0
    B1 = 0

    for I in range(5):
        for J in range(3):
            while True:
                A = LION_DATA[i % len(LION_DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0

                    A = LION_DATA[i % len(LION_DATA)]
                    i += 1

                    B = LION_DATA[i % len(LION_DATA)]
                    i += 1

                else:
                    B = LION_DATA[i % len(LION_DATA)]
                    i += 1

                X = int(NP*(7+(1-2*(I%2))*(7-A)+4+14*J)/50)
                Y = int(NP*(4.5+(1-2*(J%2))*(4.5-B)+4+9*I)/50)

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X, Y)
                    B1 = 1

                else:
                    turtle.pendown()
                    turtle.goto(X, Y)


BIRD_FISH_DATA = [
        1000,0,0, 2,0, 4,1, 4,2, 3,2, 2,3, 4,5, 4,6, 2,5, 2,6, -1,5, -2,3, -1,2, -2,2, -3,3, -4,3, -5,2, -4,2, 0,0,
        1000,-5,2, -5,1, -7,-1, -6,-2, -5,-2, -5,-3, -2,-2, -2,-3, 0,-2, 1,-1, 2, -1, 3,-2, 4,-2, 3,-1, 4,1,
        1000, 2,5, 0,4, 0,2,
        1000, -2,1, -5,1, -4,-1, -3,0, -3,-1, -4,-1, -5,-2, 0,-2,
        1000, -7,-1, -6,-1,
        1000,-4,2.5, -4,2.8, -4.3,2.8, -4.3,2.5, -4,2.5,
        1000, -5,0, -5.5,0, -5.5,0.5, -5,0.5,  -5,0,
        2000
    ]


def design_47(NP: int = 480) -> None:
    i  = 0
    B1 = 0

    for I in range(5):
        for J in range(5):
            while True:
                A = BIRD_FISH_DATA[i % len(BIRD_FISH_DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = BIRD_FISH_DATA[i % len(BIRD_FISH_DATA)]
                    i += 1

                    B = BIRD_FISH_DATA[i % len(BIRD_FISH_DATA)]
                    i += 1

                else:
                    B = BIRD_FISH_DATA[i % len(BIRD_FISH_DATA)]
                    i += 1

                X = int(NP*(B+4*I+4*J)/45)
                Y = int(NP*(A+15-5*I+9*J)/45)

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X, Y)
                    B1 = 1

                else:
                    turtle.pendown()
                    turtle.goto(X, Y)


SMURF_DATA = [
    1000,
    12,12, 14,8, 14,4, 12,2, 8,2,
    4,4, 0,10, 0,20, 4,26, 6,28, 12,28,
    14,26, 14,22, 12,16, 12,12, 20,14,
    24,14, 28,12, 28,10, 26,4, 28,0,
    36,0, 38,2, 40,10, 40,22, 36,26, 28,26, 26,22, 28,14, 28,12, 28,14,
    27,18, 18,18, 16,20, 16,18, 20,14,
    16,18, 12,16,
    1000, 16,20, 16,24, 20,32, 20,34, 20,32, 12,34, 12,32, 10,28,
    1000, 4,26, 2,28, 4,30, 8,30, 6,32, 6,34, 6,32, 4,32, 2,30, 2,28,
    1000, 8,30, 8,36, 10,38, 1000, 4,32, 4,34, 8,38, 6,40, 6,42, 8,44, 10,44, 10,42, 12,42, 12,38, 16,36, 32,36, 38,40, 40,44, 38,42, 36,46, 30,48, 36,48, 40,44, 40,56, 36,62, 32,64, 24,64, 18,62, 16,60, 16,58, 18,56, 24,56, 22,56,20,53, 28,56, 22,54, 28,54, 32,52, 34,48, 32,52, 28,48, 30,46, 28,44, 1000, 28,48, 22,48, 24,48, 24,52, 22,54, 18,52, 18,50, 20,48, 12,48, 16,48, 18,50, 16,48, 16,50, 18,52, 16,50, 16,48, 14,46, 16,44,
    1000, 12,48, 10,44,
    1000, 16,46, 18,44,
    1000, 18,46, 26,46, 24,46, 24,44, 22,42, 20,44, 20,46,
    1000, 22,42, 22,44, 24,44,
    1000, 28,46, 26,44,
    1000, 24,54, 25,52,
    1000, 27,52, 28,54, 30,52,
    1000, 25,49, 26,50, 27,49,
    1000, 36,38, 40,38, 42,40, 48,40, 48,42, 50,42, 52,40, 50,36, 48,36, 48,38, 48,38, 48,36, 46,34, 48,36, 48,26, 46,24, 46,32, 46,30, 42,30, 44,28, 44,26, 42,24, 40,26, 40,32, 42,32, 28,32, 30,32, 32,26,
    1000, 44,26, 44,24, 46,24,
    1000, 42,38, 44,36, 44,32,
    2000
]


def design_49(NP: int = 480) -> None:
    i = 0
    B1 = 0

    turtle.penup()
    turtle.goto(NP/25, NP/25)

    for I in range(8):
        K = 0.5**I

        while True:
            A = SMURF_DATA[i % len(SMURF_DATA)]
            i += 1

            if A == 2000:
                break

            if A == 1000:
                B1 = 0
                A = SMURF_DATA[i % len(SMURF_DATA)]
                i += 1

                B = SMURF_DATA[i % len(SMURF_DATA)]
                i += 1

            else:
                B = SMURF_DATA[i % len(SMURF_DATA)]
                i += 1

            X = int(NP/100*A*K + NP - NP*K)
            Y = int(NP/100*B*K)

            if B1 == 0:
                B1 = 1
                turtle.penup()
                turtle.goto(X, Y)

            if B1 == 1:
                turtle.pendown()
                turtle.goto(X, Y)


DESIGNS: dict[int, Design] = {
    34: Design(draw=draw_horse),
    35: Design(draw=design_35, world=(-1, -1, 1, 1)),
    36: Design(draw=design_36, world=(-1, -1, 1, 1)),
    37: Design(draw=design_37, world=(-1, -1, 1, 1)),
    38: Design(draw=design_38, world=(-0.5, -0.5, 1.5, 1.5)),
    39: Design(draw=design_39, world=(-1, -1, 1, 1)),
    40: Design(draw=design_40, world=(-1, -1, 1, 1)),
    41: Design(draw=design_41, world=(-1, -1, 1, 1)),
    42: Design(draw=design_42),
    43: Design(draw=design_43),
    44: Design(draw=draw_lion),
    45: Design(draw=design_45, world=(0, 0, 1.1, 1.2)),
    46: Design(draw=draw_bird_fish, world=(-1.3, -1.3, 1.3, 1.3)),
    47: Design(draw=design_47, world=(-1.3, -1.3, 1.3, 1.3)),
    48: Design(draw=draw_smurf),
    49: Design(draw=design_49),
}
