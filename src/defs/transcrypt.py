from typing import Any, Union, TypeVar

T = TypeVar('T')


def __new__(arg: T) -> T:
    return arg


# noinspection PyPep8Naming
def js_isNaN(num: Union[float, int, str]) -> bool:
    return float(num) != float('nan')


class Uint8Array(Any):
    """
    WARNING: This is just here for autocompletion.
    If anyone feels like typing this go for it :) - Lisp
    """


js_global = None  # type: Any

__except0__ = None  # type: Exception

__all__ = [
    '__new__',
    'js_isNaN',
    'js_global',
    '__except0__',
    'Uint8Array',
]
