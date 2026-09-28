"""Utilities for capturing turtle coordinates during drawing."""

from __future__ import annotations

from functools import wraps
from typing import Any, Callable

import turtle


_points_stack: list[list[tuple[float, float]]] = []
_original_goto = turtle.goto


def _goto_wrapper(x: float, y: float | None = None) -> None:
    """Proxy for ``turtle.goto`` that records points when active."""
    if y is None:
        x, y = x  # type: ignore[misc]

    if _points_stack:
        for pts in _points_stack:
            pts.append((float(x), float(y)))

    _original_goto(x, y)  # type: ignore[arg-type]


# Replace the Turtle goto with our proxy so points can be logged globally.
turtle.goto = _goto_wrapper  # type: ignore[assignment]


F = Callable[..., Any]


def capture_points(func: F) -> Callable[..., list[tuple[float, float]]]:
    """Decorator to collect turtle coordinates for CAD export."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> list[tuple[float, float]]:
        _points_stack.append([])

        try:
            result = func(*args, **kwargs)
        finally:
            pts = _points_stack.pop()

        return result if result is not None else pts

    wrapper.__annotations__["return"] = list[tuple[float, float]]
    return wrapper


__all__ = ["capture_points"]

