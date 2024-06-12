import random
from constants import *
import pyray as pr


class AI:
    def __init__(self, grid_slices: int, grid_spacing: int,
                 goal_state: tuple[int, int]):
        self.grid_slices = grid_slices
        self.grid_spacing = grid_spacing
        self.goal_state = goal_state
        self.state = self.random_state()    # Initial state of the agent

    def random_state(self):
        while True:
            state = (random.randrange(0, WINDOW_WIDTH, self.grid_spacing),
                     random.randrange(0, WINDOW_HEIGHT, self.grid_spacing))
            if state != self.goal_state:
                return state

    def reset(self):
        """Resets agent state to a random coordinate."""
        self.state = self.random_state()
        return self.state

    def draw(self):
        pr.draw_rectangle(self.state[0], self.state[1], self.grid_spacing,
                          self.grid_spacing, pr.BLUE)
