"""Pure geometry: smooth a path and cover it with polygons. No turtle, no CAD library."""

import math

Path = list[tuple[float, float]]
Polygon = list[tuple[float, float]]


def catmull_rom(a: float, b: float, c: float, d: float, t: float) -> float:
    """Evaluate the uniform Catmull-Rom segment between b and c at parameter t."""
    return 0.5 * (2 * b + (c - a) * t + (2 * a - 5 * b + 4 * c - d) * t * t + (3 * b - a - 3 * c + d) * t * t * t)


def smooth_path(path: Path, subdivisions: int = 4) -> Path:
    """Interpolate a Catmull-Rom spline through the points; endpoints are clamped and kept."""
    if len(path) < 3:
        return list(path)

    padded = [path[0], *path, path[-1]]
    smoothed: Path = []

    for i in range(1, len(padded) - 2):
        p0, p1, p2, p3 = padded[i - 1], padded[i], padded[i + 1], padded[i + 2]
        for k in range(subdivisions):
            t = k / subdivisions
            smoothed.append(
                (catmull_rom(p0[0], p1[0], p2[0], p3[0], t), catmull_rom(p0[1], p1[1], p2[1], p3[1], t))
            )

    smoothed.append(path[-1])
    return smoothed


def circle_polygon(center: tuple[float, float], radius: float, segments: int) -> Polygon:
    return [
        (center[0] + radius * math.cos(2 * math.pi * k / segments), center[1] + radius * math.sin(2 * math.pi * k / segments))
        for k in range(segments)
    ]


def stroke_polygons(path: Path, width: float) -> list[Polygon]:
    """Cover a path with one rectangle per segment and one circle per vertex: round joins and caps."""
    radius = width / 2
    segments = max(8, round(16 * math.sqrt(width / 3.5)))
    polygons: list[Polygon] = []

    for a, b in zip(path, path[1:]):
        dx, dy = b[0] - a[0], b[1] - a[1]
        length = math.hypot(dx, dy)
        if length == 0:
            continue
        # left normal; the corners run counter-clockwise so the fill rule keeps the rectangle
        nx, ny = -dy / length * radius, dx / length * radius
        polygons.append([(a[0] - nx, a[1] - ny), (b[0] - nx, b[1] - ny), (b[0] + nx, b[1] + ny), (a[0] + nx, a[1] + ny)])

    for point in path:
        polygons.append(circle_polygon(point, radius, segments))

    return polygons
