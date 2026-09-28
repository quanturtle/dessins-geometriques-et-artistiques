"""Specification for one catalog entry: a numbered design from the book."""

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass(frozen=True)
class Design:
    """A book design: a draw callable, its parameters, and its canvas window.

    world is (llx, lly, urx, ury) in multiples of the canvas size; None means
    the default window (0, 0, width, height).
    """

    draw: Callable[..., Any]
    params: dict[str, Any] = field(default_factory=dict)
    world: tuple[float, float, float, float] | None = None
