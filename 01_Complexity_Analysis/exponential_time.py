# O(2^n) - Exponential Time Complexity
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
n = 5
print(f"Fibonacci({n}):", fibonacci(n))
