"""Fractal star designs (designs 65-77) from the book."""

import math

from dessins.shapes import draw_fractal_star

from .spec import Design

DESIGNS: dict[int, Design] = {
    65: Design(draw=draw_fractal_star),
    66: Design(
        draw=draw_fractal_star,
        params={"N": 7, "K": 4, "RA": 0.32, "LL": 480, "AA": 6*math.pi/7, "NP": 480},
    ),
    67: Design(
        draw=draw_fractal_star,
        params={"N": 12, "K": 3, "RA": 0.5, "LL": 480*11/48, "AA": 2*math.pi/12, "NP": 480},
    ),
    68: Design(
        draw=draw_fractal_star,
        params={"N": 5, "K": 2, "RA": 0.5, "LL": 480/2, "AA": 2*math.pi/5, "NP": 480},
    ),
    69: Design(
        draw=draw_fractal_star,
        params={"N": 8, "K": 2, "RA": 0.5, "LL": 480/3, "AA": math.pi/4, "NP": 480},
    ),
    70: Design(
        draw=draw_fractal_star,
        params={"N": 20, "K": 2, "RA": 0.5, "LL": 480*13/96, "AA": math.pi/10, "NP": 480},
    ),
    71: Design(
        draw=draw_fractal_star,
        params={"N": 15, "K": 2, "RA": 0.9, "LL": 480*43/48, "AA": 14*math.pi/15, "NP": 480},
    ),
    72: Design(
        draw=draw_fractal_star,
        params={"N": 16, "K": 3, "RA": 0.27, "LL": 480/6, "AA": math.pi/8, "NP": 480},
    ),
    73: Design(
        draw=draw_fractal_star,
        params={"N": 8, "K": 4, "RA": 0.5, "LL": 480*17/48, "AA": math.pi/4, "NP": 480},
    ),
    74: Design(
        draw=draw_fractal_star,
        params={"N": 7, "K": 5, "RA": 0.383, "LL": 480*7/12, "AA": 2*math.pi/5, "NP": 480},
    ),
    75: Design(
        draw=draw_fractal_star,
        params={"N": 4, "K": 8, "RA": 0.47, "LL": 480, "AA": math.pi/2, "NP": 480},
    ),
    76: Design(
        draw=draw_fractal_star,
        params={"N": 15, "K": 3, "RA": 0.3, "LL": 480, "AA": 14*math.pi/15, "NP": 480},
    ),
    77: Design(
        draw=draw_fractal_star,
        params={"N": 3, "K": 11, "RA": 0.62, "LL": 480, "AA": 2*math.pi/3, "NP": 480},
    ),
}
