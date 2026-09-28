from pathlib import Path as FilePath

from build123d import *

from .paths import Path

OUTPUT_DIR = FilePath("output")


def generate_cad(paths: list[Path], name: str | None) -> None:
    with BuildPart() as part:
        with BuildSketch(Plane.XZ) as s:
            with BuildLine() as l:
                for path in paths:
                    Polyline(*path)

            trace(line_width=3.5)

        extrude(amount=10)

    try:
        OUTPUT_DIR.mkdir(exist_ok=True)
        filename = OUTPUT_DIR / f"{name or 'my_design'}.stl"
        export_stl(part.part, str(filename))
    except Exception as err:
        print(f"Error exporting STL: {err}")

    return
