import random
from enum import IntEnum
from constants import *
import numpy as np
import pyray as pr


class AI:
    """This class uses Q-learning algorithm."""

    class Action(IntEnum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3

    def __init__(self, grid_slices: int, grid_spacing: int,
                 goal_state: tuple[int, int]):
        self.grid_slices = grid_slices
        self.grid_spacing = grid_spacing
        self.goal_state = goal_state
        self.state = self.random_state()    # Initial state of the agent

        # Learning parameters
        self.alpha = 0.1         # Learning rate
        self.gamma = 0.5         # Discount factor
        self.epsilon = 1.0       # Initial exploration rate
        self.min_epsilon = 0.01  # Minimum exploration rate
        self.decay_rate = 0.99
        self.total_episodes = 10000

        self.q_table = np.zeros(
            (self.grid_slices, self.grid_slices, len(self.Action)))

        self.training = True
        self.new_episode = False
        self.current_episode = 0
        self.old_state = self.state

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

    def coord_to_indices(self, coords: tuple[int, int]) -> tuple[int, int]:
        """Converts screen coordinates to grid indices."""
        grid_index_x = coords[0] // self.grid_spacing
        grid_index_y = coords[1] // self.grid_spacing
        return (grid_index_x, grid_index_y)

    def choose_action(self, grid_indices: tuple[int, int]) -> Action:
        """Epsilon-greedy action selection"""
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(list(self.Action))   # Explore

        # Exploit
        return np.argmax(self.q_table[grid_indices[0], grid_indices[1]])

    def decay_epsilon(self):
        """Decays exploration rate."""
        self.epsilon = max(self.min_epsilon, self.epsilon * self.decay_rate)

    def train(self):
        if self.training:
            # TODO: Print episode 0 once.
            # if self.current_episode == 0:
            #     self.old_state = self.reset()

            if self.new_episode:
                self.current_episode += 1
                self.old_state = self.reset()
                self.decay_epsilon()
                self.new_episode = False
                print(f"Episode: {self.current_episode}")

            # Convert screen coordinates to grid indices
            grid_indices = self.coord_to_indices(self.old_state)

            action = self.choose_action(grid_indices)

            next_state, reward, self.new_episode = self.step(action)
            next_indices = self.coord_to_indices(next_state)

            # Update Q-value
            old_value = self.q_table[grid_indices[0], grid_indices[1], action]
            next_max = np.max(self.q_table[next_indices[0], next_indices[1]])

            new_value = old_value + self.alpha * (reward + self.gamma *
                                                  next_max - old_value)
            self.q_table[grid_indices[0], grid_indices[1], action] = new_value

            self.old_state = next_state

            # Stop training if episodes are completed
            if self.current_episode >= self.total_episodes:
                self.training = False
                print("Training complete!")

    def draw(self):
        pr.draw_rectangle(self.state[0], self.state[1], self.grid_spacing,
                          self.grid_spacing, pr.BLUE)
