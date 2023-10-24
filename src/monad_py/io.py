from collections.abc import Callable
from typing import Any, Self
from .monad import Monad


class IO(Monad):

    def bind(self: Self, func: Callable, *args: tuple, **kwargs: dict[str, Any]) -> "IO":
        return IO(value=lambda: func(self._value, *args, **kwargs))

    def run(self):
        return self._value()
