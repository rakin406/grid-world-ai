from constants import *
import pyray as pr


def find_grid_spacing(slices: int) -> int:
    return WINDOW_WIDTH // slices


def draw_grid(slices: int, spacing: int):
    # Vertical lines
    x = spacing
    for _ in range(slices - 1):
        pr.draw_line(x, 0, x, WINDOW_HEIGHT, pr.BLACK)
        x += spacing

    # Horizontal lines
    y = spacing
    for _ in range(slices - 1):
        pr.draw_line(0, y, WINDOW_WIDTH, y, pr.BLACK)
        y += spacing


def run():
    slices = int(input("Enter grid slices: ").strip() or DEFAULT_GRID_SLICES)
    spacing = find_grid_spacing(slices)

    pr.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.WHITE)

        draw_grid(slices, spacing)

        pr.end_drawing()
    pr.close_window()


if __name__ == "__main__":
    run()
