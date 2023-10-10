from typing import Any, Optional

class Monad:

    def __init__(self, value: Optional[Any] = None, *args, **kwargs) -> None:
        self._value: Any = value
        return None

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._value})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._value})"