"""Simple fractal designs (designs 115-163) from the book."""

import math

from dessins.shapes import draw_simple_fractal, draw_simple_fractal_deformed, draw_simple_fractal_rounded

from .spec import Design


def deformation_subroutine_153(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)
    else:
        AH = math.pi/2*math.copysign(1, YH)

    AH = AH + math.pi * DH
    DH = pow(DH, 4)

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = (DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_154(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)
    else:
        AH = math.pi/2*math.copysign(1, YH)

    DH = pow(DH, 5)
    AH = AH + math.pi/4 * math.sin(2*math.pi*DH)

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = (DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_155(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

    else:
        AH = math.pi/2*math.copysign(1, YH)

    DH = pow(DH, 6)
    AH = pow(AH, 3)/(math.pi*math.pi)

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = (DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_156(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

    else:
        AH = math.pi/2*math.copysign(1, YH)

    DH = pow(DH, 6)
    AH = 4*AH*AH*AH/(math.pi*math.pi)

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = (DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_157(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

    else:
        AH = math.pi/2*math.copysign(1, YH)

    DH = pow(DH, 5)
    AH = 10*AH

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = (DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_158(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

    else:
        AH = math.pi/2*math.copysign(1, YH)

    DH = pow(DH, 5)
    AH = AH + math.pi/18*math.sin(6*math.pi*DH)

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = (DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_159(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

    else:
        AH = math.pi/2*math.copysign(1, YH)

    DH = pow(DH, 5)
    AH = 20*AH

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = (DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_160(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

    else:
        AH = math.pi/2*math.copysign(1, YH)

    AH = AH / math.pi*AH*math.copysign(1, AH)

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = 2*(DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_161(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

    else:
        AH = math.pi/2*math.copysign(1, YH)

    AH = AH + math.pi/2*(1-DH)

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = 2*(DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_162(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

    else:
        AH = math.pi/2*math.copysign(1, YH)

    DH = pow(DH, 2)

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = 2*(DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


def deformation_subroutine_163(X0: float, Y0: float, NP: int = 480) -> tuple[float, float]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)

    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

    else:
        AH = math.pi/2*math.copysign(1, YH)

    DH = pow(DH, 3)
    AH = AH + math.pi/18*math.sin(6*math.pi / DH)

    X1 = (DH*math.cos(AH) + 1)*NP/2
    Y1 = 2*(DH*math.sin(AH) + 1)*NP/2

    return X1, Y1


DESIGNS: dict[int, Design] = {
    115: Design(draw=draw_simple_fractal, params={"M": 3, "N": 4, "K": 1}, world=(0, 0, 1.1, 1.2)),
    116: Design(draw=draw_simple_fractal, params={"M": 3, "N": 4, "K": 2}, world=(0, 0, 1.1, 1.2)),
    117: Design(draw=draw_simple_fractal, params={"M": 3, "N": 4, "K": 3}, world=(0, 0, 1.1, 1.2)),
    118: Design(draw=draw_simple_fractal, params={"M": 3, "N": 4, "K": 4}),
    119: Design(draw=draw_simple_fractal, params={"M": 3, "N": 4, "K": 5}),
    120: Design(
        draw=draw_simple_fractal,
        params={"M": 3, "N": 4, "K": 2, "X": [480, 0, 480*0.5, 480]},
    ),
    121: Design(
        draw=draw_simple_fractal,
        params={"M": 3, "N": 4, "K": 3, "X": [480, 0, 480*0.5, 480]},
    ),
    122: Design(
        draw=draw_simple_fractal,
        params={"M": 3, "N": 4, "K": 4, "X": [480, 0, 480*0.5, 480]},
    ),
    123: Design(
        draw=draw_simple_fractal,
        params={"M": 3, "N": 4, "K": 5, "X": [480, 0, 480*0.5, 480]},
    ),
    124: Design(
        draw=draw_simple_fractal,
        params={
            "M": 1,
            "N": 3,
            "K": 1,
            "X": [480*0.5, 480*0.5],
            "Y": [480, 0],
            "L": [math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
            "A": [math.pi/4, math.atan(-2), math.pi/4],
        },
    ),
    125: Design(
        draw=draw_simple_fractal,
        params={
            "M": 1,
            "N": 3,
            "K": 2,
            "X": [480*0.5, 480*0.5],
            "Y": [480, 0],
            "L": [math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
            "A": [math.pi/4, math.atan(-2), math.pi/4],
        },
    ),
    126: Design(
        draw=draw_simple_fractal,
        params={
            "M": 1,
            "N": 3,
            "K": 3,
            "X": [480*0.5, 480*0.5],
            "Y": [480, 0],
            "L": [math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
            "A": [math.pi/4, math.atan(-2), math.pi/4],
        },
    ),
    127: Design(
        draw=draw_simple_fractal,
        params={
            "M": 1,
            "N": 3,
            "K": 4,
            "X": [480*0.5, 480*0.5],
            "Y": [480, 0],
            "L": [math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
            "A": [math.pi/4, math.atan(-2), math.pi/4],
        },
    ),
    128: Design(
        draw=draw_simple_fractal,
        params={
            "M": 1,
            "N": 3,
            "K": 5,
            "X": [480*0.5, 480*0.5],
            "Y": [480, 0],
            "L": [math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
            "A": [math.pi/4, math.atan(-2), math.pi/4],
        },
    ),
    129: Design(
        draw=draw_simple_fractal,
        params={
            "M": 1,
            "N": 3,
            "K": 6,
            "X": [480*0.5, 480*0.5],
            "Y": [480, 0],
            "L": [math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
            "A": [math.pi/4, math.atan(-2), math.pi/4],
        },
    ),
    130: Design(
        draw=draw_simple_fractal,
        params={
            "M": 1,
            "N": 3,
            "K": 7,
            "X": [480*0.5, 480*0.5],
            "Y": [480, 0],
            "L": [math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
            "A": [math.pi/4, math.atan(-2), math.pi/4],
        },
    ),
    131: Design(
        draw=draw_simple_fractal,
        params={
            "M": 1,
            "N": 3,
            "K": 8,
            "X": [480*0.5, 480*0.5],
            "Y": [480, 0],
            "L": [math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
            "A": [math.pi/4, math.atan(-2), math.pi/4],
        },
    ),
    132: Design(
        draw=draw_simple_fractal,
        params={
            "M": 4,
            "N": 4,
            "K": 5,
            "X": [0, 480, 480, 0, 0],
            "Y": [0, 0, 480, 480, 0],
            "L": [1/(2+ 2 * math.cos(0.45 * math.pi))]*4,
            "A": [0, 0.45*math.pi, -0.45*math.pi, 0],
        },
    ),
    133: Design(
        draw=draw_simple_fractal,
        params={
            "M": 4,
            "N": 4,
            "K": 6,
            "X": [0, 480, 480, 0, 0],
            "Y": [0, 0, 480, 480, 0],
            "L": [1/(2+ 2 * math.cos(.48*math.pi))]*4,
            "A": [0, 0.48*math.pi, -0.48*math.pi, 0],
        },
    ),
    134: Design(
        draw=draw_simple_fractal,
        params={
            "M": 1,
            "N": 4,
            "K": 6,
            "X": [0, 0],
            "Y": [480, -480],
            "L": [1/3, 1/3, math.sqrt(10)/9, 5/9],
            "A": [0, math.pi/2, -math.atan(3), 0],
        },
    ),
    135: Design(
        draw=draw_simple_fractal,
        params={
            "M": 2,
            "N": 2,
            "K": 12,
            "X": [480/2, 480/2, 480/2],
            "Y": [480*.25, 480*.75, 480*.25],
            "L": [1/math.sqrt(2), 1/math.sqrt(2)],
            "A": [math.pi/4, -math.pi/4],
        },
    ),
    136: Design(
        draw=draw_simple_fractal_rounded,
        params={"M": 1, "N": 7, "K": 1, "S": 20},
        world=(-1, -1, 1, 1),
    ),
    137: Design(draw=draw_simple_fractal_rounded, params={"M": 1, "N": 7, "K": 2, "S": 10}),
    138: Design(draw=draw_simple_fractal_rounded, params={"M": 1, "N": 7, "K": 3, "S": 5}),
    139: Design(draw=draw_simple_fractal_rounded, params={"M": 1, "N": 7, "K": 4, "S": 5}),
    140: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 2,
            "N": 4,
            "K": 1,
            "S": 10,
            "X": [0, 480, 0],
            "Y": [480, 0, 480],
            "L": [0.5, 0.45, 0.45, 0.5],
            "A": [0, math.pi/2, -math.pi/2, 0],
        },
    ),
    141: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 2,
            "N": 4,
            "K": 2,
            "S": 5,
            "X": [0, 480, 0],
            "Y": [480, 0, 480],
            "L": [0.5, 0.45, 0.45, 0.5],
            "A": [0, math.pi/2, -math.pi/2, 0],
        },
    ),
    142: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 2,
            "N": 4,
            "K": 3,
            "S": 4,
            "X": [0, 480, 0],
            "Y": [480, 0, 480],
            "L": [0.5, 0.45, 0.45, 0.5],
            "A": [0, math.pi/2, -math.pi/2, 0],
        },
    ),
    143: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 2,
            "N": 4,
            "K": 4,
            "S": 3,
            "X": [0, 480, 0],
            "Y": [480, 0, 480],
            "L": [0.5, 0.45, 0.45, 0.5],
            "A": [0, math.pi/2, -math.pi/2, 0],
        },
    ),
    144: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 2,
            "N": 4,
            "K": 5,
            "S": 3,
            "X": [0, 480, 0],
            "Y": [480, 0, 480],
            "L": [0.5, 0.45, 0.45, 0.5],
            "A": [0, math.pi/2, -math.pi/2, 0],
        },
    ),
    145: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 1,
            "N": 13,
            "K": 1,
            "S": 8,
            "X": [0, 480],
            "Y": [480, 0],
            "L": [0.4, 0.4, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2, 0.2, 0.2],
            "A": [0, math.pi/2, 0, -math.pi/2, 0, -math.pi/2, -math.pi, -math.pi/2, 0, math.pi/2, 0, math.pi/2, 0],
        },
    ),
    146: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 1,
            "N": 13,
            "K": 2,
            "S": 4,
            "X": [0, 480],
            "Y": [480, 0],
            "L": [0.4, 0.4, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2, 0.2, 0.2],
            "A": [0, math.pi/2, 0, -math.pi/2, 0, -math.pi/2, -math.pi, -math.pi/2, 0, math.pi/2, 0, math.pi/2, 0],
        },
    ),
    147: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 1,
            "N": 13,
            "K": 3,
            "S": 3,
            "X": [0, 480],
            "Y": [480, 0],
            "L": [0.4, 0.4, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2, 0.2, 0.2],
            "A": [0, math.pi/2, 0, -math.pi/2, 0, -math.pi/2, -math.pi, -math.pi/2, 0, math.pi/2, 0, math.pi/2, 0],
        },
    ),
    148: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 2,
            "N": 8,
            "K": 1,
            "S": 8,
            "X": [0, 480, 0],
            "Y": [480, 0, 480],
            "L": [0.4, 0.2*math.sqrt(2), 0.2, 0.2, 0.2, 0.2, 0.2*math.sqrt(2), 0.2],
            "A": [0, math.pi/4, math.pi/2, math.pi, -math.pi/2, 0, -math.pi/4, 0],
        },
    ),
    149: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 2,
            "N": 8,
            "K": 2,
            "S": 4,
            "X": [0, 480, 0],
            "Y": [480, 0, 480],
            "L": [0.4, 0.2*math.sqrt(2), 0.2, 0.2, 0.2, 0.2, 0.2*math.sqrt(2), 0.2],
            "A": [0, math.pi/4, math.pi/2, math.pi, -math.pi/2, 0, -math.pi/4, 0],
        },
    ),
    150: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 2,
            "N": 8,
            "K": 3,
            "S": 3,
            "X": [0, 480, 0],
            "Y": [480, 0, 480],
            "L": [0.4, 0.2*math.sqrt(2), 0.2, 0.2, 0.2, 0.2, 0.2*math.sqrt(2), 0.2],
            "A": [0, math.pi/4, math.pi/2, math.pi, -math.pi/2, 0, -math.pi/4, 0],
        },
    ),
    151: Design(
        draw=draw_simple_fractal_rounded,
        params={
            "M": 2,
            "N": 8,
            "K": 4,
            "S": 1,
            "X": [0, 480, 0],
            "Y": [480, 0, 480],
            "L": [0.4, 0.2*math.sqrt(2), 0.2, 0.2, 0.2, 0.2, 0.2*math.sqrt(2), 0.2],
            "A": [0, math.pi/4, math.pi/2, math.pi, -math.pi/2, 0, -math.pi/4, 0],
        },
    ),
    152: Design(draw=draw_simple_fractal_deformed),
    153: Design(
        draw=draw_simple_fractal_deformed,
        params={"M": 3, "N": 4, "K": 5, "deformation_func": deformation_subroutine_153},
    ),
    154: Design(
        draw=draw_simple_fractal_deformed,
        params={"M": 3, "N": 4, "K": 4, "deformation_func": deformation_subroutine_154},
    ),
    155: Design(
        draw=draw_simple_fractal_deformed,
        params={"M": 3, "N": 4, "K": 5, "deformation_func": deformation_subroutine_155},
    ),
    156: Design(
        draw=draw_simple_fractal_deformed,
        params={"M": 3, "N": 4, "K": 5, "deformation_func": deformation_subroutine_156},
    ),
    157: Design(
        draw=draw_simple_fractal_deformed,
        params={"M": 3, "N": 4, "K": 5, "deformation_func": deformation_subroutine_157},
    ),
    158: Design(
        draw=draw_simple_fractal_deformed,
        params={"M": 3, "N": 4, "K": 5, "deformation_func": deformation_subroutine_158},
    ),
    159: Design(
        draw=draw_simple_fractal_deformed,
        params={"M": 3, "N": 4, "K": 5, "deformation_func": deformation_subroutine_159},
    ),
    160: Design(
        draw=draw_simple_fractal_deformed,
        params={
            "M": 4,
            "N": 4,
            "K": 4,
            "X": [480/2*(1+5/6*math.cos(2*i*math.pi/4+math.pi/4)) for i in range(4+1)],
            "Y": [480/2*(1+5/6*math.sin(2*i*math.pi/4+math.pi/4)) for i in range(4+1)],
            "L": [1/(2+2*math.cos(0.48*math.pi))] * 4,
            "A": [0, 0.48*math.pi, -0.48*math.pi, 0][:4],
            "deformation_func": deformation_subroutine_160,
        },
    ),
    161: Design(
        draw=draw_simple_fractal_deformed,
        params={
            "M": 4,
            "N": 4,
            "K": 4,
            "X": [480/2*(1+5/6*math.cos(2*i*math.pi/4+math.pi/4)) for i in range(4+1)],
            "Y": [480/2*(1+5/6*math.sin(2*i*math.pi/4+math.pi/4)) for i in range(4+1)],
            "L": [1/(2+2*math.cos(0.48*math.pi))] * 4,
            "A": [0, 0.48*math.pi, -0.48*math.pi, 0][:4],
            "deformation_func": deformation_subroutine_161,
        },
    ),
    162: Design(
        draw=draw_simple_fractal_deformed,
        params={
            "M": 4,
            "N": 4,
            "K": 4,
            "X": [480/2*(1+5/6*math.cos(2*i*math.pi/4+math.pi/4)) for i in range(4+1)],
            "Y": [480/2*(1+5/6*math.sin(2*i*math.pi/4+math.pi/4)) for i in range(4+1)],
            "L": [1/(2+2*math.cos(0.48*math.pi))] * 4,
            "A": [0, 0.48*math.pi, -0.48*math.pi, 0][:4],
            "deformation_func": deformation_subroutine_162,
        },
    ),
    163: Design(
        draw=draw_simple_fractal_deformed,
        params={
            "M": 4,
            "N": 4,
            "K": 4,
            "X": [480/2*(1+5/6*math.cos(2*i*math.pi/4+math.pi/4)) for i in range(4+1)],
            "Y": [480/2*(1+5/6*math.sin(2*i*math.pi/4+math.pi/4)) for i in range(4+1)],
            "L": [1/(2+2*math.cos(0.48*math.pi))] * 4,
            "A": [0, 0.48*math.pi, -0.48*math.pi, 0][:4],
            "deformation_func": deformation_subroutine_163,
        },
    ),
}
