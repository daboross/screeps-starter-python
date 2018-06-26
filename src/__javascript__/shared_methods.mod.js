	__nest__ (
		__all__,
		'shared_methods', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var consts = __init__ (__world__.consts);
					var refill = function (me) {
						var target = me.pos.findClosestByPath (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_CONTAINER && s.store.energy >= me.carryCapacity;
						})});
						if (target != null) {
							var code = me.withdraw (target, 'energy');
							if (code == 0) {
								// pass;
							}
							else if (code == ERR_NOT_IN_RANGE) {
								me.moveTo (target);
							}
							else {
								me.say ('ERROR:', code);
							}
							return true;
						}
						var target = me.pos.findClosestByPath (FIND_DROPPED_RESOURCES, {'filter': (function __lambda__ (r) {
							return r.resourceType == RESOURCE_ENERGY && r.amount >= me.carryCapacity;
						})});
						if (target != null) {
							var code = me.pickup (target);
							if (code == OK) {
								// pass;
							}
							else if (code == ERR_NOT_IN_RANGE) {
								me.moveTo (target);
							}
							return true;
						}
					};
					var containerIsMineDrop = function (container) {
						var mineDrop = false;
						var __iterable0__ = _.pairs (container.room.find (FIND_SOURCES));
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var key = __left0__ [0];
							var source = __left0__ [1];
							if (container.pos.isNearTo (source)) {
								var mineDrop = true;
							}
						}
						return mineDrop;
					};
					var dm = function (message, indentLevel) {
						if (consts.DEBUG_MESSAGES) {
							for (var i = 0; i < indentLevel; i++) {
								var message = '   ' + message;
							}
							print (message);
						}
					};
					var getSpawnEnergy = function (me) {
						var total = 0;
						var __iterable0__ = _.pairs (me.room.find (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_EXTENSION || s.structureType == STRUCTURE_SPAWN;
						})}));
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var key = __left0__ [0];
							var structure = __left0__ [1];
							total += structure.energy;
						}
						return total;
					};
					var getSpawnEnergyCapacity = function (me) {
						var total = 0;
						var __iterable0__ = _.pairs (me.room.find (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_EXTENSION || s.structureType == STRUCTURE_SPAWN;
						})}));
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var key = __left0__ [0];
							var structure = __left0__ [1];
							total += structure.energyCapacity;
						}
						return total;
					};
					var getStoredEnergy = function (me) {
						var total = 0;
						var __iterable0__ = _.pairs (me.room.find (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_CONTAINER;
						})}));
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var key = __left0__ [0];
							var container = __left0__ [1];
							total += container.store.energy;
						}
						var __iterable0__ = _.pairs (me.room.find (FIND_DROPPED_RESOURCES, {'filter': (function __lambda__ (r) {
							return r.resourceType == RESOURCE_ENERGY;
						})}));
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var key = __left0__ [0];
							var resource = __left0__ [1];
							total += resource.amount;
						}
						return total;
					};
					var getAvgWallStrength = function (me) {
						var wallHits = [];
						var __iterable0__ = _.pairs (me.room.find (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_WALL;
						})}));
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var key = __left0__ [0];
							var wall = __left0__ [1];
							wallHits.add (wall.hits);
						}
						return sum (wallHits) / len (wallHits);
					};
					var constructionSitesExist = function (me) {
						return !(me.pos.findClosestByRange (FIND_CONSTRUCTION_SITES) == null);
					};
					__pragma__ ('<use>' +
						'consts' +
						'defs' +
					'</use>')
					__pragma__ ('<all>')
						__all__.constructionSitesExist = constructionSitesExist;
						__all__.containerIsMineDrop = containerIsMineDrop;
						__all__.dm = dm;
						__all__.getAvgWallStrength = getAvgWallStrength;
						__all__.getSpawnEnergy = getSpawnEnergy;
						__all__.getSpawnEnergyCapacity = getSpawnEnergyCapacity;
						__all__.getStoredEnergy = getStoredEnergy;
						__all__.refill = refill;
					__pragma__ ('</all>')
				}
			}
		}
	);
