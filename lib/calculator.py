import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def mean(self, numbers):
        return sum(numbers) / len(numbers)

    def standard_deviation(self, numbers):
        avg = self.mean(numbers)
        variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
        return math.sqrt(variance)

    def summary_statistics(self, numbers):
        return {
            "mean": self.mean(numbers),
            "standard_deviation": self.standard_deviation(numbers),
        }
