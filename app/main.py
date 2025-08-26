from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_with_args = (func, args)
        if func_with_args in cash_results:
            print("Getting from cache")
        else:
            cash_results[func_with_args] = func(*args, *kwargs)
            print("Calculating new result")
        return cash_results[func_with_args]

    return wrapper
