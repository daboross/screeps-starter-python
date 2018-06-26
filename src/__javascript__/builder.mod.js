	__nest__ (
		__all__,
		'builder', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var refill = __init__ (__world__.shared_methods).refill;
					var dm = __init__ (__world__.shared_methods).dm;
					var getStoredEnergy = __init__ (__world__.shared_methods).getStoredEnergy;
					var getSpawnEnergyCapacity = __init__ (__world__.shared_methods).getSpawnEnergyCapacity;
					var getAvgWallStrength = __init__ (__world__.shared_methods).getAvgWallStrength;
					var constructionSitesExist = __init__ (__world__.shared_methods).constructionSitesExist;
					var BODY_0 = [MOVE, WORK, CARRY];
					var BODY_1 = [MOVE, MOVE, MOVE, WORK, WORK, CARRY, CARRY, CARRY, CARRY];
					var BODY_2 = [MOVE, MOVE, MOVE, MOVE, WORK, WORK, WORK, WORK, CARRY, CARRY, CARRY, CARRY];
					var run = function (me) {
						dm (me.name + ' RUN', 0);
						decideTask (me);
						if (me.memory.task == 'build') {
							build (me);
						}
						else if (me.memory.task == 'repair') {
							repair (me);
						}
						else if (me.memory.task == 'refill') {
							refill (me);
						}
						else {
							me.say ('ERROR', me.memory.task);
						}
						dm (me.name + ' END', 0);
					};
					var decideTask = function (me) {
						if (me.carry.energy == 0) {
							if (me.memory.task == 'build') {
								me.say ('Refilling');
							}
							me.memory.task = 'refill';
						}
						else if (constructionSitesExist (me)) {
							if (me.memory.task != 'build') {
								me.say ('Building');
							}
							me.memory.task = 'build';
						}
						else {
							if (me.memory.task != 'repair') {
								me.say ('Repairing');
							}
							me.memory.task = 'repair';
						}
					};
					var build = function (me) {
						var target = me.pos.findClosestByRange (FIND_CONSTRUCTION_SITES);
						if (target != null) {
							if (me.build (target) == ERR_NOT_IN_RANGE) {
								me.moveTo (target);
							}
						}
					};
					var repair = function (me) {
						var target = me.pos.findClosestByRange (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.hits < s.hitsMax && s.structureType == STRUCTURE_WALL && s.hits < getAvgWallStrength (me) + 50;
						})});
						if (target == null) {
							var target = me.pos.findClosestByRange (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
								return s.hits < s.hitsMax;
							})});
						}
						if (target != null) {
							if (me.repair (target) == ERR_NOT_IN_RANGE) {
								me.moveTo (target);
							}
						}
					};
					__pragma__ ('<use>' +
						'defs' +
						'shared_methods' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BODY_0 = BODY_0;
						__all__.BODY_1 = BODY_1;
						__all__.BODY_2 = BODY_2;
						__all__.build = build;
						__all__.constructionSitesExist = constructionSitesExist;
						__all__.decideTask = decideTask;
						__all__.dm = dm;
						__all__.getAvgWallStrength = getAvgWallStrength;
						__all__.getSpawnEnergyCapacity = getSpawnEnergyCapacity;
						__all__.getStoredEnergy = getStoredEnergy;
						__all__.refill = refill;
						__all__.repair = repair;
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
