# def retry(n_times: int):
#     def decorator(func):
#         def wrapper():
#             for _ in range(n_times):
#                 try:
#                     func()
#                 except Exception:
#                     print(f"Exception")
#             raise("All fail")
#         return wrapper
#     return decorator
from functools import wraps

def retry(n_times:int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, n_times+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt Failed.Retrying...")
            raise Exception(f"All {n_times} attempts retries failed!") from last_exception
        return wrapper
    return decorator

@retry(3)
def divide():
    n = int(input("Enter n: "))
    d = int(input("Enter d: "))
    print(n/d)

divide()
