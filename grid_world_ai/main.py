from constants import *
from pyray import *
import pecs


def find_grid_spacing(slices: int) -> float:
    return WINDOW_WIDTH / slices


def run():
    slices = int(input("Enter grid slices: ").strip() or DEFAULT_GRID_SLICES)
    spacing = find_grid_spacing(slices)

    registry = pecs.Registry()

    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        end_drawing()
    close_window()


if __name__ == "__main__":
    run()
