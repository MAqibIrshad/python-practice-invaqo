from functools import wraps

def caching():
    cache_dic = {}
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs))
            if key in cache_dic:
                return cache_dic[key]
            print(f"Computing Results...")
            result = func(*args, **kwargs)
            cache_dic[key] = result
            return result
        return wrapper
    return decorator

@caching
def add(a:int, b:int):
    return a + b

print(add(5, 6))
            

