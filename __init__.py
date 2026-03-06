"""
TopoLens — Blender 5.0+ Addon
==============================
GPU overlay that highlights Tris, Quads, and Ngons with different colors in Edit Mode.

Panel at: View3D > Sidebar (N) > TopoLens
"""

bl_info = {
    "name": "TopoLens",
    "author": "JordanRO2",
    "version": (1, 1, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > TopoLens",
    "description": "GPU overlay to visualize Tris, Quads, and Ngons in Edit Mode",
    "category": "Mesh",
}

import bpy
from . import overlay


def register():
    overlay.register()


def unregister():
    overlay.unregister()


if __name__ == "__main__":
    register()
