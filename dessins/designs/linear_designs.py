"""Linear designs (designs 101-114) from the book."""

import math

from dessins.shapes import draw_complete_bipartite_graph, draw_linear_modulo, draw_linear_sticks

from .spec import Design


def compute_Y_109(NP: int, K2: float, i: int, N: int) -> float:
    return NP * 0.5 * (1 + math.cos(K2 * i * math.pi / N))


def I1_func_109(i: int, H: int, N: int) -> float:
    return 8 * i % N


def compute_R1_111(i: int, NP: int) -> float:
    return NP / 4


def compute_R2_111(i: int, NP: int) -> float:
    return NP * 5 / 24


def compute_R1_112(i: int, NP: int) -> float:
    return NP / 3 * 0.7**(i - 1)


def compute_R2_112(i: int, NP: int) -> float:
    return NP / 8 * 0.9**(i - 1)


def compute_YD_112(NP: int, R1: float, R2: float, AN: float, K: int) -> float:
    return 1.2 * (NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN))


def compute_YA_112(NP: int, R1: float, R2: float, AN: float, K: int) -> float:
    return 1.2 * (NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN + math.pi))


def compute_R1_113(i: int, NP: int) -> float:
    return NP / 3 * 0.6**(i - 1)


def compute_R2_113(i: int, NP: int) -> float:
    return NP / 8 * 0.6**(i - 1)


def compute_R1_114(i: int, NP: int) -> float:
    return (NP / 3) * (0.8 ** (i - 1))


def compute_R2_114(i: int, NP: int) -> float:
    return (NP / 12) * (0.8 ** (i - 1))


def compute_YD_114(NP: int, R1: float, R2: float, AN: float, K: int) -> float:
    return 1.3 * (NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN))


def compute_YA_114(NP: int, R1: float, R2: float, AN: float, K: int) -> float:
    return 1.3 * compute_YD_114(NP, R1, R2, AN, K)


DESIGNS: dict[int, Design] = {
    101: Design(draw=draw_complete_bipartite_graph),
    102: Design(
        draw=draw_complete_bipartite_graph,
        params={
            "N": 15,
            "XA": 480/2,
            "YA": 480/15,
            "XB": 480/2,
            "YB": 1.2*480,
            "XC": 0,
            "YC": 0,
            "XD": 480,
            "YD": 0,
        },
    ),
    103: Design(
        draw=draw_complete_bipartite_graph,
        params={
            "N": 19,
            "XA": 0,
            "YA": 0,
            "XB": 480,
            "YB": 1.4*480,
            "XC": 0,
            "YC": 1.4*480,
            "XD": 480,
            "YD": 0,
        },
    ),
    104: Design(
        draw=draw_complete_bipartite_graph,
        params={
            "N": 16,
            "XA": 0,
            "YA": 0,
            "XB": 480/2,
            "YB": 480,
            "XC": 480,
            "YC": 0,
            "XD": 480/2,
            "YD": 480,
        },
    ),
    105: Design(draw=draw_linear_modulo),
    106: Design(draw=draw_linear_modulo, params={"N": 500, "M": 500, "K1": 11/7, "K2": 7/3, "H": 3}),
    107: Design(draw=draw_linear_modulo, params={"N": 400, "M": 400, "K1": 4, "K2": 2, "H": 2}),
    108: Design(draw=draw_linear_modulo, params={"N": 300, "M": 300, "K1": 5, "K2": 3, "H": 2}),
    109: Design(
        draw=draw_linear_modulo,
        params={
            "N": 400,
            "M": 200,
            "K1": 2,
            "K2": 2,
            "H": 9,
            "compute_Y": compute_Y_109,
            "I1_func": I1_func_109,
        },
    ),
    110: Design(draw=draw_linear_sticks),
    111: Design(
        draw=draw_linear_sticks,
        params={
            "N": 600,
            "M": 1,
            "K": 5,
            "compute_R1": compute_R1_111,
            "compute_R2": compute_R2_111,
        },
    ),
    112: Design(
        draw=draw_linear_sticks,
        params={
            "N": 100,
            "M": 6,
            "K": 6,
            "compute_R1": compute_R1_112,
            "compute_R2": compute_R2_112,
            "compute_YD": compute_YD_112,
            "compute_YA": compute_YA_112,
        },
    ),
    113: Design(
        draw=draw_linear_sticks,
        params={
            "N": 300,
            "M": 4,
            "K": 3,
            "compute_R1": compute_R1_113,
            "compute_R2": compute_R2_113,
        },
    ),
    114: Design(
        draw=draw_linear_sticks,
        params={
            "N": 300,
            "M": 7,
            "K": 7,
            "compute_R1": compute_R1_114,
            "compute_R2": compute_R2_114,
            "compute_YD": compute_YD_114,
            "compute_YA": compute_YA_114,
        },
    ),
}
