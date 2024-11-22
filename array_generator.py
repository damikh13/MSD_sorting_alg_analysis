import random

class SimpleInputGenerator:
    def __init__(self, min_value=0, max_value=2**32-1):
        self.min_value = min_value
        self.max_value = max_value
    def generate_data(self, size):
        return [random.randint(self.min_value, self.max_value) for _ in range(size)]