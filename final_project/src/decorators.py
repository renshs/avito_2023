from functools import wraps
from random import randint


def log(template="Pizza will be cooked in {} minutes!"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) == 0:
                func()
            else:
                func(*args)
            time: int = randint(25, 30)
            print(template.format(time))

        return wrapper

    return decorator
