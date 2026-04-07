import random

def simulate_crashes(days: int, probability: float = 0.045) -> float:
    crashes = 0
    for _ in range(days):
        if random.random() < probability:
            crashes += 1
    return crashes / days