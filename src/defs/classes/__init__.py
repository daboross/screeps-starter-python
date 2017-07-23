"""
This directory contains mock-up objects for many of Screep's JavaScript game objects.

There are not typings for everything, and some, such as those for `_` (lodash), exist but are incomplete.

I'll continue to add things to this, but if there's something in particular you need, it's very
easy to either add it yourself and submit a PR to this repository, or submit an issue asking
for the class.

A few notes:

- None of the constructors for game objects are accurate. It's not reliable to create these in game,
  but a 'fake' constructor with all attributes as arguments is created to give type checkers correct
  thoughts on what properties should exist.
- All methods and properties are typed with python-3.5+ annotations, and all properties are *also*
  typed with `:type x: y` style types, for editors such as PyCharm which do not fully use annotations
  for type hinting.
"""
from .creep import Creep
from .game import Game
from .lodash import _
from .memory import Memory, RawMemory
from .misc_obj import Flag, Mineral, Resource, RoomObject, Source
from .other_js import Infinity, JSON, Math, Object, RegExp, module, require, this, typeof, undefined
from .room import Room, RoomPosition
from .structures import ConstructionSite, OwnedStructure, Structure, StructureContainer, StructureController, \
    StructureExtension, StructureExtractor, StructureKeeperLair, StructureLab, StructureLink, StructureNuker, \
    StructureObserver, StructurePortal, StructurePowerBank, StructurePowerSpawn, StructureRampart, StructureRoad, \
    StructureSpawn, StructureStorage, StructureTerminal, StructureTower, StructureWall

__all__ = [
    'Creep', 'Game', '_', 'Memory', 'RawMemory', 'Flag', 'Mineral', 'Resource', 'RoomObject', 'Source',
    'Infinity', 'JSON', 'Math', 'Object', 'RegExp', 'module', 'require', 'this', 'typeof', 'undefined',
    'Room', 'RoomPosition',
    'ConstructionSite', 'OwnedStructure', 'Structure', 'StructureContainer', 'StructureController',
    'StructureExtension', 'StructureExtractor', 'StructureKeeperLair', 'StructureLab', 'StructureLink',
    'StructureNuker', 'StructureObserver', 'StructurePortal', 'StructurePowerBank', 'StructurePowerSpawn',
    'StructureRampart', 'StructureRoad', 'StructureSpawn', 'StructureStorage', 'StructureTerminal', 'StructureTower',
    'StructureWall'
]
