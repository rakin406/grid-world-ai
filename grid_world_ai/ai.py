import random
from enum import Enum, auto
from constants import *
import numpy as np
import pyray as pr


class AI:
    """This class uses Q-learning algorithm."""

    class Action(Enum):
        UP = auto()
        DOWN = auto()
        LEFT = auto()
        RIGHT = auto()

    def __init__(self, grid_slices: int, grid_spacing: int,
                 goal_state: tuple[int, int]):
        self.grid_slices = grid_slices
        self.grid_spacing = grid_spacing
        self.goal_state = goal_state
        self.state = self.random_state()    # Initial state of the agent

        # Learning parameters
        self.alpha = 0.00025    # Learning rate
        self.gamma = 0.9        # Discount factor
        self.epsilon = 0.1      # Exploration rate
        self.total_episodes = 100000

        # 4 actions: up, down, left, right
        self.q_table = np.zeros((self.grid_slices, self.grid_slices, 4))

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

    def step(self, action: Action):
        next_state = ()

        if action == self.Action.UP:
            next_state = (self.state[0], max(
                self.state[1] - self.grid_spacing, 0))
        elif action == self.Action.DOWN:
            next_state = (self.state[0], min(self.state[1] + self.grid_spacing,
                                             WINDOW_HEIGHT - self.grid_spacing))
        elif action == self.Action.LEFT:
            next_state = (
                max(self.state[0] - self.grid_spacing, 0), self.state[1])
        elif action == self.Action.RIGHT:
            next_state = (min(self.state[0] + self.grid_spacing,
                              WINDOW_WIDTH - self.grid_spacing), self.state[1])

        reward = 1 if next_state == self.goal_state else -1
        done = next_state == self.goal_state
        self.state = next_state

        return next_state, reward, done

    def draw(self):
        pr.draw_rectangle(self.state[0], self.state[1], self.grid_spacing,
                          self.grid_spacing, pr.BLUE)
