# noinspection PyPep8Naming
from typing import Any, Dict, Optional, Union

from .room import Room, RoomPosition


class RoomObject:
    """
    :type pos: RoomPosition
    :type room: Room
    """

    def __init__(self, pos: RoomPosition, room: Room) -> None:
        self.pos = pos
        self.room = room


# noinspection PyPep8Naming
class Flag(RoomObject):
    """
    :type room: Room | None
    :type color: int
    :type secondaryColor: int
    :type memory: dict[str, Any]
    :type name: str
    """

    def __init__(self, pos: RoomPosition, room: Optional[Room], color: int, secondaryColor: int,
                 memory: Dict[str, Any], name: str) -> None:
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
                 id: str, ticksToRegeneration: int) -> None:
        super().__init__(pos, room)
        self.density = density
        self.mineralAmount = mineralAmount
        self.mineralType = mineralType
        self.id = id
        self.ticksToRegeneration = ticksToRegeneration


class Resource(RoomObject):
    """
    :type amount: int
    :type id: str
    :type resourceType: str
    """

    def __init__(self, pos: RoomPosition, room: Room, _id: str, amount: int, resourceType: str) -> None:
        super().__init__(pos, room)
        self.id = _id
        self.amount = amount
        self.resourceType = resourceType
