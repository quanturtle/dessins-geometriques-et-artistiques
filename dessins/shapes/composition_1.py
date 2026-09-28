import math

from .regular_star import draw_regular_star


def draw_composition_1(
    K1: int = 5,
    DX: float = 240,
    DY: float = 240,
    R1: float = 480 * 0.27,
    A1: float = math.pi / 2,
    K: int = 25,
    H: int = 12,
    R: float = 480 * 0.22,
    AD: float = math.pi / 2,
    NP: int = 480,
) -> None:
    for I1 in range(K1):
        CX = DX + R1 * math.cos(2 * math.pi * I1 / K1 + A1)
        CY = DY + R1 * math.sin(2 * math.pi * I1 / K1 + A1)
        # TODO: scale CY by 1.5 to get last composition (design_19)

        draw_regular_star(CX, CY, K, H, R, AD)

