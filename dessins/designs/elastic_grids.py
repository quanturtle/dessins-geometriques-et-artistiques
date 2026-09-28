"""Elastic grid designs (designs 164-176) from the book."""

import math

from dessins.shapes import draw_elastic_grid

from .spec import Design


def deformation_subroutine_165(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        DI = DI ** 3

    return DI, AN


def deformation_subroutine_166(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN = AN + math.pi/2*(1 - DI)

    return DI, AN


def deformation_subroutine_167(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += 3.5 * (1 - DI)
        DI = DI ** 0.3

    return DI, AN


def deformation_subroutine_168(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += 2 * math.pi * (1 - DI)

    return DI, AN


def deformation_subroutine_169(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += math.pi * (1 - DI)
        DI = DI ** 3

    return DI, AN


def deformation_subroutine_170(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += (math.pi/2) * math.sin(math.pi*(1-DI))
        DI = DI ** 0.2

    return DI, AN


def deformation_subroutine_171(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += (math.pi/4) * math.sin(2 * math.pi * (1-DI))

    return DI, AN


def deformation_subroutine_172(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += (math.pi/2) * math.sin(math.pi * (1-DI))
        DI = DI ** 2

    return DI, AN


def deformation_subroutine_173(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += (math.pi/2) * math.sin(math.pi * (1-DI))

    return DI, AN


def xy_transform_174(I: float, J: float) -> tuple[float, float]:
    return I / 20 - 1, J / 20 - 1


def deformation_subroutine_174(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += math.pi * (1-DI)
        DI = DI ** .3

    return DI, AN


def xy_transform_175(I: float, J: float) -> tuple[float, float]:
    return I / 10 - 1, J / 20 - 1


def deformation_subroutine_175(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += math.pi * 2 * (1-DI)

    return DI, AN


def xy_transform_176(I: float, J: float) -> tuple[float, float]:
    return I / 20 - 1, J / 20 - 1


def deformation_subroutine_176(DI: float, AN: float) -> tuple[float, float]:
    if DI < 1:
        AN += math.pi * 2* (1-DI)

    return DI, AN


DESIGNS: dict[int, Design] = {
    164: Design(draw=draw_elastic_grid),
    165: Design(draw=draw_elastic_grid, params={"deformation_subroutine": deformation_subroutine_165}),
    166: Design(draw=draw_elastic_grid, params={"deformation_subroutine": deformation_subroutine_166}),
    167: Design(draw=draw_elastic_grid, params={"deformation_subroutine": deformation_subroutine_167}),
    168: Design(draw=draw_elastic_grid, params={"deformation_subroutine": deformation_subroutine_168}),
    169: Design(draw=draw_elastic_grid, params={"deformation_subroutine": deformation_subroutine_169}),
    170: Design(draw=draw_elastic_grid, params={"deformation_subroutine": deformation_subroutine_170}),
    171: Design(draw=draw_elastic_grid, params={"deformation_subroutine": deformation_subroutine_171}),
    172: Design(draw=draw_elastic_grid, params={"deformation_subroutine": deformation_subroutine_172}),
    173: Design(draw=draw_elastic_grid, params={"deformation_subroutine": deformation_subroutine_173}),
    174: Design(
        draw=draw_elastic_grid,
        params={
            "xy_transform": xy_transform_174,
            "deformation_subroutine": deformation_subroutine_174,
            "L_range": 1,
            "I_range": 41,
            "J_range": 41,
        },
    ),
    175: Design(
        draw=draw_elastic_grid,
        params={
            "xy_transform": xy_transform_175,
            "deformation_subroutine": deformation_subroutine_175,
            "L_range": 1,
            "I_range": 21,
            "J_range": 41,
        },
    ),
    176: Design(
        draw=draw_elastic_grid,
        params={
            "xy_transform": xy_transform_176,
            "deformation_subroutine": deformation_subroutine_176,
            "L_range": 1,
            "I_range": 21,
            "J_range": 41,
        },
    ),
}
