from collections.abc import Callable
from typing import Any, Self, TypeAlias

from .monad import Monad

Log: TypeAlias = list[str] | str


class Writer(Monad):

    def __init__(self: Self, value: Any = None, log: list[str] | None = None, *args: tuple, **kwargs: dict[str, Any]) -> None:
        super().__init__(value, *args, **kwargs)
        self.log = log or []

    def write(self, log: Log, *args: tuple, **kwargs: dict[str, Any]) -> Self:
        if isinstance(log, str):
            self.log.append(log)
        if isinstance(log, list):
            self.log.extend(log)
        return self

    def bind(self: Self, func: Callable[..., tuple[Any, Log]], *args: tuple, **kwargs: dict[str, Any]) -> "Writer":
        result, log = func(self._value, *args, **kwargs)
        return Writer(result, self.log).write(log)

    def result(self: Self, *args: tuple, **kwargs: dict[str, Any]) -> tuple[Any, list[str]]:
        return self._value, self.log

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._value}, {self.log})"
