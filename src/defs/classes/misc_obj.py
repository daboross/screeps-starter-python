# noinspection PyPep8Naming
from typing import Optional, Type, Union, Dict

from .memory import _Memory
from .room import Room, RoomPosition
from .structures import Structure


class RoomObject:
    """
    Any object with a position in a room. Almost all game objects prototypes are derived from RoomObject.

    :type effects: [effect, level, ticksRemaining]
    :type pos: RoomPosition
    :type room: Room
    """

    def __init__(self, effects,  pos: RoomPosition, room: Room) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        self.effects = effects
        self.pos = pos
        self.room = room


# noinspection PyPep8Naming
class Flag(RoomObject):
    """
    :type room: Room | None
    :type color: int
    :type memory: _Memory
    :type name: str
    :type secondaryColor: int
    """
    prototype = None  # type: Type[Flag]

    def __init__(self, pos: RoomPosition, room: Optional[Room], color: int, memory: _Memory, name: str,
                 secondaryColor: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(pos, room)
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

    def __init__(self, pos: RoomPosition, room: Optional[Room], energy: int, energyCapacity: int, _id: str,
                 ticksToRegeneration: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(pos, room)
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

    def __init__(self, effects: RoomPosition, pos: RoomPosition, room: Optional[Room], density: int, mineralAmount: int, mineralType: str,
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

    def __init__(self, effects: RoomPosition, pos: RoomPosition, room: Room, _id: str, amount: int, resourceType: str) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room)
        self.id = _id
        self.amount = amount
        self.resourceType = resourceType


# noinspection PyPep8Naming
class Ruin(RoomObject):
    """
    :type destroyTime: int
    :type id: str
    :type store: dict[str, int]
    :type _Structure: Structure
    :type ticksToDecay: int
    """

    def __init__(self, effects: RoomPosition, pos: RoomPosition, room: Optional[Room], destroyTime: int, _id: str,
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
