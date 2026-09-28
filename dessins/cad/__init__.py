"""Pipeline from recorded turtle paths to a printable STL: record, smooth, stroke, extrude, write.

paths.py records with turtle, geometry.py is pure, export.py talks to manifold3d and the filesystem.
Import the edge modules directly so geometry stays importable without turtle or manifold3d.
"""
