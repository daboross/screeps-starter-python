# noinspection PyPep8Naming
from typing import Optional, Type, Union, Dict, List

from .memory import _Memory
from .room import Room, RoomPosition
from .structures import Structure
from .creep import Creep


# noinspection PyPep8Naming
class _Effect:  # type: List[_Effect]
    """
    Applied effects, an array of objects with the following properties

    :type effect: int
    :type level: int
    :type ticksRemaining: int
    """
    def __init__(self, effect: int, level: Optional[int], ticksRemaining: int):
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        self.effect = effect
        self.level = level
        self.ticksRemaining = ticksRemaining


_Effect = List[_Effect]


# noinspection PyPep8Naming
class RoomObject:
    """
    Any object with a position in a room. Almost all game objects prototypes are derived from RoomObject.

    :type effects: _Effect
    :type pos: RoomPosition
    :type room: Room
    """

    def __init__(self, effects: _Effect,  pos: RoomPosition, room: Room) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        self.effects = effects
        self.pos = pos
        self.room = room


# noinspection PyPep8Naming
class Flag(RoomObject):
    """
    :type effects: _Effect
    :type room: Room | None
    :type color: int
    :type memory: _Memory
    :type name: str
    :type secondaryColor: int
    """
    prototype = None  # type: Type[Flag]

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Optional[Room], color: int, memory: _Memory,
                 name: str, secondaryColor: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room)
        self.color = color
        self.memory = memory
        self.name = name
        self.secondaryColor = secondaryColor

    def remove(self) -> int:
        pass

    def setColor(self, color: int, secondaryColor: int = None) -> int:
        pass

    def setPosition(self, x: Union[int, RoomPosition, RoomObject], y: int = None) -> int:
        pass

    @property
    def hint(self) -> int:
        return 0


Flag.prototype = Flag


# noinspection PyPep8Naming
class Source(RoomObject):
    """
    :type energy: int
    :type energyCapacity: int
    :type id: str
    :type ticksToRegeneration: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Optional[Room], energy: int, energyCapacity: int, _id: str,
                 ticksToRegeneration: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room)
        self.energy = energy
        self.energyCapacity = energyCapacity
        self.id = _id
        self.ticksToRegeneration = ticksToRegeneration


# noinspection PyPep8Naming
class Mineral(RoomObject):
    """
    :type density: int
    :type mineralAmount: int
    :type mineralType: str
    :type id: str
    :type ticksToRegeneration: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Optional[Room], density: int, mineralAmount: int, mineralType: str,
                 _id: str, ticksToRegeneration: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room)
        self.density = density
        self.mineralAmount = mineralAmount
        self.mineralType = mineralType
        self.id = _id
        self.ticksToRegeneration = ticksToRegeneration


# noinspection PyPep8Naming
class Resource(RoomObject):
    """
    :type amount: int
    :type id: str
    :type resourceType: str
    """

    def __init__(self, effects: _Effect, pos: RoomPosition,
                 room: Room, _id: str, amount: int, resourceType: str) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room)
        self.id = _id
        self.amount = amount
        self.resourceType = resourceType


# noinspection PyPep8Naming
class Store:
    """
    WARNING: This constructor is purely for type completion, and does not exist in the game.
    """
    def getCapacity(self, resource: str = None) -> Union[Dict[str, int], int]:
        pass

    def getFreeCapacity(self, resource: str = None) -> Union[Dict[str, int], int]:
        pass

    def getUsedCapacity(self, resource: str = None) -> Union[Dict[str, int], int]:
        pass


# noinspection PyPep8Naming
class Ruin(RoomObject):
    """
    :type destroyTime: int
    :type id: str
    :type store: dict[str, int]
    :type _Structure: Structure
    :type ticksToDecay: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Optional[Room], destroyTime: int, _id: str,
                 store: Dict[str, int], _Structure: Structure, ticksToDecay: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room)
        self.destroyTime = destroyTime
        self.id = _id
        self.store = store
        self.Structure = _Structure
        self.ticksToDecay = ticksToDecay


# noinspection PyPep8Naming
class Tombstone(RoomObject):
    """
    :type deathTime: int
    :type id: str
    :type store: dict[str, int]
    :type _Structure: Structure
    :type ticksToDecay: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Optional[Room],
                 creep: Creep, deathTime: int, _id: str,
                 store: Store, ticksToDecay: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room)
        self.creep = creep
        self.deathTime = deathTime
        self.id = _id
        self.store = store
        self.ticksToDecay = ticksToDecay
