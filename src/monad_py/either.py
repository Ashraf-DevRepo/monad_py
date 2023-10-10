from typing import Any, Callable, Self
from .monad import Monad


class Either(Monad):

    def right(self, func: Callable, *args, **kwargs) -> Self | "Left" | "Right":
        try:
            return self if isinstance(self, Left) else func(self._value, *args, **kwargs)
        except Exception as error:
            return Left(str(error))

    def left(self, func: Callable, *args, **kwargs) -> Self | "Left" | "Right":
        try:
            return self if isinstance(self, Right) else func(self._value, *args, **kwargs)
        except Exception as error:
            return Left(str(error))

    def unit(self, *args, **kwargs) -> Any:
        return self._value


class Left(Either):
    pass


class Right(Either):
    pass
