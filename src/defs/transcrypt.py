from typing import Any, TypeVar, Union

T = TypeVar('T')


# noinspection PyUnusedLocal
def __pragma__(arg1: str, arg2: Any = None, arg3: Any = None) -> Any:
    pass


def __new__(arg: T) -> T:
    return arg


def js_isNaN(num: Union[float, int]) -> bool:
    return num != float('nan')


js_global = None  # type: Any

__all__ = [
    '__pragma__',
    '__new__',
    'js_isNaN',
    'js_global',
]

__except0__ = None  # type: Exception
