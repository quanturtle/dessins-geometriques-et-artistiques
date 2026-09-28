from pathlib import Path

from build123d import *

OUTPUT_DIR = Path("output")


def generate_cad(pts: list[tuple[float, float]], name: str | None) -> None:
    with BuildPart() as part:
        with BuildSketch(Plane.XZ) as s:
            with BuildLine() as l:
                l1 = Polyline(*pts)

            trace(line_width=3.5)

        extrude(amount=10)

    try:
        OUTPUT_DIR.mkdir(exist_ok=True)
        filename = OUTPUT_DIR / f"{name or 'my_design'}.stl"
        export_stl(part.part, str(filename))
    except Exception as err:
        print(f"Error exporting STL: {err}")

    return
