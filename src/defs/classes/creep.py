from typing import Any, ClassVar, Dict, List, Optional, Union

from .memory import _Memory
from .misc_obj import Mineral, Resource, RoomObject, Source, Store
from .room import Room, RoomPosition, _Owner
from .structures import ConstructionSite, Structure, StructureController


class _CreepPart:
    """
    :type boost: str | None
    :type type: str
    :type hits: int
    """

    def __init__(self, _type: str, hits: int, boost: Optional[str]) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        self.type = _type
        self.hits = hits
        self.boost = boost


# noinspection PyPep8Naming
class Creep(RoomObject):
    """
    :type body: list[_CreepPart]
    :type fatigue: int
    :type hits: int
    :type hitsMax: int
    :type id: str
    :type memory: _Memory
    :type my: bool
    :type name: str
    :type owner: _Owner
    :type saying: Optional[str]
    :type spawning: bool
    :type store: Store
    :type ticksToLive: int
    """

    prototype = None  # type: ClassVar[Any]

    def __init__(self, pos: RoomPosition, room: Room, body: List[_CreepPart], fatigue: int,
                 hits: int, hitsMax: int, _id: str, memory: _Memory, my: bool, name: str,
                 owner: _Owner, saying: Optional[str], spawning: bool, store: Store, ticksToLive: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(pos, room)
        self.body = body
        self.fatigue = fatigue
        self.hits = hits
        self.hitsMax = hitsMax
        self.id = _id
        self.memory = memory
        self.my = my
        self.name = name
        self.owner = owner
        self.saying = saying
        self.spawning = spawning
        self.store = store
        self.ticksToLive = ticksToLive

    def attack(self, target: Union[Structure, 'Creep']) -> int:
        pass

    def attackController(self, target: StructureController) -> int:
        pass

    def build(self, target: ConstructionSite) -> int:
        pass

    def cancelOrder(self, methodName: str) -> int:
        pass

    def claimController(self, target: StructureController) -> int:
        pass

    def dismantle(self, target: Structure) -> int:
        pass

    def drop(self, resourceType: str, amount: int = None) -> int:
        pass

    def generateSafeMode(self, target: StructureController) -> int:
        pass

    def getActiveBodyparts(self, _type: str) -> int:
        pass

    def harvest(self, target: Union[Source, Mineral]) -> int:
        pass

    def heal(self, target: 'Creep') -> int:
        pass

    def move(self, direction: int) -> int:
        pass

    def moveByPath(self, path: Union[list, str]) -> int:
        pass

    def moveTo(self, target: Union[RoomPosition, RoomObject], opts: Optional[Dict[str, Any]] = None) -> int:
        pass

    def notifyWhenAttacked(self, enabled: bool) -> int:
        pass

    def pickup(self, target: Resource) -> int:
        pass

    def rangedAttack(self, target: Union['Creep', Structure]) -> int:
        pass

    def rangedHeal(self, target: 'Creep') -> int:
        pass

    def rangedMassAttack(self) -> int:
        pass

    def repair(self, target: Structure) -> int:
        pass

    def reserveController(self, target: StructureController) -> int:
        pass

    def say(self, message: str, public: bool = False) -> int:
        pass

    def signController(self, target: StructureController, message: str) -> int:
        pass

    def suicide(self) -> int:
        pass

    def transfer(self, target: Union['Creep', Structure], resourceType: str, amount: int = None) -> int:
        pass

    def upgradeController(self, target: StructureController) -> int:
        pass

    def withdraw(self, target: Structure, resourceType: str, amount: int = None) -> int:
        pass
