from typing import Any, Callable, Self
from .monad import Monad


class Option(Monad):
    def bind(self, func: Callable, *args, **kwargs) -> Self:
        return self if self._value is None else self.__class__(value=(func(self._value, *args, **kwargs)))

    def unit(self, *args, **kwargs) -> Any:
        return self._value
