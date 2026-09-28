"""Folded-paper dragon designs (designs 50-64) from the book."""

import math

from dessins.shapes import draw_dragon

from .spec import Design


def A_every_third(N: int) -> list[int]:
    A = [0] * (N + 1)

    for i in range(0, N + 1, 3):
        A[i] = 1

    return A


def A_every_fourth(N: int) -> list[int]:
    A = [0] * (N + 1)

    for i in range(0, N + 1, 4):
        A[i] = 1

    return A


def A_every_fourth_pair(N: int) -> list[int]:
    A = [0] * (N + 1)

    for i in range(0, N + 1, 4):
        A[i] = 1
        A[i + 1] = 1

    return A


def A_every_fifth(N: int) -> list[int]:
    A = [0] * (N + 1)

    for i in range(0, N + 1, 5):
        A[i] = 1

    return A


def A_every_fifth_offset_two(N: int) -> list[int]:
    A = [0] * (N + 1)

    for i in range(0, N + 1, 5):
        A[i] = 1

    for i in range(1, N, 5):
        A[i + 1] = 1

    return A


def A_every_fifth_offset_three(N: int) -> list[int]:
    A = [0] * (N + 1)

    for i in range(0, N + 1, 5):
        A[i] = 1

    for i in range(1, N - 1, 5):
        A[i + 2] = 1

    return A


DESIGNS: dict[int, Design] = {
    50: Design(draw=draw_dragon, params={"N": 6}),
    51: Design(draw=draw_dragon, params={"N": 10}),
    52: Design(draw=draw_dragon, params={"N": 14}),
    53: Design(
        draw=draw_dragon,
        params={
            "N": 10,
            "A_initializer": A_every_third,
            "initial_values": [480*0.25, 0, -math.pi/2, 480/math.sqrt(2)**10*0.9],
        },
        world=(-1, -1, 1, 1),
    ),
    54: Design(
        draw=draw_dragon,
        params={
            "N": 14,
            "A_initializer": A_every_third,
            "initial_values": [480*0.25, 0, -math.pi, 480/math.sqrt(2)**14*0.9],
        },
        world=(-3, -3, 3, 3),
    ),
    55: Design(
        draw=draw_dragon,
        params={
            "N": 10,
            "A_initializer": A_every_fourth,
            "initial_values": [480*0.62, 0, 0, 480/math.sqrt(2)**10*0.9],
        },
        world=(-1, -1, 1, 1),
    ),
    56: Design(
        draw=draw_dragon,
        params={
            "N": 14,
            "A_initializer": A_every_fourth,
            "initial_values": [480*0.62, 0, -math.pi/2, 480/math.sqrt(2)**14*0.9],
        },
        world=(-3, -3, 3, 3),
    ),
    57: Design(
        draw=draw_dragon,
        params={
            "N": 10,
            "A_initializer": A_every_fourth_pair,
            "initial_values": [480*0.7, 480/2, math.pi/2, 480/math.sqrt(2)**10*0.8],
        },
        world=(-1, -1, 1, 1),
    ),
    58: Design(
        draw=draw_dragon,
        params={
            "N": 14,
            "A_initializer": A_every_fourth_pair,
            "initial_values": [480*0.7, 480/2, math.pi/2, 480/math.sqrt(2)**14*0.8],
        },
        world=(-1, -1, 1, 1),
    ),
    59: Design(
        draw=draw_dragon,
        params={
            "N": 10,
            "A_initializer": A_every_fifth,
            "initial_values": [480*0.4, 480/2, math.pi, 480/math.sqrt(2)**10*0.9],
        },
        world=(-1, -1, 1, 1),
    ),
    60: Design(
        draw=draw_dragon,
        params={
            "N": 14,
            "A_initializer": A_every_fifth,
            "initial_values": [480*0.4, 480/2, 0, 480/math.sqrt(2)**14*0.9],
        },
        world=(-1, -1, 1, 1),
    ),
    61: Design(
        draw=draw_dragon,
        params={
            "N": 10,
            "A_initializer": A_every_fifth_offset_two,
            "initial_values": [480*0.55, 480/2, 0, 480/math.sqrt(2)**10*0.96],
        },
        world=(-1, -1, 1, 1),
    ),
    62: Design(
        draw=draw_dragon,
        params={
            "N": 14,
            "A_initializer": A_every_fifth_offset_two,
            "initial_values": [480*0.55, 480/2, 3*math.pi/2, 480/math.sqrt(2)**14*0.96],
        },
    ),
    63: Design(
        draw=draw_dragon,
        params={
            "N": 10,
            "A_initializer": A_every_fifth_offset_three,
            "initial_values": [480*0.15, 480/2, 0, 480/math.sqrt(2)**10*0.9],
        },
    ),
    64: Design(
        draw=draw_dragon,
        params={
            "N": 14,
            "A_initializer": A_every_fifth_offset_three,
            "initial_values": [480*0.15, 480/2, 0, 480/math.sqrt(2)**14*0.9],
        },
    ),
}
