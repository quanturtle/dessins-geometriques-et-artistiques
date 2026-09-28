"""Build the solid with manifold3d and write it as a binary STL."""

import struct
from dataclasses import dataclass
from pathlib import Path as FilePath

import numpy as np
from manifold3d import CrossSection, Error, Manifold, OpType

from .geometry import Path, smooth_path, stroke_polygons


@dataclass(frozen=True)
class Mesh:
    """Triangle mesh: vertices as an (n, 3) float array, triangles as an (m, 3) index array."""

    vertices: np.ndarray
    triangles: np.ndarray


def build_model(paths: list[Path], width: float, depth: float, smooth: bool) -> Mesh:
    """Stroke every path, union the polygons in 2D, and extrude the outline by depth along Z."""
    polygons = []
    for path in paths:
        if smooth:
            path = smooth_path(path)
        polygons.extend(stroke_polygons(path, width))

    outline = CrossSection.batch_boolean([CrossSection([polygon]) for polygon in polygons], OpType.Add)
    solid = Manifold.extrude(outline, depth)
    if solid.status() != Error.NoError:
        raise ValueError(f"manifold3d could not build the solid: {solid.status()}")

    mesh = solid.to_mesh()
    return Mesh(np.asarray(mesh.vert_properties)[:, :3], np.asarray(mesh.tri_verts))


def write_stl(mesh: Mesh, file: FilePath) -> None:
    """Write the mesh as binary STL: 80-byte header, triangle count, 50 bytes per triangle."""
    corners = mesh.vertices[mesh.triangles]
    normals = np.cross(corners[:, 1] - corners[:, 0], corners[:, 2] - corners[:, 0])
    normals /= np.maximum(np.linalg.norm(normals, axis=1, keepdims=True), 1e-12)

    records = np.zeros(len(corners), dtype=[("normal", "<f4", 3), ("corners", "<f4", (3, 3)), ("attributes", "<u2")])
    records["normal"] = normals
    records["corners"] = corners

    file.parent.mkdir(parents=True, exist_ok=True)
    with open(file, "wb") as f:
        f.write(b"\0" * 80)
        f.write(struct.pack("<I", len(corners)))
        f.write(records.tobytes())
    return
