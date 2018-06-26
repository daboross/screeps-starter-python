	__nest__ (
		__all__,
		'hauler', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var containerIsMineDrop = __init__ (__world__.shared_methods).containerIsMineDrop;
					var dm = __init__ (__world__.shared_methods).dm;
					var getSpawnEnergy = __init__ (__world__.shared_methods).getSpawnEnergy;
					var getSpawnEnergyCapacity = __init__ (__world__.shared_methods).getSpawnEnergyCapacity;
					var getStoredEnergy = __init__ (__world__.shared_methods).getStoredEnergy;
					var BODY_0 = [MOVE, CARRY];
					var BODY_1 = [MOVE, MOVE, MOVE, MOVE, MOVE, CARRY, CARRY, CARRY, CARRY, CARRY];
					var BODY_2 = [MOVE, MOVE, MOVE, MOVE, MOVE, MOVE, MOVE, MOVE, CARRY, CARRY, CARRY, CARRY, CARRY, CARRY, CARRY, CARRY];
					var run = function (me) {
						dm (me.name + ' RUN', 0);
						decideTask (me);
						if (me.memory.depositing) {
							deposit (me);
						}
						else {
							refill (me);
						}
						dm (me.name + ' END', 0);
					};
					var decideTask = function (me) {
						if (me.carry.energy == 0) {
							if (me.memory.depositing) {
								me.say ('Refilling');
							}
							me.memory.depositing = false;
						}
						else if (me.carry.energy == me.carryCapacity) {
							if (!(me.memory.depositing)) {
								me.say ('Dropping');
							}
							me.memory.depositing = true;
						}
					};
					var deposit = function (me) {
						var target = getDropTarget (me);
						if (target == false) {
							queueByExtension (me);
						}
						else {
							var code = me.transfer (target, RESOURCE_ENERGY);
							if (code == OK) {
								me.memory.target = false;
							}
							else if (code == ERR_NOT_IN_RANGE) {
								me.moveTo (target);
							}
							else {
								me.say ('ERR', code);
							}
						}
					};
					var refill = function (me) {
						var out = getCollectTarget (me);
						if (out == null) {
							me.say ('NO TARGET. CHECK THIS IS RIGHT');
							return ;
						}
						var target = out [0];
						var targetType = out [1];
						if (targetType == 'floor') {
							var code = me.pickup (target);
						}
						else if (targetType == 'container') {
							var code = me.withdraw (target, 'energy');
						}
						else {
							me.say ('ERROR - BAD TARGET');
						}
						if (code == 0) {
							// pass;
						}
						else if (code == ERR_NOT_IN_RANGE) {
							me.moveTo (target);
						}
						else {
							me.say (code);
						}
						return true;
					};
					var getDropTarget = function (me) {
						if (Game.spawns ['Spawn1'].energy < Game.spawns ['Spawn1'].energyCapacity) {
							return Game.spawns ['Spawn1'];
						}
						var target = me.pos.findClosestByPath (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_EXTENSION && s.energy < s.energyCapacity;
						})});
						if (target != null) {
							return target;
						}
						var target = me.pos.findClosestByPath (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_TOWER && s.energyCapacity - s.energy > 200;
						})});
						if (target != null) {
							return target;
						}
						var target = me.pos.findClosestByPath (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_CONTAINER && s.store.energy < s.storeCapacity && containerIsMineDrop (s) == false;
						})});
						if (target != null) {
							return target;
						}
						return false;
					};
					var getCollectTarget = function (me, fillCarry) {
						if (typeof fillCarry == 'undefined' || (fillCarry != null && fillCarry .hasOwnProperty ("__kwargtrans__"))) {;
							var fillCarry = true;
						};
						dm ('Getting collection target', 1);
						var takeFromStorage = false;
						if (getSpawnEnergy (me) < getSpawnEnergyCapacity (me)) {
							var takeFromStorage = true;
						}
						else if (len (me.room.find (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_TOWER && s.energyCapacity - s.energy > me.carryCapacity;
						})})) > 0) {
							var takeFromStorage = true;
						}
						if (takeFromStorage) {
							var target = me.pos.findClosestByPath (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
								return s.structureType == STRUCTURE_CONTAINER && s.store.energy >= me.carryCapacity;
							})});
						}
						if (target != null) {
							return [target, 'container'];
						}
						if (fillCarry) {
							var target = me.pos.findClosestByPath (FIND_DROPPED_RESOURCES, {'filter': (function __lambda__ (r) {
								return r.resourceType == RESOURCE_ENERGY && r.amount >= me.carryCapacity;
							})});
						}
						else {
							var target = me.pos.findClosestByPath (FIND_DROPPED_RESOURCES, {'filter': (function __lambda__ (r) {
								return r.resourceType == RESOURCE_ENERGY;
							})});
						}
						if (target != null) {
							return [target, 'floor'];
						}
						if (fillCarry) {
							var target = me.pos.findClosestByPath (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
								return s.structureType == STRUCTURE_CONTAINER && containerIsMineDrop (s) && s.store.energy >= me.carryCapacity;
							})});
						}
						else {
							var target = me.pos.findClosestByPath (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
								return s.structureType == STRUCTURE_CONTAINER && containerIsMineDrop (s) && s.store.energy > 0;
							})});
						}
						if (target != null) {
							return [target, 'container'];
						}
						if (fillCarry) {
							return getCollectTarget (me, false);
						}
						else {
							return false;
						}
					};
					var queueByExtension = function (me) {
						var __iterable0__ = _.pairs (Game.structures);
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var key = __left0__ [0];
							var point = __left0__ [1];
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
						__all__.containerIsMineDrop = containerIsMineDrop;
						__all__.decideTask = decideTask;
						__all__.deposit = deposit;
						__all__.dm = dm;
						__all__.getCollectTarget = getCollectTarget;
						__all__.getDropTarget = getDropTarget;
						__all__.getSpawnEnergy = getSpawnEnergy;
						__all__.getSpawnEnergyCapacity = getSpawnEnergyCapacity;
						__all__.getStoredEnergy = getStoredEnergy;
						__all__.queueByExtension = queueByExtension;
						__all__.refill = refill;
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
