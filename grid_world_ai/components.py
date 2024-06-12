"""Global components for entities."""

from dataclasses import dataclass


@dataclass
class Grid:
    slices: int
    spacing: float
