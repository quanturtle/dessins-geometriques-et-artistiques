"""Polygon and star designs (designs 1-33) from the book."""

import math

from dessins.shapes import (
    draw_composition_1,
    draw_composition_2,
    draw_prettygon,
    draw_regular_polygon,
    draw_regular_star,
)

from .spec import Design

DESIGNS: dict[int, Design] = {
    1: Design(
        draw=draw_regular_polygon,
        params={"CX": 240, "CY": 240, "K": 4, "R": 480*0.45, "AD": math.pi/4, "NP": 480},
    ),
    2: Design(
        draw=draw_regular_polygon,
        params={"CX": 240, "CY": 240, "K": 3, "R": 480*0.45, "AD": 0, "NP": 480},
    ),
    3: Design(
        draw=draw_regular_polygon,
        params={"CX": 240, "CY": 240, "K": 3, "R": 480*0.45, "AD": math.pi/2, "NP": 480},
    ),
    4: Design(
        draw=draw_regular_polygon,
        params={"CX": 240, "CY": 240, "K": 5, "R": 480*0.45, "AD": math.pi/2, "NP": 480},
    ),
    5: Design(
        draw=draw_regular_polygon,
        params={"CX": 240, "CY": 240, "K": 8, "R": 480*0.5, "AD": math.pi/8, "NP": 480},
    ),
    6: Design(
        draw=draw_regular_polygon,
        params={"CX": 240, "CY": 240, "K": 20, "R": 480*0.4, "AD": 0, "NP": 480},
    ),
    7: Design(
        draw=draw_regular_star,
        params={"CX": 240, "CY": 240, "K": 5, "H": 3, "R": 480*0.45, "AD": math.pi/2},
    ),
    8: Design(
        draw=draw_regular_star,
        params={"CX": 240, "CY": 240, "K": 7, "H": 3, "R": 480*0.45, "AD": math.pi/2},
    ),
    9: Design(
        draw=draw_regular_star,
        params={"CX": 240, "CY": 240, "K": 20, "H": 9, "R": 480*0.45, "AD": math.pi/2},
    ),
    10: Design(
        draw=draw_regular_star,
        params={"CX": 240, "CY": 240, "K": 20, "H": 7, "R": 480*0.45, "AD": math.pi/2},
    ),
    11: Design(
        draw=draw_regular_star,
        params={"CX": 240, "CY": 240, "K": 51, "H": 20, "R": 480*0.45, "AD": math.pi/2},
    ),
    12: Design(
        draw=draw_regular_star,
        params={"CX": 240, "CY": 240, "K": 51, "H": 25, "R": 480*0.45, "AD": math.pi/2},
    ),
    13: Design(
        draw=draw_composition_1,
        params={
            "K1": 5,
            "DX": 240,
            "DY": 240,
            "R1": 480*0.27,
            "A1": math.pi/2,
            "K": 25,
            "H": 12,
            "R": 480*0.22,
            "AD": math.pi/2,
            "NP": 480,
        },
    ),
    14: Design(
        draw=draw_composition_1,
        params={
            "K1": 6,
            "DX": 240,
            "DY": 240,
            "R1": 480*0.2,
            "A1": 0,
            "K": 24,
            "H": 11,
            "R": 480*0.3,
            "AD": 0,
            "NP": 480,
        },
    ),
    15: Design(
        draw=draw_composition_1,
        params={
            "K1": 40,
            "DX": 240,
            "DY": 240,
            "R1": 480*0.25,
            "A1": math.pi/2,
            "K": 80,
            "H": 1,
            "R": 480*0.25,
            "AD": math.pi/2,
            "NP": 480,
        },
    ),
    16: Design(
        draw=draw_composition_1,
        params={
            "K1": 10,
            "DX": 240,
            "DY": 240,
            "R1": 480*0.35,
            "A1": math.pi/2,
            "K": 10,
            "H": 3,
            "R": 480*0.15,
            "AD": 0,
            "NP": 480,
        },
    ),
    17: Design(
        draw=draw_composition_1,
        params={
            "K1": 63,
            "DX": 240,
            "DY": 240,
            "R1": 480*0.15,
            "A1": 0,
            "K": 4,
            "H": 1,
            "R": 480*0.35,
            "AD": 0,
            "NP": 480,
        },
    ),
    18: Design(
        draw=draw_composition_1,
        params={
            "K1": 25,
            "DX": 240,
            "DY": 240,
            "R1": 480*0.1,
            "A1": math.pi/2,
            "K": 5,
            "H": 2,
            "R": 480*0.4,
            "AD": math.pi/2,
            "NP": 480,
        },
    ),
    19: Design(
        draw=draw_composition_1,
        params={
            "K1": 99,
            "DX": 240,
            "DY": 240,
            "R1": 480*0.25,
            "A1": 0,
            "K": 7,
            "H": 3,
            "R": 480*0.25,
            "AD": math.pi/2,
            "NP": 480,
        },
    ),
    20: Design(
        draw=draw_composition_2,
        params={
            "K1": 8,
            "N": 32,
            "K": 16,
            "H": 5,
            "R1": 480*0.36,
            "R": 480*0.14,
            "RR": 0.9,
            "DX": 240,
            "DY": 240,
            "NP": 480,
        },
    ),
    21: Design(
        draw=draw_composition_2,
        params={
            "K1": 10,
            "N": 30,
            "K": 8,
            "H": 3,
            "R1": 480*0.35,
            "R": 480*.15,
            "RR": 0.85,
            "DX": 240,
            "DY": 240,
            "NP": 480,
        },
    ),
    22: Design(
        draw=draw_composition_2,
        params={
            "K1": 10,
            "N": 10,
            "K": 18,
            "H": 7,
            "R1": 480*0,
            "R": 480*0.5,
            "RR": 0.8,
            "NP": 480,
        },
    ),
    23: Design(
        draw=draw_composition_2,
        params={
            "K1": 10,
            "N": 10,
            "K": 21,
            "H": 10,
            "R1": 480*0,
            "R": 480*0.5,
            "RR": 0.75,
            "NP": 480,
        },
    ),
    24: Design(
        draw=draw_composition_2,
        params={
            "K1": 28,
            "N": 56,
            "K": 7,
            "H": 3,
            "R1": 480*0.15,
            "R": 480*0.35,
            "RR": 0.95,
            "NP": 480,
        },
    ),
    25: Design(
        draw=draw_composition_2,
        params={
            "K1": 20,
            "N": 60,
            "K": 8,
            "H": 1,
            "R1": 480*0.05,
            "R": 480*0.45,
            "RR": 0.945,
            "NP": 480,
        },
    ),
    26: Design(
        draw=draw_prettygon,
        params={"K": 200, "AN": 15*(math.pi/31), "RA": 0.98, "AA": 0, "RR": 480*0.80, "NP": 480},
    ),
    27: Design(
        draw=draw_prettygon,
        params={"K": 120, "AN": 29*(math.pi/30), "RA": 0.98, "initial_y": 240, "NP": 480},
    ),
    28: Design(
        draw=draw_prettygon,
        params={"K": 200, "AN": math.pi/4, "RA": 0.98, "AA": 0.0, "RR": 480*0.40, "NP": 480},
    ),
    29: Design(
        draw=draw_prettygon,
        params={"K": 200, "AN": math.pi/20, "RA": 0.998, "AA": 0.0, "RR": 480*0.65, "NP": 480},
    ),
    30: Design(
        draw=draw_prettygon,
        params={"K": 200, "AN": 4*(math.pi/5)+0.02, "RA": 0.99, "RR": 480*0.80, "initial_y": 200, "NP": 480},
    ),
    31: Design(
        draw=draw_prettygon,
        params={"K": 100, "AN": 6*(math.pi/7), "RA": 0.98, "initial_y": 200, "NP": 480},
    ),
    32: Design(
        draw=draw_prettygon,
        params={
            "K": 300,
            "AN": 2*(math.pi/5)+0.01,
            "RA": 0.993,
            "AA": 0.0,
            "RR": 480*0.60,
            "initial_y": 20,
            "NP": 480,
        },
    ),
    33: Design(
        draw=draw_prettygon,
        params={"K": 400, "AN": 19*(math.pi/60), "RA": 0.996, "RR": 480*0.60, "NP": 480},
    ),
}
