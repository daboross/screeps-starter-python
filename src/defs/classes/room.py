from typing import Any, Callable, Dict, List, Optional, Type, Union

from .memory import _Memory
from .misc_obj import RoomObject
from .structures import StructureController, StructureStorage, StructureTerminal


# noinspection PyPep8Naming
class RoomPosition:
    """
    :type x: int
    :type y: int
    :type roomName: str
    :type prototype: Type[RoomPosition]
    # used for the common (pos.pos or pos).. trick for accepting RoomObject and RoomPosition
    """
    prototype = None  # type: Type[RoomPosition]

    def __init__(self, x: int, y: int, roomName: str) -> None:
        self.x = x
        self.y = y
        self.roomName = roomName

    def createConstructionSite(self, structureType: str) -> int:
        pass

    def createFlag(self, name: str = None, color: str = None, secondaryColor: str = None) -> int:
        pass

    def findClosestByPath(self, source: _FindParameter, opts: Dict[str, Any]) -> Optional[RoomObject]:
        pass

    def findClosestByRange(self, source: _FindParameter, opts: Dict[str, Any]) -> Optional[RoomObject]:
        pass

    def findInRange(self, source: _FindParameter, _range: int, opts: Dict[str, Any]) -> List[RoomObject]:
        pass

    def getDirectionTo(self, x: Union[int, 'RoomPosition', RoomObject], y: int = None) -> int:
        pass

    def getRangeTo(self, x: Union[int, 'RoomPosition', RoomObject], y: int = None) -> int:
        pass

    def inRangeTo(self, x: Union[int, 'RoomPosition', RoomObject], y_or_range: int = None,
                  _range: int = None) -> bool:
        pass

    def isEqualTo(self, x: Union[int, 'RoomPosition', RoomObject], y: int = None) -> bool:
        pass

    def isNearTo(self, x: Union[int, 'RoomPosition', RoomObject], y: int = None) -> bool:
        pass

    def look(self) -> List[Dict[str, Any]]:
        pass

    def lookFor(self, _type: str) -> List[RoomObject]:
        pass


RoomPosition.prototype = RoomPosition

_HasPosition = Union['RoomPosition', 'RoomObject']
_FindParameter = Union[int, List[_HasPosition]]


class _Owner:
    """
    :type username: str
    """

    def __init__(self, username: str) -> None:
        self.username = username


class _PathPos:
    """
    :type x: int
    :type y: int
    :type dx: int
    :type dy: int
    :type direction: int
    """

    def __init__(self, x: int, y: int, dx: int, dy: int, direction: int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.direction = direction


# noinspection PyPep8Naming
class Room:
    """
    :type controller: Optional[StructureController]
    :type storage: Optional[StructureStorage]
    :type terminal: Optional[StructureTerminal]
    :type energyAvailable: int
    :type energyCapacityAvailable: int
    :type memory: _Memory
    :type mode: str
    :type name: str
    :type visual: Any
    """

    def __init__(self, controller: Optional[StructureController], storage: Optional[StructureStorage],
                 terminal: Optional[StructureTerminal], energyAvailable: int, energyCapacityAvailable: int,
                 memory: _Memory, mode: str, name: str, visual: Any) -> None:
        self.controller = controller
        self.storage = storage
        self.terminal = terminal
        self.energyAvailable = energyAvailable
        self.energyCapacityAvailable = energyCapacityAvailable
        self.memory = memory
        self.mode = mode
        self.name = name
        self.visual = visual

    @classmethod
    def serializePath(cls, path: List[Dict[str, Union[_PathPos, Dict[str, Any]]]]) -> str:
        pass

    @classmethod
    def deserializePath(cls, path: str) -> List[Union[_PathPos, Dict[str, Any]]]:
        pass

    def createConstructionSite(self, x: Union[int, RoomPosition, RoomObject], y: Union[int, str],
                               structureType: str = None) -> int:
        pass

    def createFlag(self, pos: Union[RoomPosition, RoomObject], name: str = None, color: int = None,
                   secondaryColor: int = None) -> Union[str, int]:
        pass

    def find(self, _type: _FindParameter, opts: Dict[str, Callable[[RoomObject], bool]] = None) -> List[RoomObject]:
        pass

    def findExitTo(self, room: str) -> int:
        pass

    def findPath(self, fromPos: RoomPosition, toPos: RoomPosition, opts: Dict[str, Any]) \
            -> List[Union[_PathPos, Dict[str, Any]]]:
        pass

    def getPositionAt(self, x: int, y: int) -> RoomPosition:
        pass

    def lookAt(self, x: Union[int, RoomPosition, RoomObject], y: int = None) -> List[Dict[str, Any]]:
        pass

    def lookAtArea(self, top: int, left: int, bottom: int, right: int, asArray: bool = False) \
            -> Union[List[Dict[str, Any]], Dict[int, Dict[int, Dict[str, Any]]]]:
        pass

    def lookForAt(self, _type: str, x: Union[int, RoomPosition, RoomObject], y: int = None) -> List[RoomObject]:
        pass

    def lookForAtArea(self, _type: str, top: int, left: int, bottom: int, right: int, asArray: bool = False) \
            -> Union[List[Dict[str, RoomObject]], Dict[int, Dict[int, Dict[str, RoomObject]]]]:
        pass
