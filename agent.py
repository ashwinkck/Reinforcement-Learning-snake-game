import torch
import random
import numpy as np
from collections import deque #data structure to store memories
from game import SnakeGameAI, Direction, Point

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        pass


    def get_state(self,game):
        pass


    def remember(self, state,action, reward, next_state, done):
        