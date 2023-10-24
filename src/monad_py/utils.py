from functools import reduce, wraps
from typing import Any, Callable, Sequence


def curry(func: Callable):
    @wraps(func)
    def curried(*args: tuple, **kwargs: dict[str, Any]):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *args2, **kwargs2: curried(*args, *args2, **kwargs, **kwargs2)
    return curried

def compose(func_list:Sequence[Callable]):
    def composed(x):
        return reduce(lambda acc, func: func(acc), reversed(func_list), x)
    return composed

def pipe(value:Any, func_list:Sequence[Callable]):
    return reduce(lambda acc, func: func(acc), func_list, value)
