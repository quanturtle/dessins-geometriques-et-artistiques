"""Catalog of the numbered designs from the book, keyed by design number."""

from .spec import Design
from . import (
    curves,
    designs_from_data,
    elastic_grids,
    folding_paper_dragons,
    fractal_stars,
    linear_designs,
    polygons_stars,
    simple_fractals,
    surfaces,
    third_dimension,
)

_CATEGORIES = [
    polygons_stars,
    designs_from_data,
    folding_paper_dragons,
    fractal_stars,
    curves,
    linear_designs,
    simple_fractals,
    elastic_grids,
    surfaces,
    third_dimension,
]

DESIGNS: dict[int, Design] = {}
for _category in _CATEGORIES:
    DESIGNS.update(_category.DESIGNS)

__all__ = ["Design", "DESIGNS"]
