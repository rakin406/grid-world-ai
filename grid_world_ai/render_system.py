"""System for rendering entities in the world."""

from constants import *
import pecs
from pyray import *


class RenderSystem:
    def __init__(self, registry: pecs.Registry):
        self.registry = registry

    def display(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        while not window_should_close():
            begin_drawing()
            clear_background(WHITE)
            draw_text("Hello world", 190, 200, 20, VIOLET)
            end_drawing()
        close_window()
