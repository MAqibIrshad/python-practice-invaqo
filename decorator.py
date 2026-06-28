from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator
def mid_func():
    """
    Hello
    """
    print(f"Returning Mid Value")


print(mid_func.__name__)
print(mid_func.__doc__)


def repeat(times):
    def deco(func):
        def wrap(text):
            for _ in range(times):
                func(text)
        return wrap
    return deco

@repeat(5)
def greet(text):
    print(text)

greet("AOA")

