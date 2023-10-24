from abc import ABC, abstractmethod
from typing import Any, Self
from collections.abc import Callable




class Monad(ABC):

    def __init__(self: Self, value: Any=None, *args: tuple, **kwargs: dict[str, Any]) -> None:
        self._value = value
        

    @abstractmethod
    def bind(self: Self, func: Callable, *args: tuple, **kwargs: dict[str, Any]) -> Any:
        ...

    def flatmap(self: Self, func: Callable, *args: tuple, **kwargs: dict[str, Any]) -> Self:
        return self.bind(func, *args, **kwargs)
    
    def __rshift__(self: Self, func: Callable, *args: tuple, **kwargs: dict[str, Any]) -> Self:
        return self.bind(func, *args, **kwargs)

    @property
    def unit(self: Self, *args: tuple, **kwargs: dict[str, Any]) -> Any:
        return self._value

    def __call__(self: Self, *args: tuple, **kwargs: dict[str, Any]) -> Any:
        return self._value
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._value})"
    def __str__(self) -> str:
        return f"{self._value}"


