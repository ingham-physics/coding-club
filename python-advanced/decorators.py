"""Some examples of decorators in Python
"""

from time import time

from functools import lru_cache


def timer_func(func):
    def wrap_func(*args, **kwargs):
        time_point_1 = time()

        result = func(*args, **kwargs)

        time_point_2 = time()
        print(
            f"Function {func.__name__!r} executed in {(time_point_2-time_point_1):.4f}s"
        )
        return result

    return wrap_func


@lru_cache
def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case


@timer_func
def get_fib_of(n):
    return fibonacci_of(n)


if __name__ == "__main__":

    fib_n = 35
    fib_result = get_fib_of(fib_n)
    print(f"Fibonacci of {fib_n}: {fib_result}")
