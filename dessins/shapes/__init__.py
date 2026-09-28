"""The original drawing programs from the book, one module per program."""

from typing import Callable

from .bird_fish import draw_bird_fish
from .complete_bipartite_graph import draw_complete_bipartite_graph
from .composition_1 import draw_composition_1
from .composition_2 import draw_composition_2
from .d3cube import draw_d3cube
from .d3data import draw_d3data
from .d3structures import draw_d3structures
from .dragon import draw_dragon
from .elastic_grid import draw_elastic_grid
from .fractal_star import draw_fractal_star
from .horse import draw_horse
from .linear_modulo import draw_linear_modulo
from .linear_sticks import draw_linear_sticks
from .lion import draw_lion
from .orbiting_curves import draw_orbiting_curves
from .prettygon import draw_prettygon
from .regular_polygon import draw_regular_polygon
from .regular_star import draw_regular_star
from .rotating_curves import draw_rotating_curves
from .simple_fractal import draw_simple_fractal
from .simple_fractal_deformed import draw_simple_fractal_deformed
from .simple_fractal_rounded import draw_simple_fractal_rounded
from .smurf import draw_smurf
from .spiraling_curves import draw_spiraling_curves
from .surface import draw_surface

SHAPES: dict[str, Callable] = {
    "regular_polygon": draw_regular_polygon,
    "regular_star": draw_regular_star,
    "composition_1": draw_composition_1,
    "composition_2": draw_composition_2,
    "prettygon": draw_prettygon,
    "horse": draw_horse,
    "lion": draw_lion,
    "bird_fish": draw_bird_fish,
    "smurf": draw_smurf,
    "dragon": draw_dragon,
    "fractal_star": draw_fractal_star,
    "orbiting_curves": draw_orbiting_curves,
    "rotating_curves": draw_rotating_curves,
    "spiraling_curves": draw_spiraling_curves,
    "complete_bipartite_graph": draw_complete_bipartite_graph,
    "linear_modulo": draw_linear_modulo,
    "linear_sticks": draw_linear_sticks,
    "simple_fractal": draw_simple_fractal,
    "simple_fractal_rounded": draw_simple_fractal_rounded,
    "simple_fractal_deformed": draw_simple_fractal_deformed,
    "elastic_grid": draw_elastic_grid,
    "surface": draw_surface,
    "d3data": draw_d3data,
    "d3cube": draw_d3cube,
    "d3structures": draw_d3structures,
}
