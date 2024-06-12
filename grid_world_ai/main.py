from constants import *
from pyray import *
import pecs


def run():
    registry = pecs.Registry()

    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        draw_text("Hello world", 190, 200, 20, VIOLET)
        end_drawing()
    close_window()


if __name__ == "__main__":
    run()
