import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        retVal = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end-start} seconds.")
        return retVal
    return wrapper