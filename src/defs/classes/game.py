from typing import Any, Callable, Dict, List, Optional, Union

from .creep import Creep
from .misc_obj import Flag, RoomObject
from .room import Room, RoomPosition, _Owner
from .structures import ConstructionSite, Structure, StructureSpawn


# noinspection PyPep8Naming
class _GameCpu:
    """
    :type limit: int
    :type tickLimit: int
    :type bucket: int
    """

    def __init__(self, limit: int, tickLimit: int, bucket: int) -> None:
        self.limit = limit
        self.tickLimit = tickLimit
        self.bucket = bucket

    def getUsed(self) -> float:
        pass


# noinspection PyPep8Naming
class _GameGcl:
    """
    :type level: int
    :type progress: int
    :type progressTotal: int
    """

    def __init__(self, level: int, progress: int, progressTotal: int) -> None:
        self.level = level
        self.progress = progress
        self.progressTotal = progressTotal


# noinspection PyPep8Naming
class _GameMap:
    def describeExits(self, roomName: str) -> Dict[str, str]:
        pass

    def findExit(self, fromRoom: str, toRoom: str, opts: Dict[str, Any]) -> int:
        pass

    def findRoute(self, fromRoom: str, toRoom: str, opts: Dict[str, Any]) -> List[Dict[str, Union[int, str]]]:
        pass

    def getRoomLinearDistance(self, roomName1: str, roomName2: str, terminalDistance: bool = False) -> int:
        pass

    def getTerrainAt(self, x: Union[int, RoomPosition], y: int = None, roomName: str = None) -> str:
        pass

    def isRoomAvailable(self, roomName: str) -> bool:
        pass


class _MarketTransactionOrder:
    """
    :type id: str
    :type type: str
    :type price: float
    """

    def __init__(self, _id: str, _type: str, price: int) -> None:
        self.id = _id
        self.type = _type
        self.price = price


# noinspection PyPep8Naming
class _MarketTransaction:
    """
    :type transactionId: str
    :type time: int
    :type sender: _Owner
    :type recipient: _Owner
    :type resourceType: str
    :type amount: int
    :type js_from: str
    :type to: str
    :type description: str
    :type order: _MarketTransactionOrder | None
    """

    def __init__(self, transactionId: str, time: int, sender: _Owner, recipient: _Owner, resourceType: str,
                 amount: int, js_from: str, to: str, description: str, order: Optional[_MarketTransactionOrder]) \
            -> None:
        self.transactionId = transactionId
        self.time = time
        self.sender = sender
        self.recipient = recipient
        self.resourceType = resourceType
        self.amount = amount
        self.js_from = js_from
        self.to = to
        self.description = description
        self.order = order


# noinspection PyPep8Naming
class _MarketOrder:
    """
    :type id: str
    :type created: int
    :type type: str
    :type resourceType: str
    :type roomName: str
    :type amount: int
    :type remainingAmount: int
    :type price: float
    """

    def __init__(self, _id: str, created: int, _type: str, resourceType: str, roomName: str, amount: int,
                 remainingAmount: int, price: float) -> None:
        self.id = _id
        self.created = created
        self.type = _type
        self.resourceType = resourceType
        self.roomName = roomName
        self.amount = amount
        self.remainingAmount = remainingAmount
        self.price = price


# noinspection PyPep8Naming
class _OwnedMarketOrder(_MarketOrder):
    """
    :type active: bool
    :type totalAmount: int
    """

    def __init__(self, _id: str, created: int, _type: str, resourceType: str, roomName: str, amount: int,
                 remainingAmount: int, price: float, active: bool, totalAmount: int) -> None:
        super().__init__(_id, created, _type, resourceType, roomName, amount, remainingAmount, price)
        self.active = active
        self.totalAmount = totalAmount


# noinspection PyPep8Naming
class _GameMarket:
    """
    :type credits: int
    :type incomingTransactions: list[_MarketTransaction]
    :type outgoingTransactions: list[_MarketTransaction]
    :type orders: dict[str, _OwnedMarketOrder]
    """

    def __init__(self, _credits: int, incomingTransactions: List[_MarketTransaction],
                 outgoingTransactions: List[_MarketTransaction], orders: Dict[str, _OwnedMarketOrder]) -> None:
        self.credits = _credits
        self.incomingTransactions = incomingTransactions
        self.outgoingTransactions = outgoingTransactions
        self.orders = orders

    def calcTransactionCost(self, amount: Union[int, float], roomName1: str, roomName2: str) -> int:
        pass

    def cancelOrder(self, orderId: str) -> int:
        pass

    def changeOrderPrice(self, orderId: str, newPrice: int) -> int:
        pass

    def createOrder(self, _type: str, resourceType: str, price: float, totalAmount: int, roomName: str = None) \
            -> int:
        pass

    def deal(self, orderId: str, amount: Union[int, float], yourRoomName: str = None) -> int:
        pass

    def extendOrder(self, orderId: str, addAmount: int) -> int:
        pass

    def getAllOrders(self, _filter: Union[Dict[str, Union[int, str]], Callable[[_MarketOrder], bool]]) \
            -> List[_MarketOrder]:
        pass

    def getOrderById(self, _id: str) -> _MarketOrder:
        pass


# noinspection PyPep8Naming
class Game:
    """
    :type constructionSites: dict[str, ConstructionSite]
    :type cpu: _GameCpu
    :type creeps: dict[str, Creep]
    :type flags: dict[str, Flag]
    :type gcl: _GameGcl
    :type map: _GameMap
    :type market: _GameMarket
    :type resources: dict[str, int]
    :type rooms: dict[str, Room]
    :type spawns: dict[str, StructureSpawn]
    :type structures: dict[str, Structure]
    :type time: int
    """
    constructionSites = {}  # type: Dict[str, ConstructionSite]
    cpu = None  # type: _GameCpu
    creeps = {}  # type: Dict[str, Creep]
    flags = {}  # type: Dict[str, Flag]
    gcl = None  # type: _GameGcl
    map = None  # type: _GameMap
    market = None  # type: _GameMarket
    resources = {}  # type: Dict[str, int]
    rooms = {}  # type: Dict[str, Room]
    spawns = {}  # type: Dict[str, StructureSpawn]
    structures = {}  # type: Dict[str, Structure]
    time = 0  # type: int

    @classmethod
    def getObjectById(cls, _id: str) -> RoomObject:
        pass

    @classmethod
    def notify(cls, message: str, groupInterval: int = 0):
        pass


class _PathFinderResult:
    """
    :type path: List[RoomPosition]
    :type ops: int
    :type cost: int
    :type incomplete: bool
    """

    def __init__(self, path: List[RoomPosition], ops: int, cost: int, incomplete: bool):
        self.path = path
        self.ops = ops
        self.cost = cost
        self.incomplete = incomplete


class PathFinder:
    @staticmethod
    def search(origin: RoomPosition, goal: Union[Dict[str, Any], List[Dict[str, Any]]],
               opts: Optional[Dict[str, Any]] = None) -> _PathFinderResult:
        pass
