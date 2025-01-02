# Parametrized decorators. Definition and use cases.
# When python creates and executes decorators
# Standard library decorators:
#   wraps
#   cache
#   cached_property
#   lru_cache
#   contextmanager
# How to call decorator and parametrized decorator without @
# Closures:
#   definition and usecases, nonlocal usecases

def param_deco(x: int, y: int):
    def inner(func):
        def wrapper(*args, **kwargs):
            print("this is a parametrized decorator")
            print(f"It was called with {x} and {y}")
            func(*args, **kwargs)
        return wrapper
    return inner

@param_deco(1, 2)
def adder(x: int) -> int:
    return x+2

print(adder(2))

# Decorators are called at the starttime not at the runtime, in the inner function is then executed at runtime

from functools import wraps, cache, cached_property
from time import perf_counter
from contextlib import contextmanager

def wraps_dec_example(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Calling wraps example decorator")
        func(*args, **kwargs)
    return inner

@wraps_dec_example
def new_adder(x: int) -> int:
    """Test docstring"""
    return x+1

print(new_adder.__name__)
print(new_adder.__doc__)


# Cache is a thin wrapper around a dictionary lookup
def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        res = func(*args, **kwargs)
        print(f"Elapse time: {perf_counter()-start_time}")
        return res
    return wrapper

@time_function
@cache
def factorial(n: int) -> int:
    print(f"Finding factorial of {n}")
    factorial = 1
    for i in range(2, n+1):
        factorial*= i
    return factorial


factorial(50000)
factorial(50000)

# Difference with lru cache you can set the size, ex. number of calls

# Works as a cache for the property decorator, for ex. if you need some computation
#   for setting a variable you could use cached_property


class CPropertyExample:
    def __init__(self, item_list) -> None:
        self.item_list = item_list

    @cached_property
    @time_function
    def calculate_sum_cached(self):
        print("cached property calculate")
        return sum(self.item_list)

    @time_function
    def calculate_sum(self):
        print("no cache calculate")
        return sum(self.item_list)

array = [i for i in range(100000)]
x = CPropertyExample(array)

x.calculate_sum()
x.calculate_sum()
x.calculate_sum()

x.calculate_sum_cached
x.calculate_sum_cached
x.calculate_sum_cached

@contextmanager
def ctx_function(x: int):
    print("i am doing something")
    try:
        print(x)
        x=-1
        yield 
    finally:
        print("I am done") 

with ctx_function(2) as ct:
    print("hello") 
