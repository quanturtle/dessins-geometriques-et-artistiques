"""Command-line interface for drawing geometric designs using Turtle graphics."""

import argparse
import inspect
import sys
import turtle
from typing import Any, Callable

from dessins.cad import Path, generate_cad, record_paths
from dessins.designs import DESIGNS
from dessins.shapes import SHAPES

COMMON_ARGS = {
    "--animation": {
        "choices": ["fast", "fastest", "instant"],
        "default": "instant",
        "required": False,
        "help": "Animation speed (default: instant)",
    },
    "--output": {
        "type": str,
        "default": None,
        "required": False,
        "help": "Output file name (default: No file output)",
    },
    "--width": {
        "type": int,
        "default": 480,
        "required": False,
        "help": "Canvas width (default: 480)",
    },
    "--height": {
        "type": int,
        "default": 480,
        "required": False,
        "help": "Canvas height (default: 480)",
    },
}

# canvas windows for shapes drawn with their book defaults, in multiples of size
SHAPE_WORLDS = {
    "linear_modulo": (0, 0, 1.5, 1.5),
    "simple_fractal": (0, 0, 1.3, 1.3),
    "d3data": (0, 0, 1.5, 1.5),
}


def numeric_params(draw_function: Callable[..., Any]) -> list[tuple[str, type, Any]]:
    """List the (name, type, default) of a draw function's numeric parameters."""
    params: list[tuple[str, type, Any]] = []
    for name, param in inspect.signature(draw_function).parameters.items():
        if isinstance(param.default, (int, float)) and not isinstance(param.default, bool):
            params.append((name, type(param.default), param.default))
    return params


def add_common_arguments(parser: argparse.ArgumentParser, skipped: tuple[str, ...] = ()) -> None:
    for arg_name, arg_config in COMMON_ARGS.items():
        if arg_name not in skipped:
            parser.add_argument(arg_name, **arg_config)
    return


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Draw shapes and designs using Turtle graphics.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    shape_parser = subparsers.add_parser("shape", help="Draw one of the book's programs")
    shape_subparsers = shape_parser.add_subparsers(dest="shape_name", required=True)

    for shape_name, draw_function in SHAPES.items():
        subparser = shape_subparsers.add_parser(shape_name, help=f"Draw {shape_name}")
        for param_name, param_type, default in numeric_params(draw_function):
            subparser.add_argument(
                f"-{param_name}",
                type=param_type,
                default=None,
                required=False,
                help=f"{param_name} (default: {default})",
            )
        add_common_arguments(subparser)

    design_parser = subparsers.add_parser("design", help="Draw one of the book's numbered designs")
    design_parser.add_argument("design_number", type=int, help="Design number to draw (1-252)")
    add_common_arguments(design_parser)

    check_parser = subparsers.add_parser("check", help="Draw every numbered design once, then exit")
    add_common_arguments(check_parser, skipped=("--output",))

    return parser


def inject_canvas_size(draw_function: Callable[..., Any], params: dict[str, Any], size: int) -> None:
    """Pass the canvas size as NP when the draw function accepts it and no value was given."""
    if "NP" in inspect.signature(draw_function).parameters and "NP" not in params:
        params["NP"] = size
    return


def resolve_design(args: argparse.Namespace, size: int) -> tuple[Callable[..., Any], dict[str, Any], tuple | None]:
    design = DESIGNS[args.design_number]

    params = dict(design.params)
    inject_canvas_size(design.draw, params, size)

    return design.draw, params, design.world


def setup_canvas(width: int, height: int, animation: str, world: tuple | None) -> None:
    """Configure the turtle canvas; world is in multiples of size, None for the default window."""
    size = min(width, height)
    turtle.setup(width=width, height=height)

    if world is None:
        turtle.setworldcoordinates(0, 0, width, height)
    else:
        turtle.setworldcoordinates(world[0] * size, world[1] * size, world[2] * size, world[3] * size)

    match animation:
        case "instant":
            turtle.tracer(0)
        case "fast":
            turtle.speed("fast")
        case "fastest":
            turtle.speed("fastest")

    turtle.penup()
    turtle.home()
    return


def check_designs(args: argparse.Namespace, size: int) -> None:
    """Draw every design sequentially, resetting the canvas between designs."""
    for index, number in enumerate(sorted(DESIGNS), start=1):
        args.design_number = number
        draw_function, params, world = resolve_design(args, size)

        setup_canvas(args.width, args.height, args.animation, world)
        record_paths(draw_function, **params)
        turtle.update()

        # reset after each design to avoid overlap
        turtle.reset()

        # every 16 designs, clear the screen completely
        if index % 16 == 0:
            turtle.clearscreen()

    turtle.bye()
    return


def resolve_shape(args: argparse.Namespace, size: int) -> tuple[Callable[..., Any], dict[str, Any], tuple | None]:
    draw_function = SHAPES[args.shape_name]

    skipped = {"command", "shape_name", "animation", "output", "width", "height"}
    params = {name: value for name, value in vars(args).items() if name not in skipped and value is not None}
    inject_canvas_size(draw_function, params, size)

    return draw_function, params, SHAPE_WORLDS.get(args.shape_name)


def post_processing(paths: list[Path], name: str | None) -> None:
    """Finalize drawing and optionally export CAD data."""
    turtle.hideturtle()
    turtle.update()

    if paths and name:
        generate_cad(paths, name)

    turtle.exitonclick()
    return


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    size = min(args.width, args.height)

    if args.command == "check":
        check_designs(args, size)
        return 0

    if args.command == "shape":
        draw_function, params, world = resolve_shape(args, size)
    elif args.design_number in DESIGNS:
        draw_function, params, world = resolve_design(args, size)
    else:
        print(f"Error: Design '{args.design_number}' not found. Available: 1-252.")
        return 1

    setup_canvas(args.width, args.height, args.animation, world)
    paths = record_paths(draw_function, **params)
    post_processing(paths, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
