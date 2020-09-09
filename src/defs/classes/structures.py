from typing import Any, Dict, List, Optional, Union
import warnings

from .creep import Creep
# noinspection PyProtectedMember
from .memory import _Memory
from .misc_obj import RoomObject, Store, _Effect
# noinspection PyProtectedMember
from .room import Room, RoomPosition, _Owner


# noinspection PyPep8Naming
class Structure(RoomObject):
    """

    :type id: str
    :type structureType: str
    :type hits: int
    :type hitsMax: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room, structureType: str, _id: str,
                 hits: int, hitsMax: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room)
        self.structureType = structureType
        self.id = _id
        self.hits = hits
        self.hitsMax = hitsMax

    def destroy(self) -> int:
        pass

    def isActive(self) -> bool:
        pass

    def notifyWhenAttacked(self, enabled: bool) -> int:
        pass


# noinspection PyPep8Naming
class OwnedStructure(Structure):
    """
    :type my: bool
    :type owner: _Owner
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room, structureType: str, _id: str,
                 hits: int, hitsMax: int, my: bool, owner: _Owner) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax)
        self.my = my
        self.owner = owner


# noinspection PyPep8Naming
class ConstructionSite(RoomObject):
    """
    :type effects: _Effect
    :type id: str
    :type my: bool
    :type owner: _Owner
    :type progress: int
    :type progressTotal: int
    :type structureType: str
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room, _id: str, my: bool,
                 owner: _Owner, progress: int, progressTotal: int, structureType: str) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room)
        self.id = _id
        self.my = my
        self.owner = owner
        self.progress = progress
        self.progressTotal = progressTotal
        self.structureType = structureType

    def remove(self) -> int:
        pass


# noinspection PyPep8Naming
class StructureContainer(Structure):
    """
    :type effects: _Effect
    :type store: Store
    :type ticksToDecay: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room, structureType: str,
                 _id: str, hits: int, hitsMax: int, store: Store, ticksToDecay: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax)
        self.store = store
        self.ticksToDecay = ticksToDecay


# noinspection PyPep8Naming
class _RoomReservation:
    """
    :type username: str
    :type ticksToEnd: int
    """

    def __init__(self, username: str, ticksToEnd: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        self.username = username
        self.ticksToEnd = ticksToEnd


class _ControllerSign:
    """
    :type username: str
    :type text: str
    :type time: int
    :type datetime: Any
    """

    def __init__(self, username: str, text: str, time: int, datetime: Any) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        self.time = time
        self.text = text
        self.username = username
        self.datetime = datetime


# noinspection PyPep8Naming
class StructureController(OwnedStructure):
    """
    :type effects: _Effect
    :type level: int
    :type progress: int
    :type progressTotal: int
    :type reservation: _RoomReservation | None
    :type safeMode: int
    :type safeModeAvailable: int
    :type safeModeCooldown: int
    :type sign: _ControllerSign | None
    :type ticksToDowngrade: int
    :type upgradeBlocked: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room, structureType: str,
                 _id: str, hits: int, hitsMax: int, my: bool, owner: _Owner, isPowerEnabled: bool,
                 level: int, progress: int, progressTotal: int, reservation: Optional[_RoomReservation],
                 safeMode: int, safeModeAvailable: int, safeModeCooldown: int, sign: Optional[_ControllerSign],
                 ticksToDowngrade: int, upgradeBlocked: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.isPowerEnabled = isPowerEnabled
        self.level = level
        self.progress = progress
        self.progressTotal = progressTotal
        self.reservation = reservation
        self.safeMode = safeMode
        self.safeModeAvailable = safeModeAvailable
        self.safeModeCooldown = safeModeCooldown
        self.sign = sign
        self.ticksToDowngrade = ticksToDowngrade
        self.upgradeBlocked = upgradeBlocked

    def activateSafeMode(self) -> int:
        pass

    def unclaim(self) -> int:
        pass


# noinspection PyPep8Naming
class StructureExtension(OwnedStructure):
    """
    :type effects: _Effect
    :type store: Store()
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room, structureType: str,
                 _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.store = store


# noinspection PyPep8Naming
class StructureExtractor(OwnedStructure):
    """
    :type effects: _Effect
    :type cooldown: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, cooldown: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.cooldown = cooldown


# noinspection PyPep8Naming
class StructureFactory(OwnedStructure):
    """
    :type effects: _Effect
    :type cooldown: int
    :type level: int
    :type store: Store
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, level: int, cooldown: int,
                 store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.cooldown = cooldown
        self.level = level
        self.store = store

        def produce(self, resourceType: str) -> int:
            pass


# noinspection PyPep8Naming
class StructureInvaderCore(OwnedStructure):
    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, level: int, ticksToDeploy: int) -> None:
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.level = level
        self.ticksToDeploy = ticksToDeploy

    """
    :type effects: _Effects
    :type level: int
    :type ticksToDeploy: int
    """


# noinspection PyPep8Naming
class StructureKeeperLair(OwnedStructure):
    """
    :type effects: _Effect
    :type ticksToSpawn: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, ticksToSpawn: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.ticksToSpawn = ticksToSpawn


# noinspection PyPep8Naming
class StructureLab(OwnedStructure):
    """
    :type effects: _Effect
    :type cooldown: int
    :type mineralType: Optional[str]
    :type store: Store
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, cooldown: int,
                 mineralType: Optional[str], store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.cooldown = cooldown
        self.mineralType = mineralType
        self.store = store

    def boostCreep(self, creep: Creep, bodyPartsCount: Optional[int] = None) -> int:
        pass

    def reverseReaction(self, lab1: 'StructureLab', lab2: 'StructureLab') -> int:
        pass

    def runReaction(self, lab1: 'StructureLab', lab2: 'StructureLab') -> int:
        pass

    def unboostCreep(self, creep: Creep) -> int:
        pass


# noinspection PyPep8Naming
class StructureLink(OwnedStructure):
    """
    :type effects: _Effect
    :type cooldown: int
    :type store: Store
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, cooldown: int, store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.cooldown = cooldown
        self.store = store

    def transferEnergy(self, target: 'StructureLink', amount: int = 0) -> int:
        pass


# noinspection PyPep8Naming
class StructureNuker(OwnedStructure):
    """
    :type effects: _Effect
    :type store: Store
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, energy: int, cooldown: int, store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.energy = energy
        self.cooldown = cooldown
        self.store = store

    def launchNuke(self, pos: RoomPosition) -> int:
        pass


# noinspection PyPep8Naming
class StructureObserver(OwnedStructure):
    """
    :type effects: _Effect
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner) -> None:
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)

    def observeRoom(self, roomName: str) -> int:
        pass


# noinspection PyPep8Naming
class StructurePowerBank(Structure):
    """
    :type effects: _Effect
    :type power: int
    :type ticksToDecay: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 power: int, ticksToDecay: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax)
        self.power = power
        self.ticksToDecay = ticksToDecay


# noinspection PyPep8Naming
class StructurePowerSpawn(OwnedStructure):
    """
    :type effects: _Effect
    :type energy: int
    :type energyCapacity: int
    :type power: int
    :type powerCapacity: int
    :type cooldown: int
    :type store: Store
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.store = store

    # erased from docs?
    # def createPowerCreep(self, name: str) -> int:
    #     pass

    def processPower(self) -> int:
        pass


class _ShardPortalDestination:
    """
    :type shard: str
    :type room: str
    """

    def __init__(self, shard: str, room: str) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        self.shard = shard
        self.room = room


# noinspection PyPep8Naming
class StructurePortal(Structure):
    """
    :type effects: _Effect
    :type destination: Union[RoomPosition, _ShardPortalDestination]
    :type ticksToDecay: Optional[int]
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 destination: Union[RoomPosition, _ShardPortalDestination], ticksToDecay: Optional[int]) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax)

        self.destination = destination
        self.ticksToDecay = ticksToDecay


# noinspection PyPep8Naming
class StructureRampart(OwnedStructure):
    """
    :type effects: _Effect
    :type isPublic: bool
    :type ticksToDecay: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, isPublic: bool, ticksToDecay: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.isPublic = isPublic
        self.ticksToDecay = ticksToDecay

    def setPublic(self, isPublic: bool) -> int:
        pass


# noinspection PyPep8Naming
class StructureRoad(Structure):
    """
    :type effects: _Effect
    :type ticksToDecay: int
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 ticksToDecay: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax)

        self.ticksToDecay = ticksToDecay


# noinspection PyPep8Naming
class _SpawnSpawningCreep:
    """
    :type directions: List[int]
    :type name: str
    :type needTime: int
    :type remainingTime: int
    :type spawn: StructureSpawn
    """

    def __init__(self, directions: List[int], name: str, needTime: int, remainingTime: int, spawn: str):
        self.directions = directions
        self.name = name
        self.needTime = needTime
        self.remainingTime = remainingTime
        self.spawn = spawn

    def cancel(self) -> int:
        pass

    def setDirections(self, directions: List[int]) -> int:
        pass


# noinspection PyPep8Naming
class StructureSpawn(OwnedStructure):
    """
    :type effects: _Effect
    :type memory: _Memory
    :type name: str
    :type spawning: Optional[_SpawnSpawningCreep]
    :type store: Store
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner,  # energy: int, energyCapacity: int,
                 memory: _Memory, name: str,
                 spawning: Optional[_SpawnSpawningCreep],
                 store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.memory = memory
        self.name = name
        self.spawning = spawning
        self.store = store

    @warnings.warn('This method is deprecated and will be removed soon.'
                   ' Please use StructureSpawn.spawnCreep with dryRun flag instead.', DeprecationWarning)
    def canCreateCreep(self, body: List[str], name: Optional[str] = None) -> int:
        pass

    @warnings.warn('This method is deprecated and will be removed soon.'
                   ' Please use StructureSpawn.spawnCreep instead.', DeprecationWarning)
    def createCreep(self, body: List[str], name: Optional[str] = None, memory: Optional[Dict[str, Any]] = None) \
            -> Union[int, str]:
        pass

    def spawnCreep(self, body: List[str], name: str, opts: Optional[Dict[str, Any]] = None) -> int:
        pass

    def recycleCreep(self, target: Creep) -> int:
        pass

    def renewCreep(self, target: Creep) -> int:
        pass


# noinspection PyPep8Naming
class StructureStorage(OwnedStructure):
    """
    :type effects: _Effect
    :type store: Store
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.store = store


# noinspection PyPep8Naming
class StructureTerminal(OwnedStructure):
    """
    :type effects: _Effect
    :type cooldown: int
    :type store: dict[str, int]
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, cooldown: int, store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.cooldown = cooldown
        self.store = store

    def send(self, resourceType: str, amount: Union[int, float], destination: str, description: str = None) -> int:
        pass


# noinspection PyPep8Naming
class StructureTower(OwnedStructure):
    """
    :type effects: _Effect
    :type store: Store
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int,
                 my: bool, owner: _Owner, store: Store) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax, my, owner)
        self.store = store

    def attack(self, target: Creep) -> int:
        pass

    def heal(self, target: Creep) -> int:
        pass

    def repair(self, target: Structure) -> int:
        pass


# noinspection PyPep8Naming
class StructureWall(Structure):
    """
    :type effects: _Effect
    """

    def __init__(self, effects: _Effect, pos: RoomPosition, room: Room,
                 structureType: str, _id: str, hits: int, hitsMax: int) -> None:
        """
        WARNING: This constructor is purely for type completion, and does not exist in the game.
        """
        super().__init__(effects, pos, room, structureType, _id, hits, hitsMax)
