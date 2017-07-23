from typing import Any, Callable, Dict, List, Optional, TypeVar, Union

_K = TypeVar('K')
_V = TypeVar('V')


# noinspection PyPep8Naming
class Object:
    """
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object
    """

    @classmethod
    def assign(cls, target: Any, *sources: Any):
        pass

    @classmethod
    def create(cls, proto: Any, propertiesObject: Any = None):
        pass

    @classmethod
    def defineProperties(cls, obj: Any, props: Dict[str, Any]):
        pass

    @classmethod
    def defineProperty(cls, obj: Any, prop: str, descriptor: Dict[str, Any]):
        pass

    @classmethod
    def freeze(cls, obj: Any):
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
    def stringify(cls, v: Any) -> str:
        pass


this = None  # type: Any


# noinspection PyPep8Naming,PyShadowingBuiltins
class module:
    # noinspection PyPep8Naming
    class exports:
        loop = None  # type: Optional[Callable[[], None]]


class RegExp(str):
    def __init__(self, regex: str, args: Optional[str] = None) -> None:
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

    def exec(self, string: str) -> Optional[List[str]]:
        pass

    def test(self, string: str) -> bool:
        pass


Infinity = float('inf')

undefined = None  # type: None
