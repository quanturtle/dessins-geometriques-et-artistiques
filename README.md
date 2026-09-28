# Dessins géométriques et artistiques avec votre micro-ordinateur
> Inspired by https://github.com/v3ga/dessins_geometriques_et_artistiques/

Python recreation of the 252 designs in Jean-Paul Delahaye's 1985 book, drawn with the turtle module and exportable as STL files for 3D printing.

Book scans: [Dessins géométriques et artistiques avec votre micro-ordinateur](https://nextcloud.univ-lille.fr/index.php/s/R4PgSRWGyHEbDgG) and [Nouveaux dessins géométriques et artistiques avec votre micro-ordinateur](https://nextcloud.univ-lille.fr/index.php/s/cwXAAokbbeaykW6).

## About
In 1985, mathematician Jean-Paul Delahaye used a [Canon X-07](https://en.wikipedia.org/wiki/Canon_X-07) microcomputer with an [X-710 color plotter](https://www.youtube.com/watch?v=JWhNcsYoXQ0) to create simple yet elegant designs, showcased in his book _Dessins géométriques et artistiques avec votre micro-ordinateur_. This project ports the original BASIC programs to Python and reproduces the designs with the turtle module, as Delahaye did four decades ago.

![Star](/img/example_star.png)

![Dragon](/img/example_dragon.png)

The same programs can also produce CAD models, so the drawings can be 3D printed.

| Turtle   | CAD     | Slicer   | Printing |  Printed |
| -------- | ------- | -------- | -------- | -------- |
| ![8-point star Turtle](/img/star8_turtle.png) | ![8-point star CAD](/img/star8_cad.png) | ![8-point star slicer](/img/star8_slicer.png) | ![8-point star printing](/img/star8_printing.png) | ![8-point star printed](/img/star8_printed.png) |

## Install
Requires [uv](https://docs.astral.sh/uv/).
```sh
uv sync
uv run dessins shape dragon
```
A window opens with the drawing. Click it to close.

If the window fails with `Can't find a usable init.tcl`, the uv-managed Python cannot locate its Tcl library. Point it there and try again:
```sh
export TCL_LIBRARY="$(uv run python -c 'import sys; print(sys.base_prefix)')/lib/tcl8.6"
export TK_LIBRARY="$(uv run python -c 'import sys; print(sys.base_prefix)')/lib/tk8.6"
```

## Draw a program from the book
Each program of the book is a shape. Run it with the book's base parameters, or override any of them:
```sh
uv run dessins shape regular_star
uv run dessins shape regular_star -K 8
uv run dessins shape dragon -N 12
```
`uv run dessins shape --help` lists the shapes; `uv run dessins shape <name> --help` lists the parameters of one shape with their defaults.

## Draw a numbered design
The 252 designs of the book are numbered as in the book:
```sh
uv run dessins design 78
```
`uv run dessins check` draws all 252 designs one after the other and exits.

Both commands accept `--animation {fast,fastest,instant}` (default `instant`) and `--width`/`--height` for the window size (default 480).

## Export an STL
Add `--output <name>` to either command. The file lands in `output/<name>.stl`:
```sh
uv run dessins shape regular_star -K 8 --output star8
uv run dessins design 78 --output design78 --smooth
```
Every line the pen draws becomes a stroke with round joins and caps, the strokes are merged and extruded, and the model lies flat on the print bed. One canvas unit becomes one STL unit, so a 480-unit drawing imports as 480 mm; scale it in the slicer.

| Flag | Default | Effect |
| --- | --- | --- |
| `--line-width` | 3.5 | Width of each stroke, in canvas units |
| `--depth` | 10 | Height of the extrusion, in canvas units |
| `--smooth` | off | Fit a spline through the drawn points before stroking |

`--smooth` is for the chapters that approximate curves with many short segments: curves (designs 78-100), surfaces (177-200) and rounded fractals (136-151). Polygons, stars, dragons, fractals and linear designs are made of straight segments and should stay sharp. Design 78 at the same zoom, without and with `--smooth`:

| `--output design78` | `--output design78 --smooth` |
| --- | --- |
| ![Design 78 stroked as drawn](/img/design78_stroke_raw.png) | ![Design 78 stroked through a spline](/img/design78_stroke_smooth.png) |

## Index
1. Polygones, étoiles, etc. (designs 1-33, [dessins/designs/polygons_stars.py](./dessins/designs/polygons_stars.py))
    * [Le programme POLYGONES RÉGULIERS](./dessins/shapes/regular_polygon.py)
    * [Le programme ÉTOILES RÉGULIÈRES](./dessins/shapes/regular_star.py)
    * [Le programme COMPOSITION 1](./dessins/shapes/composition_1.py)
    * [Le programme COMPOSITION 2](./dessins/shapes/composition_2.py)
    * [Le programme JOLIGONES](./dessins/shapes/prettygon.py)

2. Dessins à partir de données (designs 34-49, [dessins/designs/designs_from_data.py](./dessins/designs/designs_from_data.py))
    * [Le programme CHEVAL](./dessins/shapes/horse.py)
    * Les programmes [LION](./dessins/shapes/lion.py), [OISEAUX-POISSONS](./dessins/shapes/bird_fish.py), [SMURF](./dessins/shapes/smurf.py)

3. Dragons de papiers pliés (designs 50-64, [dessins/designs/folding_paper_dragons.py](./dessins/designs/folding_paper_dragons.py))
    * [Le programme DRAGONS](./dessins/shapes/dragon.py)

4. Étoiles fractales (designs 65-77, [dessins/designs/fractal_stars.py](./dessins/designs/fractal_stars.py))
    * [Le programme ÉTOILES FRACTALES](./dessins/shapes/fractal_star.py)

5. Courbes (designs 78-100, [dessins/designs/curves.py](./dessins/designs/curves.py))
    * [Le programme COURBES ORBITALES](./dessins/shapes/orbiting_curves.py)
    * [Le programme COURBES TOURNANTES](./dessins/shapes/rotating_curves.py)
    * [Le programme COURBES SPIRALES](./dessins/shapes/spiraling_curves.py)

6. Dessins linéaires (designs 101-114, [dessins/designs/linear_designs.py](./dessins/designs/linear_designs.py))
    * [Le programme BIPARTI COMPLET](./dessins/shapes/complete_bipartite_graph.py)
    * [Le programme LINÉAIRES MODULO](./dessins/shapes/linear_modulo.py)
    * [Le programme LINÉAIRES BÂTONS](./dessins/shapes/linear_sticks.py)

7. Fractales simples (designs 115-163, [dessins/designs/simple_fractals.py](./dessins/designs/simple_fractals.py))
    * [Le programme FRACTALES SIMPLES](./dessins/shapes/simple_fractal.py)
    * [Le programme FRACTALES SIMPLES ARRONDIES](./dessins/shapes/simple_fractal_rounded.py)
    * [Le programme FRACTALES SIMPLES DÉFORMÉES](./dessins/shapes/simple_fractal_deformed.py)

8. Quadrillages élastiques (designs 164-176, [dessins/designs/elastic_grids.py](./dessins/designs/elastic_grids.py))
    * [Le programme QUADRILLAGES ÉLASTIQUES](./dessins/shapes/elastic_grid.py)

9. Surfaces (designs 177-200, [dessins/designs/surfaces.py](./dessins/designs/surfaces.py))
    * [Le programme SURFACES](./dessins/shapes/surface.py)

10. La troisième dimension (designs 201-252, [dessins/designs/third_dimension.py](./dessins/designs/third_dimension.py))
    * [Le programme D3DATA](./dessins/shapes/d3data.py)
    * [Le programme D3CUBE](./dessins/shapes/d3cube.py)
    * [Le programme D3STRUCTURES](./dessins/shapes/d3structures.py)

## Gallery
| | |
| --- | --- |
| ![Stars](/img/stars_1.png) | ![Stars](/img/stars_2.png) |
| ![Spirals](/img/spirals_1.png) | ![Spirals](/img/spirals_2.png) |
| ![Horses](/img/horses.png) | ![Elastic grid](/img/grids_1.png) |
| ![Cubes](/img/cubes.png) | ![Torus](/img/torus.png) |
