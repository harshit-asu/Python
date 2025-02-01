from time import perf_counter

def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        ret_val = func(*args, **kwargs)
        end = perf_counter()
        print(f"Time taken by '{func.__name__}': {(end-start)} seconds")
        return ret_val
    return wrapper