from typing import Any, Callable, Dict, Generic, List, Optional, Tuple, Type, TypeVar, Union

_L1 = TypeVar('_L1')
_L2 = TypeVar('_L2')
_L3 = TypeVar('_L3', int, float)
_L4 = TypeVar('_L4')


# noinspection PyPep8Naming
class _LodashChain(Generic[_L1]):
    def __init__(self, value: Union[List[_L1], Dict[Any, _L1]]) -> None:
        self.__inner = value

    def concat(self, other: Union[List[_L1], Dict[Any, _L1]]) -> '_LodashChain[_L1]':
        pass

    def chunk(self, size: int = 1) -> '_LodashChain[List[_L1]]':
        pass

    def compact(self) -> '_LodashChain[_L1]':
        pass

    def difference(self, *other: List[_L1]) -> '_LodashChain[_L1]':
        pass

    def drop(self, n: int = 1) -> '_LodashChain[_L1]':
        pass

    def dropRight(self, n: int = 1) -> '_LodashChain[_L1]':
        pass

    def dropRightWhile(self,
                       predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                       thisArg: Any = None) -> '_LodashChain[_L1]':
        pass

    def dropWhile(self,
                  predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                  thisArg: Any = None) -> '_LodashChain[_L1]':
        pass

    def fill(self, value: _L1, start: int = 0, end: int = 0) -> '_LodashChain[_L1]':
        pass

    def first(self) -> Optional[_L1]:
        pass

    def flatten(self) -> '_LodashChain':
        pass

    def flattenDeep(self) -> '_LodashChain':
        pass

    def initial(self) -> List[_L1]:
        pass

    def intersection(self, arrays: List[List[_L1]]) -> '_LodashChain':
        pass

    def last(self) -> Optional[Any]:
        pass

    def lastIndexOf(self, value: _L1, fromIndex: Union[int, bool] = 0) -> int:
        pass

    def pull(self, values: List[_L1]) -> '_LodashChain':
        pass

    def pullAt(self, indices: List[int]) -> '_LodashChain':
        pass

    def remove(self, predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
               thisArg: Any = None) -> '_LodashChain':
        pass

    def rest(self) -> '_LodashChain':
        pass

    def slice(self, start: int = 0, end: int = 0) -> '_LodashChain':
        pass

    def sortedIndex(self,
                    value: _L1,
                    iteratee: Union[str, Callable[[_L1], _L2], None] = None,
                    thisArg: Any = None) -> int:
        pass

    def sortedLastIndex(self,
                        value: _L1,
                        iteratee: Union[str, Callable[[_L1], _L2], None] = None,
                        thisArg: Any = None) -> int:
        pass

    def take(self, n: int = 1) -> '_LodashChain':
        pass

    def takeRight(self, n: int = 1) -> '_LodashChain':
        pass

    def takeRightWhile(self,
                       predicate: Union[str, Callable[[_L1], _L2], None] = None,
                       thisArg: Any = None) -> '_LodashChain':
        pass

    def takeWhile(self,
                  predicate: Union[str, Callable[[_L1], _L2], None] = None,
                  thisArg: Any = None) -> '_LodashChain':
        pass

    def union(self, arrays: List[List[_L1]]) -> '_LodashChain':
        pass

    def unique(self,
               isSorted: bool = False,
               iteratee: Union[str, Callable[[_L1], _L2], None] = None,
               thisArg: Any = None) -> List[_L1]:
        pass

    def uniq(self,
             isSorted: bool = False,
             iteratee: Union[str, Callable[[_L1], _L2], None] = None,
             thisArg: Any = None) -> List[_L1]:
        pass

    def unzip(self) -> '_LodashChain':
        pass

    def unzipWith(self,
                  iteratee: Optional[Callable[[Any, Any, Any, Any], Any]] = None,
                  thisArg: Any = None) -> '_LodashChain':
        pass

    def without(self, values: List[_L1]) -> '_LodashChain':
        pass

    def xor(self, arrays: List[List[_L1]]) -> '_LodashChain':
        pass

    def zip(self) -> '_LodashChain':
        pass

    def zipObject(self, values: Optional[List[Any]] = None) -> '_LodashChain':
        pass

    def zipWith(self,
                iteratee: Optional[Callable[[Any, Any, Any, Any], None]] = None,
                thisArg: Any = None) -> '_LodashChain':
        pass

    def all(self, predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
            thisArg: Any = None) -> bool:
        pass

    def any(self, predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
            thisArg: Any = None) -> bool:
        pass

    def at(self, *props: Any) -> List[_L1]:
        pass

    def countBy(self, iteratee: Union[str, Callable[[_L1], _L2], None] = None, thisArg: Any = None) -> '_LodashChain':
        pass

    def every(self,
              predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
              thisArg: Any = None) -> bool:
        pass

    def filter(self,
               predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
               thisArg: Any = None) -> '_LodashChain[_L1]':
        pass

    def find(self,
             predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
             thisArg: Any = None) -> _L1:
        pass

    def findLast(self,
                 predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                 thisArg: Any = None) -> _L1:
        pass

    def findWhere(self,
                  predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                  thisArg: Any = None) -> _L1:
        pass

    def forEach(self, iteratee: Callable[[_L1], Optional[bool]] = None, thisArg: Any = None) -> '_LodashChain[_L1]':
        pass

    def forEachRight(self,
                     iteratee: Callable[[_L1], Optional[bool]] = None,
                     thisArg: Any = None) -> '_LodashChain[_L1]':
        pass

    def groupBy(self, iteratee: Union[str, Callable[[_L1], _L2], None] = None, thisArg: Any = None) -> '_LodashChain':
        pass

    def includes(self, value: _L1, fromIndex: int = 0) -> bool:
        pass

    def indexBy(self, iteratee: Union[str, Callable[[_L1], _L2], None] = None, thisArg: Any = None) -> Dict[str, _L1]:
        pass

    def invoke(self, path: str, *args: Any) -> '_LodashChain':
        pass

    def map(self, iteratee: Union[str, Callable[[_L1], _L2], None] = None, thisArg: Any = None) -> '_LodashChain':
        pass

    def partition(self,
                  predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                  thisArg: Any = None) -> '_LodashChain':
        pass

    def pluck(self, path: Union[str, List[str]]) -> '_LodashChain':
        pass

    def reduce(self,
               iteratee: Callable[[_L2, _L1], _L2] = None, accumulator: _L2 = None,
               thisArg: Any = None) -> _L2:
        pass

    def reduceRight(self,
                    iteratee: Callable[[_L2, _L1], _L2] = None, accumulator: _L2 = None,
                    thisArg: Any = None) -> _L2:
        pass

    def reject(self,
               predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
               thisArg: Any = None) -> '_LodashChain':
        pass

    def sample(self) -> Any:
        pass

    def shuffle(self) -> '_LodashChain':
        pass

    def size(self) -> int:
        pass

    def some(self,
             predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
             thisArg: Any = None) -> bool:
        pass

    def sortBy(self, iteratee: Union[str, Callable[[_L1], _L2], None] = None, thisArg: Any = None) -> '_LodashChain':
        pass

    def sortByAll(self, *iteratee: Union[str, Callable[[_L1], _L2], None]) -> '_LodashChain':
        pass

    def sortByOrder(self, iteratees: List[Union[str, Callable[[_L1], _L2], None]], orders: List[str]) -> '_LodashChain':
        pass

    def where(self, source: Any) -> '_LodashChain':
        pass

    def toArray(self) -> '_LodashChain':
        pass

    def toPlainObject(self) -> '_LodashChain':
        pass

    def sum(self, iteratee: Union[str, Callable[[_L1], _L2], None] = None, thisArg: Any = None) -> _L2:
        pass

    def keys(self) -> '_LodashChain':
        pass

    def mapKeys(self, iteratee: Callable[[str], str] = None, thisArg: Any = None) -> '_LodashChain':
        pass

    def mapValues(self, iteratee: Callable[[Any], Any] = None, thisArg: Any = None) -> '_LodashChain':
        pass

    def omit(self,
             predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str],
             thisArg: Any = None) -> '_LodashChain':
        pass

    def pairs(self) -> '_LodashChain':
        pass

    def values(self) -> '_LodashChain':
        pass

    def value(self) -> Any:
        pass

    def max(self, iteratee: Callable[[_L1], _L3] = None, thisArg: Any = None) -> _L1:
        pass

    def min(self, iteratee: Callable[[_L1], _L3] = None, thisArg: Any = None) -> _L1:
        pass


# noinspection PyPep8Naming
class _:
    def __new__(cls, value: Union[List[_L1], Dict[Any, _L1]]) -> _LodashChain[_L1]:
        return _LodashChain(value)

    @staticmethod
    def chunk(array: List[_L1], size: int = 1) -> List[List[_L1]]:
        pass

    @staticmethod
    def compact(array: List[_L1]) -> List[_L1]:
        pass

    @staticmethod
    def difference(array: List[_L1], *other: List[_L1]) -> List[_L1]:
        pass

    @staticmethod
    def drop(array: List[_L1], n: int = 1) -> List[_L1]:
        pass

    @staticmethod
    def dropRight(array: List[_L1], n: int = 1) -> List[_L1]:
        pass

    @staticmethod
    def dropRightWhile(array: List[_L1],
                       predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                       thisArg: Any = None) -> List[_L1]:
        pass

    @staticmethod
    def dropWhile(array: List[_L1],
                  predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                  thisArg: Any = None) -> List[_L1]:
        pass

    @staticmethod
    def fill(array: List[_L1], value: _L1, start: int = 0, end: int = 0) -> List[_L1]:
        pass

    @staticmethod
    def findIndex(array: List[_L1],
                  predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                  thisArg: Any = None) -> int:
        pass

    @staticmethod
    def findLastIndex(array: List[_L1],
                      predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                      thisArg: Any = None) -> int:
        pass

    @staticmethod
    def first(array: List[_L1]) -> Optional[_L1]:
        pass

    @staticmethod
    def flatten(array: List[List[_L1]]) -> List[_L1]:
        pass

    @staticmethod
    def flattenDeep(array: List[Any]) -> List[Any]:
        pass

    @staticmethod
    def indexOf(array: List[_L1], value: _L1, fromIndex: Union[int, bool] = 0) -> int:
        pass

    @staticmethod
    def initial(array: List[_L1]) -> List[_L1]:
        pass

    @staticmethod
    def intersection(array: List[List[_L1]]) -> List[_L1]:
        pass

    @staticmethod
    def last(array: List[_L1]) -> Optional[_L1]:
        pass

    @staticmethod
    def lastIndexOf(array: List[_L1], value: _L1, fromIndex: Union[int, bool] = 0) -> int:
        pass

    @staticmethod
    def pull(array: List[_L1], *values: _L1) -> List[_L1]:
        pass

    @staticmethod
    def pullAt(array: List[_L1], indices: List[int]) -> List[_L1]:
        pass

    @staticmethod
    def remove(array: List[_L1],
               predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
               thisArg: Any = None) -> List[_L1]:
        pass

    @staticmethod
    def rest(array: List[_L1]) -> List[_L1]:
        pass

    @staticmethod
    def slice(array: List[_L1], start: int = 0, end: int = 0) -> List[_L1]:
        pass

    @staticmethod
    def sortedIndex(array: List[_L1],
                    value: _L1,
                    iteratee: Union[str, Callable[[_L1], _L2], None] = None,
                    thisArg: Any = None) -> int:
        pass

    @staticmethod
    def sortedLastIndex(array: List[_L1],
                        value: _L1,
                        iteratee: Union[str, Callable[[_L1], _L2], None] = None,
                        thisArg: Any = None) -> int:
        pass

    @staticmethod
    def take(array: List[_L1], n: int = 1) -> List[_L1]:
        pass

    @staticmethod
    def takeRight(array: List[_L1], n: int = 1) -> List[_L1]:
        pass

    @staticmethod
    def takeRightWhile(array: List[_L1],
                       predicate: Union[str, Callable[[_L1], _L2], None] = None,
                       thisArg: Any = None) -> List[_L1]:
        pass

    @staticmethod
    def takeWhile(array: List[_L1],
                  predicate: Union[str, Callable[[_L1], _L2], None] = None,
                  thisArg: Any = None) -> List[_L1]:
        pass

    @staticmethod
    def union(array: List[List[_L1]]) -> List[_L1]:
        pass

    @staticmethod
    def unique(array: List[_L1],
               isSorted: bool = False,
               iteratee: Union[str, Callable[[_L1], _L2], None] = None,
               thisArg: Any = None) -> List[_L1]:
        pass

    @staticmethod
    def uniq(array: List[_L1],
             isSorted: bool = False,
             iteratee: Union[str, Callable[[_L1], _L2], None] = None,
             thisArg: Any = None) -> List[_L1]:
        pass

    @staticmethod
    def unzip(array: List[Any]) -> List[Any]:
        pass

    @staticmethod
    def unzipWith(array: List[Any],
                  iteratee: Optional[Callable[[Any, Any, Any, Any], Any]] = None,
                  thisArg: Any = None) -> List[Any]:
        pass

    @staticmethod
    def without(array: List[_L1], values: List[_L1]) -> List[_L1]:
        pass

    @staticmethod
    def xor(array: List[List[_L1]]) -> List[_L1]:
        pass

    @staticmethod
    def zip(array: List[Any]) -> List[Any]:
        pass

    @staticmethod
    def zipObject(props: List[Any], values: Optional[List[Any]] = None) -> Any:
        pass

    @staticmethod
    def zipWith(array: List[Any],
                iteratee: Optional[Callable[[Any, Any, Any, Any], None]] = None,
                thisArg: Any = None) -> List[Any]:
        pass

    @staticmethod
    def all(collection: List[_L1],
            predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
            thisArg: Any = None) -> bool:
        pass

    @staticmethod
    def any(collection: Union[List[_L1], Dict[Any, _L1]],
            predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
            thisArg: Any = None) -> bool:
        pass

    @staticmethod
    def at(collection: Union[List[_L1], Dict[Any, _L1]], *props: Any) -> List[_L1]:
        pass

    @staticmethod
    def countBy(collection: Union[List[_L1], Dict[Any, _L1]],
                iteratee: Union[str, Callable[[_L1], _L2], None] = None,
                thisArg: Any = None) -> Dict[_L2, int]:
        pass

    @staticmethod
    def every(collection: Union[List[_L1], Dict[Any, _L1]],
              predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
              thisArg: Any = None) -> bool:
        pass

    @staticmethod
    def filter(collection: Union[List[_L1], Dict[Any, _L1]],
               predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
               thisArg: Any = None) -> List[_L1]:
        pass

    @staticmethod
    def find(collection: Union[List[_L1], Dict[Any, _L1]],
             predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
             thisArg: Any = None) -> _L1:
        pass

    @staticmethod
    def findLast(collection: Union[List[_L1], Dict[Any, _L1]],
                 predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                 thisArg: Any = None) -> _L1:
        pass

    @staticmethod
    def findWhere(collection: Any,
                  predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                  thisArg: Any = None) -> _L1:
        pass

    @staticmethod
    def groupBy(collection: Union[List[_L1], Dict[Any, _L1]],
                iteratee: Union[str, Callable[[_L1], _L2], None] = None,
                thisArg: Any = None) -> Dict[_L2, List[_L1]]:
        pass

    @staticmethod
    def includes(collection: Union[List[_L1], Dict[Any, _L1], str], value: _L1, fromIndex: int = 0) -> bool:
        pass

    @staticmethod
    def indexBy(collection: Union[List[_L1], Dict[Any, _L1]],
                iteratee: Union[str, Callable[[_L1], _L2], None] = None,
                thisArg: Any = None) -> Dict[str, _L1]:
        pass

    @staticmethod
    def invoke(collection: Union[List[_L1], Dict[Any, _L1]], path: str, *args: Any) -> Any:
        pass

    @staticmethod
    def map(collection: Union[List[_L1], Dict[Any, _L1]],
            iteratee: Union[str, Callable[[_L1], _L2], None] = None,
            thisArg: Any = None) -> List[_L2]:
        pass

    @staticmethod
    def partition(collection: Union[List[_L1], Dict[Any, _L1]],
                  predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                  thisArg: Any = None) -> Tuple[List[_L1], List[_L1]]:
        pass

    @staticmethod
    def pluck(collection: Union[List[_L1], Dict[Any, _L1]], path: Union[str, List[str]]) -> List[Any]:
        pass

    @staticmethod
    def reduce(collection: Union[List[_L1], Dict[Any, _L1]],
               iteratee: Callable[[_L2, _L1], _L2] = None,
               accumulator: _L2 = None,
               thisArg: Any = None) -> _L2:
        pass

    @staticmethod
    def reduceRight(collection: Union[List[_L1], Dict[Any, _L1]],
                    iteratee: Callable[[_L2, _L1], _L2] = None,
                    accumulator: _L2 = None,
                    thisArg: Any = None) -> _L2:
        pass

    @staticmethod
    def reject(collection: Union[List[_L1], Dict[Any, _L1]],
               predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
               thisArg: Any = None) -> List[
        _L1]:
        pass

    @staticmethod
    def sample(collection: Union[List[_L1], Dict[Any, _L1]]) -> _L1:
        pass

    @staticmethod
    def shuffle(collection: Union[List[_L1], Dict[Any, _L1]]) -> List[_L1]:
        pass

    @staticmethod
    def size(collection: Optional[Union[List[_L1], Dict[Any, _L1]]]) -> int:
        pass

    @staticmethod
    def some(collection: Union[List[_L1], Dict[Any, _L1]],
             predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
             thisArg: Any = None) -> bool:
        pass

    @staticmethod
    def sortBy(collection: Union[List[_L1], Dict[Any, _L1]],
               iteratee: Union[str, Callable[[_L1], _L2], None] = None,
               thisArg: Any = None) -> List[_L1]:
        pass

    @staticmethod
    def sortByAll(collection: Union[List[_L1], Dict[Any, _L1]],
                  *iteratee: Union[str, Callable[[_L1], _L2], None]) -> List[_L1]:
        pass

    @staticmethod
    def sortByOrder(collection: Union[List[_L1], Dict[Any, _L1]],
                    iteratees: List[Union[str, Callable[[_L1], _L2], None]],
                    orders: List[str]) -> List[_L1]:
        pass

    @staticmethod
    def where(collection: Union[List[_L1], Dict[Any, _L1]], source: Any) -> List[_L1]:
        pass

    @staticmethod
    def clone(value: _L1) -> _L1:
        pass

    @staticmethod
    def cloneDeep(value: _L1) -> _L1:
        pass

    @staticmethod
    def gt(value: Any, other: Any) -> bool:
        pass

    @staticmethod
    def gte(value: Any, other: Any) -> bool:
        pass

    @staticmethod
    def isArguments(value: Any) -> bool:
        pass

    @staticmethod
    def isArray(value: Any) -> bool:
        pass

    @staticmethod
    def isBoolean(value: Any) -> bool:
        pass

    @staticmethod
    def isDate(value: Any) -> bool:
        pass

    @staticmethod
    def isElement(value: Any) -> bool:
        pass

    @staticmethod
    def isEmpty(value: Any) -> bool:
        pass

    @staticmethod
    def isEqual(value: Any, other: Any) -> bool:
        pass

    @staticmethod
    def isError(value: Any) -> bool:
        pass

    @staticmethod
    def isFinite(value: Any) -> bool:
        pass

    @staticmethod
    def isFunction(value: Any) -> bool:
        pass

    @staticmethod
    def isMatch(value: Any) -> bool:
        pass

    @staticmethod
    def isNaN(value: Any) -> bool:
        pass

    @staticmethod
    def isNative(value: Any) -> bool:
        pass

    @staticmethod
    def isNull(value: Any) -> bool:
        pass

    @staticmethod
    def isNumber(value: Any) -> bool:
        pass

    @staticmethod
    def isObject(value: Any) -> bool:
        pass

    @staticmethod
    def isPlainObject(value: Any) -> bool:
        pass

    @staticmethod
    def isRegExp(value: Any) -> bool:
        pass

    @staticmethod
    def isString(value: Any) -> bool:
        pass

    @staticmethod
    def isTypedArray(value: Any) -> bool:
        pass

    @staticmethod
    def isUndefined(value: Any) -> bool:
        pass

    @staticmethod
    def lt(value: Any, other: Any) -> bool:
        pass

    @staticmethod
    def lte(value: Any, other: Any) -> bool:
        pass

    @staticmethod
    def toArray(value: Any) -> List[Any]:
        pass

    @staticmethod
    def toPlainObject(value: Any) -> Any:
        pass

    @staticmethod
    def add(augend: Union[int, float], addend: Union[int, float]) -> Union[int, float]:
        pass

    @staticmethod
    def ceil(n: Union[int, float], precision: int = 0) -> Union[int, float]:
        pass

    @staticmethod
    def floor(n: Union[int, float], precision: int = 0) -> Union[int, float]:
        pass

    @staticmethod
    def max(collection: Union[List[_L1], Dict[Any, _L1]],
            iteratee: Union[str, Callable[[_L1], Any], None] = lambda x: x,
            thisArg: Any = None) -> _L1:
        pass

    @staticmethod
    def min(collection: Union[List[_L1], Dict[Any, _L1]],
            iteratee: Union[str, Callable[[_L1], Any], None] = lambda x: x,
            thisArg: Any = None) -> _L1:
        pass

    @staticmethod
    def round(n: Union[int, float], precision: int = 0) -> Union[int, float]:
        pass

    @staticmethod
    def sum(collection: Union[List[_L1], Dict[Any, _L1]],
            iteratee: Union[str, Callable[[_L1], _L2], None] = None,
            thisArg: Any = None) -> _L2:
        pass

    @staticmethod
    def extend(_object: Any, *sources: Any) -> Any:
        pass

    @staticmethod
    def assign(_object: Any, *sources: Any) -> Any:
        pass

    @staticmethod
    def create(prototype: Type[_L1], properties: Any = None) -> _L1:
        pass

    @staticmethod
    def defaults(_object: Any, *sources: Any) -> Any:
        pass

    @staticmethod
    def defaultsDeep(_object: Any, *sources: Any) -> Any:
        pass

    @staticmethod
    def findKey(_object: Any,
                predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                thisArg: Any = None) -> str:
        pass

    @staticmethod
    def findLastKey(_object: Any,
                    predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str] = None,
                    thisArg: Any = None) -> str:
        pass

    @staticmethod
    def forIn(_object: _L4, iteratee: Callable[[_L1], Optional[bool]] = None, thisArg: Any = None) -> _L4:
        pass

    @staticmethod
    def forInRight(_object: _L4, iteratee: Callable[[_L1], Optional[bool]] = None, thisArg: Any = None) -> _L4:
        pass

    @staticmethod
    def forOwn(_object: _L4, iteratee: Callable[[_L1], Optional[bool]] = None, thisArg: Any = None) -> _L4:
        pass

    @staticmethod
    def functions(_object: Any) -> List[str]:
        pass

    @staticmethod
    def get(_object: Any, path: Union[str, List[str]], defaultValue: _L1 = None) -> _L1:
        pass

    @staticmethod
    def has(_object: Any, path: str) -> bool:
        pass

    @staticmethod
    def invert(_object: Any) -> Dict[str, str]:
        pass

    @staticmethod
    def keys(_object: Any) -> List[str]:
        pass

    @staticmethod
    def keysIn(_object: Any) -> List[str]:
        pass

    @staticmethod
    def mapKeys(_object: Any, iteratee: Callable[[str], str] = None, thisArg: Any = None) -> Any:
        pass

    @staticmethod
    def mapValues(_object: Any, iteratee: Callable[[Any], Any] = None, thisArg: Any = None) -> Any:
        pass

    @staticmethod
    def merge(_object: Any, *sources: Any) -> Any:
        pass

    @staticmethod
    def omit(_object: Any,
             predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str],
             thisArg: Any = None) -> Any:
        pass

    @staticmethod
    def pairs(_object: Any) -> List[Tuple[str, Any]]:
        pass

    @staticmethod
    def pick(_object: Any,
             predicate: Union[Dict[str, Any], Callable[[_L1], bool], None, str],
             thisArg: Any = None) -> Any:
        pass

    @staticmethod
    def result(_object: Any, path: str, defaultValue: _L1 = None) -> _L1:
        pass

    @staticmethod
    def set(_object: _L4, path: str, value: Any) -> _L4:
        pass

    @staticmethod
    def transform(_object: Any,
                  iteratee: Callable[[_L2, _L1], _L2] = None,
                  accumulator: _L2 = None,
                  thisArg: Any = None) -> _L2:
        pass

    @staticmethod
    def values(_object: Union[Dict[str, _L2], Any]) -> List[_L2]:
        pass

    @staticmethod
    def valuesIn(_object: Union[Dict[str, _L2], Any]) -> List[_L2]:
        pass

    @staticmethod
    def random(minimum: int, maximum: int) -> int:
        pass
