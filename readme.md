# Reinforcement Learning Snake Game

This project implements an AI agent that learns to play the classic Snake game using Reinforcement Learning. It uses Deep Q-Learning built with PyTorch and Pygame for the game environment.

## Overview

The AI agent learns to play the game through trial and error, balancing exploration (trying new moves) and exploitation (using known moves to maximize rewards).

### State Representation (11 Inputs)
The agent makes decisions based on an 11-dimensional state space:
- **Danger Detection (3):** Danger straight, danger right, danger left
- **Current Direction (4):** Moving left, right, up, down
- **Food Location (4):** Food is left relative to the head, right, up, down

### Actions (3 Outputs)
The model outputs a 3-dimensional vector representing the next move:
- `[1, 0, 0]`: Continue straight
- `[0, 1, 0]`: Turn right
- `[0, 0, 1]`: Turn left

### Neural Network
The agent uses a Feed Forward Neural Network consisting of:
- Input layer: 11 nodes (state space)
- Hidden layer: 256 nodes
- Output layer: 3 nodes (actions)

### Deep Q-Learning
The training process utilizes the Bellman Equation to update Q-values. The model uses:
- Replay Memory (`deque`) for training on past experiences (short and long term memory)
- Adam Optimizer
- Mean Squared Error (MSE) loss function

## Project Structure

- `agent.py`: Contains the main reinforcement learning logic, state extraction, and the training loop.
- `model.py`: Defines the PyTorch Neural Network (`Linear_QNet`) and the Q-Learning trainer (`QTrainer`).
- `snakegame.py`: The Pygame environment built for the AI to interact with.
- `snake_game_human.py`: A playable version of the game for humans.
- `helper.py`: Utility functions for plotting the training progress.



## Dependencies
- Python 3.x
- PyTorch
- Pygame
- NumPy
- Matplotlib
