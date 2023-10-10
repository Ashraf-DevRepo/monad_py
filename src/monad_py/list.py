import itertools
from typing import Any, Callable, Self

from .monad import Monad


class List(Monad):

    def bind(self, func: Callable, *args, **kwargs) -> Self:
        return List(list(itertools.chain(*list(map(func, self._value, *args, **kwargs)))))

    def unit(self, *args, **kwargs) -> Any:
        new_value = []
        for val in self._value:
            if isinstance(val, (list, tuple, set)):
                new_value.extend(list(val))
            else:
                new_value.append(val)
        contains_tuple = any(isinstance(item, tuple) for item in new_value)
        contains_set = any(isinstance(item, set) for item in new_value)
        contains_list = any(isinstance(item, list) for item in new_value)
        if any({contains_tuple, contains_set, contains_list}):
            return List(new_value).flat()
        return new_value
