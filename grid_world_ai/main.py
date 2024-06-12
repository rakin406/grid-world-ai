import random
from constants import *
from ai import AI
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
    grid_slices = int(input("Enter grid slices: ").strip()
                      or DEFAULT_GRID_SLICES)
    grid_spacing = find_grid_spacing(grid_slices)

    # Random (x, y) coordinates as goal
    goal_pos = (random.randrange(0, WINDOW_WIDTH, grid_spacing),
                random.randrange(0, WINDOW_HEIGHT, grid_spacing))

    pr.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    pr.set_target_fps(60)

    ai = AI(grid_slices, grid_spacing, goal_pos)

    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.WHITE)

        draw_grid(grid_slices, grid_spacing)

        # Draw goal
        pr.draw_rectangle(goal_pos[0], goal_pos[1], grid_spacing, grid_spacing,
                          pr.RED)

        ai.draw()

        pr.end_drawing()

    pr.close_window()


if __name__ == "__main__":
    run()
