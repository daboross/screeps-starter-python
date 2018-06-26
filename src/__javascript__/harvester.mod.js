	__nest__ (
		__all__,
		'harvester', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var dm = __init__ (__world__.shared_methods).dm;
					var BODY_0 = [MOVE, WORK, CARRY];
					var BODY_1 = [MOVE, MOVE, MOVE, WORK, WORK, WORK, CARRY, CARRY];
					var BODY_2 = [MOVE, MOVE, MOVE, MOVE, WORK, WORK, WORK, WORK, CARRY, CARRY, CARRY, CARRY];
					var run = function (me) {
						dm (me.name + ' RUN', 0);
						if (me.carry.energy == 0) {
							if (me.memory.depositing) {
								me.say ('Mining');
							}
							me.memory.depositing = false;
						}
						else if (me.carry.energy == me.carryCapacity) {
							if (!(me.memory.depositing)) {
								me.say ('Dropping');
							}
							me.memory.depositing = true;
						}
						if (me.memory.depositing) {
							var target = getTarget (me);
							var code = me.transfer (target, RESOURCE_ENERGY);
							if (code == OK) {
								me.memory.target = false;
							}
							if (me.transfer (target, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE) {
								me.moveTo (target);
							}
						}
						else {
							var target = me.pos.findClosestByPath (FIND_SOURCES_ACTIVE);
							var code = me.harvest (target);
							if (code == OK) {
								// pass;
							}
							else if (code == ERR_NOT_IN_RANGE) {
								me.moveTo (target);
							}
						}
						dm (me.name + ' END', 0);
					};
					var getTarget = function (me) {
						var dropPoints = [];
						dropPoints.extend (me.room.find (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_EXTENSION;
						})}));
						var __iterable0__ = Object.keys (Game.structures);
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var pointName = __iterable0__ [__index0__];
							var point = Game.structures [pointName];
							var pointTargeted = false;
							if (point.structureType == STRUCTURE_EXTENSION && point.energy < point.energyCapacity) {
								var __iterable1__ = Object.keys (Game.creeps);
								for (var __index1__ = 0; __index1__ < __iterable1__.length; __index1__++) {
									var creepName = __iterable1__ [__index1__];
									var creep = Game.creeps [creepName];
									if (creep.memory.target == point) {
										var pointTargeted = true;
									}
								}
								if (pointTargeted == false) {
									me.memory.target = point;
									return point;
								}
							}
						}
						if (Game.spawns ['Spawn1'].energy < Game.spawns ['Spawn1'].energyCapacity) {
							me.memory.target = Game.spawns ['Spawn1'];
							return Game.spawns ['Spawn1'];
						}
						var __iterable0__ = Object.keys (Game.structures);
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var pointName = __iterable0__ [__index0__];
							var point = Game.structures [pointName];
							var pointTargeted = false;
							if (point.structureType == STRUCTURE_EXTENSION) {
								var __iterable1__ = Object.keys (Game.creeps);
								for (var __index1__ = 0; __index1__ < __iterable1__.length; __index1__++) {
									var creepName = __iterable1__ [__index1__];
									var creep = Game.creeps [creepName];
									if (creep.memory.target == point) {
										var pointTargeted = true;
									}
								}
								if (pointTargeted == false) {
									me.memory.target = point;
									return point;
								}
							}
						}
						me.memory.target = Game.spawns ['Spawn1'];
						return Game.spawns ['Spawn1'];
					};
					__pragma__ ('<use>' +
						'defs' +
						'shared_methods' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BODY_0 = BODY_0;
						__all__.BODY_1 = BODY_1;
						__all__.BODY_2 = BODY_2;
						__all__.dm = dm;
						__all__.getTarget = getTarget;
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
