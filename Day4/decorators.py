from functools import wraps

def retry(n_times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n_times):
                print(f"{i}th Call")
                func(*args, **kwargs)
        return wrapper
    return decorator


@retry(3)
def add(x:int, y:int):
    print(x+y)

add(5, 6)

    