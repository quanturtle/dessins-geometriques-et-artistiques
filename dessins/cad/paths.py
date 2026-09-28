"""Record the pen-down paths a draw function traces with turtle."""

import turtle
from typing import Any, Callable

from .geometry import Path


class PathRecorder:
    """Proxy for turtle.goto that splits the visited points into pen-down paths."""

    def __init__(self, goto: Callable[..., None]) -> None:
        self.goto = goto
        self.paths: list[Path] = []

    def __call__(self, x: Any, y: float | None = None) -> None:
        """Start a new path on a pen-up move, extend the current one on a pen-down move."""
        if y is None:
            x, y = x
        point = (float(x), float(y))

        if not turtle.isdown():
            self.paths.append([point])
        elif self.paths:
            self.paths[-1].append(point)
        else:
            self.paths.append([tuple(turtle.pos()), point])

        self.goto(x, y)
        return


def record_paths(draw: Callable[..., Any], **params: Any) -> list[Path]:
    """Run a draw function with turtle.goto proxied; return its pen-down paths of two points or more."""
    recorder = PathRecorder(turtle.goto)
    turtle.goto = recorder

    try:
        draw(**params)
    finally:
        turtle.goto = recorder.goto

    return [path for path in recorder.paths if len(path) > 1]
