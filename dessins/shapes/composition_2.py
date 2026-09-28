import math

from .regular_star import draw_regular_star


def draw_composition_2(
    K1: int = 8,
    N: int = 32,
    K: int = 16,
    H: int = 5,
    R1: float = 480 * 0.36,
    R: float = 480 * 0.14,
    RR: float = 0.9,
    DX: float = 240,
    DY: float = 240,
    NP: int = 480,
) -> None:
    for I1 in range(N):
        R2 = R1 * (RR ** I1)
        R3 = R * (RR ** I1)

        CX = DX + R2 * math.cos(2 * math.pi * I1 / K1)
        CY = DY + R2 * math.sin(2 * math.pi * I1 / K1)

        draw_regular_star(CX, CY, K, H, R3, 0)

