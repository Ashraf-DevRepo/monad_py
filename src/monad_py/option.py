from .monad import Monad
from typing import Any, Self, TypeAlias
from collections.abc import Callable


class OptionMonad(Monad):
    pass


class Just(OptionMonad):
    def bind(self: Self, func: Callable[..., "Option"], *args: tuple, **kwargs: dict[str, Any]) -> "Option":
        return func(self._value, *args, **kwargs)


class Nothing(OptionMonad):
    def __init__(self: Self, value: Any = None, *args: tuple, **kwargs: dict[str, Any]) -> None:
        super().__init__(None, *args, **kwargs)

    def bind(self: Self, func: Callable[..., "Option"], *args: tuple, **kwargs: dict[str, Any]) -> "Option":
        return self


Option: TypeAlias = Just | Nothing
