from collections.abc import Callable
from typing import Any, Self
from .monad import Monad


# class Reader(Monad):

#     def exceute(self, env: Any, *args: tuple, **kwargs: dict[str, Any]):
#         return self._value(env, *args, **kwargs)

#     def bind(self, func: Callable, *args: tuple, **kwargs: dict[str, Any]) -> "Reader":
#         return Reader(lambda env: func(self.exceute(env)).exceute(env))

# class Reader:
#     def __init__(self, func=None):
#         self.func = func

#     def run(self, env):
#         return self.func(env)

#     @staticmethod
#     def ask():
#         return Reader(lambda env: env)

#     def map(self, fn):
#         return Reader(lambda env: fn(self.run(env)))

#     def flat_map(self, fn):
#         return Reader(lambda env: fn(self.run(env)).run(env))


class Reader(Monad):

    def run(self: Self, env: dict[str, Any], *args: tuple, **kwargs: dict[str, Any]):
        return self._value(env)

    def bind(self: Self, func: Callable, *args: tuple, **kwargs: dict[str, Any]) -> "Reader":
        return Reader(lambda env: func(self.run(env)).run(env))

    def excecute(self, env: dict[str, Any], *args: tuple, **kwargs: dict[str, Any]):
        return self.run(env)
