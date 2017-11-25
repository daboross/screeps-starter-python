# noinspection PyPep8Naming
from typing import Optional, Type, Union

from .memory import _Memory
from .room import Room, RoomPosition


class RoomObject:
    """
    :type pos: RoomPosition
    :type room: Room
    """

    def __init__(self, pos: RoomPosition, room: Room) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        self.pos = pos
        self.room = room


# noinspection PyPep8Naming
class Flag(RoomObject):
    """
    :type room: Room | None
    :type color: int
    :type secondaryColor: int
    :type memory: _Memory
    :type name: str
    """
    prototype = None  # type: Type[Flag]

    def __init__(self, pos: RoomPosition, room: Optional[Room], color: int, secondaryColor: int,
                 memory: _Memory, name: str) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(pos, room)
        self.color = color
        self.secondaryColor = secondaryColor
        self.memory = memory
        self.name = name

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

    def __init__(self, pos: RoomPosition, room: Optional[Room], density: int, mineralAmount: int, mineralType: str,
                 _id: str, ticksToRegeneration: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(pos, room)
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

    def __init__(self, pos: RoomPosition, room: Room, _id: str, amount: int, resourceType: str) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(pos, room)
        self.id = _id
        self.amount = amount
        self.resourceType = resourceType
