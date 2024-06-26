# Grid World AI
This is a 2D demonstration of a grid with a goal coordinate (red square) and an
AI that tries to reach the goal (blue square). The program first asks for input
regarding the size of the grid or the grid slices. The default number of grid
slices is 5.

The algorithm used for the AI is called [Q-learning](https://en.wikipedia.org/wiki/Q-learning).
It is a reinforcement learning algorithm and doesn't require a model. It learns
through trial and error. The training is a long process and takes even longer if
the grid is large. The number of training episodes is 10000.

> [!WARNING]
> If you get an `IndexError`, please use a different grid slice.

## Getting Started

### Dependencies

* Python
* Poetry

### Executing program

```bash
git clone https://github.com/rakin406/grid-world-ai.git
cd grid-world-ai
poetry install
poetry run python grid_world_ai/main.py
```

## Author

Rakin Rahman

## License

This project is licensed under the MIT License - see the LICENSE file for details
