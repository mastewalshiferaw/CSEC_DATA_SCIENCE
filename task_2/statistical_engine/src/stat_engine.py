import math
from typing import List, Union

class StatEngine:
    def __init__(self, data: List[Union[int, float]]):
        if not data:
            raise ValueError("Data list cannot be empty.")
        
        # Data cleaning: Only accept integers and floats
        self.data = []
        for x in data:
            if not isinstance(x, (int, float)):
                raise TypeError(f"Invalid data type detected: {type(x)}. Only int/float allowed.")
            self.data.append(float(x))
        self.data.sort()

    def get_mean(self) -> float:
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def get_mode(self) -> Union[List[float], str]:
        counts = {x: self.data.count(x) for x in set(self.data)}
        max_freq = max(counts.values())
        if max_freq == 1:
            return "All values are unique."
        return [k for k, v in counts.items() if v == max_freq]

    def get_variance(self, is_sample: bool = True) -> float:
        n = len(self.data)
        if n < 2 and is_sample:
            return 0.0
        mean = self.get_mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]
        return sum(squared_diffs) / (n - 1 if is_sample else n)

    def get_standard_deviation(self, is_sample: bool = True) -> float:
        return math.sqrt(self.get_variance(is_sample))

    def get_outliers(self, threshold: float = 2.0) -> List[float]:
        mean = self.get_mean()
        std = self.get_standard_deviation(is_sample=True)
        return [x for x in self.data if abs(x - mean) > (threshold * std)]