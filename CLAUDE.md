# Project contract

Python port of the 252 designs in Delahaye's 1985 book. The README is the user-facing doc; this file is the contract for working on the code.

## Package map

```
dessins/
  cli.py          argparse entry point: shape | design | check; main() is last
  __main__.py     python -m dessins
  shapes/         one module per book program; SHAPES maps name -> draw function
  designs/        one module per book chapter; DESIGNS maps number -> Design
  designs/spec.py Design(draw, params, world): world is (llx, lly, urx, ury) in multiples of the canvas size, None = (0, 0, width, height)
  cad/paths.py    record_paths(draw, **params) -> list[Path]; turtle only
  cad/geometry.py smooth_path, stroke_polygons; pure, no turtle, no manifold3d
  cad/export.py   build_model -> Mesh, write_stl; manifold3d and filesystem
```

`dessins/cad/__init__.py` holds only a docstring. Import the edge modules directly so `geometry` stays importable without turtle or manifold3d.

## Draw function contract

- Signature: keyword parameters with numeric defaults taken from the book's base program (line 100 of the listing), plus `NP` for the canvas size when the program uses it. The CLI exposes every numeric default as a `-NAME` flag and injects `NP` when not given.
- Body: only `turtle.goto`, `turtle.penup`, `turtle.pendown` (and `turtle.clear`). No other turtle movement, or the recorder misses it.
- Coordinates are floats. The book's `INT()` before `LPRINT` is plotter quantization and is not reproduced. `INT()` that is part of an algorithm stays (band indices `I1`, `I2`, `M` in SURFACES; fractional parts in the surface Z functions).
- Returns `None`. Points are captured by the recorder, never by the shape.
- Loops follow the listing: `FOR I=0 TO N` is `range(N + 1)`.

## Catalog contract

- `DESIGNS[n].params` are the book's "Modifications pour le dessin n" applied to the base program. Values are written in canvas units with `480` spelled out, as in the book.
- A design that changes a formula gets a module-level function or lambda in the chapter module, named after the design number (`compute_z_185`, `design_35`).
- Adding a design: add the entry in its chapter module; the number range in the module docstring and the README index must include it.

## CAD pipeline

Pipeline: record -> smooth (optional) -> stroke -> union -> extrude -> write.

- `record_paths` proxies `turtle.goto` for the duration of the call and restores it after. A pen-up move starts a new path; paths shorter than two points are dropped.
- `smooth_path` is a uniform Catmull-Rom spline with clamped endpoints, 4 subdivisions per segment. Paths shorter than 3 points pass through.
- `stroke_polygons` covers a path with one counter-clockwise rectangle per segment and one circle per vertex (round joins and caps). Winding matters: manifold3d's fill rule treats clockwise polygons as holes.
- `build_model` unions the polygons with `CrossSection.batch_boolean(OpType.Add)`, extrudes along Z by `depth`, and raises if the result is not a valid manifold.
- Units: one canvas unit is one STL unit. Drawing on XY, extrusion along Z, so the part lies flat on the bed.

## Commands

```sh
uv sync
uv run dessins shape dragon
uv run dessins design 78 --output design78 --smooth   # writes output/design78.stl
uv run dessins check                                  # draws all 252 designs, exits 0
```

`uv run dessins check` is the regression check for the catalog: run it after touching any shape or design.

If turtle fails with `Can't find a usable init.tcl` under the uv-managed Python:
```sh
export TCL_LIBRARY="$(uv run python -c 'import sys; print(sys.base_prefix)')/lib/tcl8.6"
export TK_LIBRARY="$(uv run python -c 'import sys; print(sys.base_prefix)')/lib/tk8.6"
```

## Repository

- `output/` is gitignored and holds generated STLs. `stl/` holds committed samples from the original pipeline and is not regenerated.
- One task per commit; the repo passes `uv run dessins check` at every commit.
