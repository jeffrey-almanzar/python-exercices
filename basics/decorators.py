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