import time

def time_func_decorator(func):
    # *args - for a tuple of args
    # **kwargs - for a dictionary, key value pairs
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        start = time.time()
        func()
        end = time.time()
        print(f"function {func.__name__} took {end - start} seconds")
    return wrapper

@time_func_decorator
def sample_func():
    i = 0
    while i < 1000000:
        i += 1

    print("done")


sample_func()


def positive_nums_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                return False
        return True
    return wrapper

@positive_nums_decorator
def sum(a, b):
    return a + b

print(sum(10, 10))


## Class decorator

def log_methods(cls):
    # Get all methods of the class
    for name, method in vars(cls).items():
        # Check if it's a method (excluding __dunder__ methods)
        if callable(method) and not name.startswith("__"):
            # Create a wrapper function to log method calls
            def wrapper(self, *args, **kwargs):
                print(f"Calling {name} with args: {args}, kwargs: {kwargs}")
                result = method(self, *args, **kwargs)
                print(f"{name} returned: {result}")
                return result
            
            # Replace the original method with the wrapper
            setattr(cls, name, wrapper)
    
    return cls

# Applying the class decorator
@log_methods
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

# Using the decorated class
calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(8, 2))


