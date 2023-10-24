from collections.abc import Callable
from typing import Any, TypeAlias
from .monad import Monad


class EitherMonad(Monad):
    pass


class Left(EitherMonad):

    def bind(self, func: Callable[..., "Either"], *args: tuple, **kwargs: dict[str, Any]) -> "Either":
        return func(self._value, *args, **kwargs)


class Right(EitherMonad):

    def bind(self, func: Callable[..., "Either"], *args: tuple, **kwargs: dict[str, Any]) -> "Either":
        try:
            return func(self._value, *args, **kwargs)
        except Exception as error:
            return Left(value=f"{error.__class__.__name__} : {error}")


Either: TypeAlias = Left | Right
