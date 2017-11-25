from typing import Any, Callable, Dict, Generic, Iterable, Iterator, List, Optional, Tuple, TypeVar, Union

_K = TypeVar('_K')
_V = TypeVar('_V')


# noinspection PyPep8Naming
class Object:
    """
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object
    """

    @classmethod
    def assign(cls, target: Any, *sources: Any) -> None:
        pass

    @classmethod
    def create(cls, proto: Any, propertiesObject: Any = None) -> None:
        pass

    @classmethod
    def defineProperties(cls, obj: Any, props: Dict[str, Any]) -> None:
        pass

    @classmethod
    def defineProperty(cls, obj: Any, prop: str, descriptor: Dict[str, Any]) -> None:
        pass

    @classmethod
    def freeze(cls, obj: Any) -> None:
        pass

    @classmethod
    def keys(cls, obj: Dict[_K, _V]) -> List[_K]:
        pass


class Math:
    """
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math
    """

    @staticmethod
    def abs(x: Union[int, float]) -> Union[int, float]:
        pass

    @staticmethod
    def exp(x: Union[int, float]) -> Union[int, float]:
        pass

    @staticmethod
    def sign(x: Union[int, float]) -> int:
        pass

    @staticmethod
    def random() -> float:
        pass

    @staticmethod
    def floor(x: Union[int, float]) -> int:
        pass


# noinspection PyPep8Naming
class String:
    @staticmethod
    def fromCodePoint(number: int) -> str:
        pass


# noinspection PyUnusedLocal
def typeof(x: Any) -> str:
    pass


# noinspection PyUnusedLocal
def require(name: str) -> Any:
    pass


class JSON:
    @classmethod
    def parse(cls, s: str) -> Dict[str, Any]:
        pass

    @classmethod
    def stringify(cls, v: Any, _filter: Any = None, indent: int = 0) -> str:
        pass


this = None  # type: Any


# noinspection PyPep8Naming,PyShadowingBuiltins
class module:
    # noinspection PyPep8Naming
    class exports:
        loop = None  # type: Optional[Callable[[], None]]


class RegExp(str):
    def __init__(self, regex: str, args: Optional[str] = None) -> None:
        """
        NOTE: In order to use this, you must surround it with `__new__`: `__new__(RegExp(expression))`
        """
        super().__init__(regex)
        self.ignoreCase = False
        self.js_global = False
        self.multiline = False

        self.source = regex

        if args is not None:
            for char in args:
                if char == 'i':
                    self.ignoreCase = True
                elif char == 'g':
                    self.js_global = True
                elif char == 'm':
                    self.multiline = True

    def __new__(cls, regex: str, args: Optional[str] = None) -> 'RegExp':
        return RegExp(regex, args)

    def exec(self, string: str) -> Optional[List[str]]:
        pass

    def test(self, string: str) -> bool:
        pass


_T = TypeVar('_T')


class Array(list):
    @staticmethod
    def js_from(v: Iterable[_T]) -> List[_T]:
        pass


# noinspection PyPep8Naming
class console:
    @staticmethod
    def log(string: str) -> None:
        pass

    @staticmethod
    def addVisual(roomName: str, data: Any) -> None:
        pass

    @staticmethod
    def getVisualSize(roomName: str) -> int:
        pass

    @staticmethod
    def clearVisual(roomName: str) -> None:
        pass


K = TypeVar("K")
V = TypeVar("V")


class Map(Generic[K, V]):
    def __init__(self, iterable: Optional[List[Tuple[K, V]]] = None) -> None:
        """
        NOTE: In order to use this, you must surround it with `__new__`: `__new__(Map(iterable))`
        """
        pass

    @property
    def size(self) -> int:
        return 0

    def clear(self) -> None:
        pass

    def delete(self, key: K) -> None:
        pass

    def entries(self) -> Iterator[Tuple[K, V]]:
        pass

    def forEach(self, callback: Callable[[V, K, 'Map[K, V]'], None]) -> None:
        pass

    def get(self, key: K) -> Optional[V]:
        pass

    def has(self, key: K) -> bool:
        pass

    def keys(self) -> Iterator[K]:
        pass

    def set(self, key: K, value: V) -> 'Map[K, V]':
        pass

    def values(self) -> Iterator[V]:
        pass


class Set(Generic[K]):
    def __init__(self, iterable: Optional[List[K]] = None) -> None:
        """
        NOTE: In order to use this, you must surround it with `__new__`: `__new__(Set(iterable))`
        """
        pass

    def has(self, key: K) -> bool:
        pass

    def add(self, key: K) -> None:
        pass

    def delete(self, key: K) -> None:
        pass

    def keys(self) -> Iterable[K]:
        pass

    def values(self) -> Iterable[K]:
        pass

    def js_clear(self) -> None:
        pass

    @property
    def size(self) -> int:
        return 0


Infinity = float('inf')

undefined = None  # type: None

__all__ = [
    "Object",
    "Math",
    "String",
    "typeof",
    "require",
    "JSON",
    "this",
    "module",
    "RegExp",
    "Array",
    "console",
    "Map",
    "Set",
    "Infinity",
    "undefined",
]
