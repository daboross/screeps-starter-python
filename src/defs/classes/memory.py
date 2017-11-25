from typing import Any, Dict, List, Optional, Union

__all__ = ['Memory', 'RawMemory', '_Memory', '_MemoryValue']

_MemoryValue = Union[str, int, float, bool, '_Memory', List['_MemoryValue'], None]


class _Memory(dict):
    def __getattr__(self, key: str) -> _MemoryValue:
        pass

    def __setattr__(self, key: str, value: _MemoryValue) -> None:
        pass


Memory = _Memory()


class _ForeignSegment:
    """
    :type username: str
    :type id: int
    :type data: str
    """

    def __init__(self, username: str, _id: int, data: str) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        self.data = data
        self.username = username
        self.id = _id


# noinspection PyPep8Naming
class RawMemory:
    """
    :type segments: Dict[int, str]
    :type foreignSegment: _ForeignSegment | None
    """
    segments = {}  # type: Dict[int, str]
    foreignSegment = None  # type: Optional[_ForeignSegment]

    @classmethod
    def get(cls) -> str:
        pass

    @classmethod
    def set(cls, value: str) -> None:
        pass

    @classmethod
    def setActiveSegments(cls, ids: List[int]) -> None:
        pass

    @classmethod
    def setActiveForeignSegment(cls, username: Optional[str], _id: Optional[int] = None) -> None:
        pass

    @classmethod
    def setDefaultPublicSegment(cls, _id: Optional[int]) -> None:
        pass

    @classmethod
    def setPublicSegments(cls, ids: List[int]) -> None:
        pass
