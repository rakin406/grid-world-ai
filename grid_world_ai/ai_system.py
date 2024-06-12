from components import Grid
import pecs


class AISystem:
    def __init__(self, registry: pecs.Registry, grid_slices: int,
                 grid_spacing: float):
        ai = registry.create()
        registry.emplace(ai, Grid(grid_slices, 5))
