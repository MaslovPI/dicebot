import random

from classes.rollresult import RollResult


def roll(dimensions):
    if dimensions < 1:
        raise ValueError(f"Wrong dimensions: {dimensions}")
    return random.randint(1, dimensions)


def roll_multiple(number, dimensions):
    if number < 1:
        raise ValueError(f"Wrong number: {dimensions}")
    return RollResult(roll(dimensions) for _ in range(number))
