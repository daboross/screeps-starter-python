	__nest__ (
		__all__,
		'towerControl', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var dm = __init__ (__world__.shared_methods).dm;
					var getAvgWallStrength = __init__ (__world__.shared_methods).getAvgWallStrength;
					var getStoredEnergy = __init__ (__world__.shared_methods).getStoredEnergy;
					var getSpawnEnergyCapacity = __init__ (__world__.shared_methods).getSpawnEnergyCapacity;
					var run = function (me) {
						dm (me.id + ' RUN');
						var task = decideTask (me);
						if (task == 'attack') {
							attack (me);
						}
						else if (task == 'build') {
							build (me);
						}
						else if (task == 'repair') {
							repair (me);
						}
						else {
							print ('UNRECOGNISED TASK FOR TOWER');
						}
						dm (me.id + ' END');
					};
					var decideTask = function (me) {
						if (me.pos.findClosestByRange (FIND_HOSTILE_CREEPS) != null || me.pos.findClosestByRange (FIND_HOSTILE_STRUCTURES) != null || me.pos.findClosestByRange (FIND_HOSTILE_CONSTRUCTION_SITES) != null) {
							return 'attack';
						}
						else {
							return 'repair';
						}
					};
					var attack = function (me) {
						var target = me.pos.findClosestByRange (FIND_HOSTILE_CREEPS);
						if (target != null) {
							me.attack (target);
						}
					};
					var repair = function (me) {
						var target = me.pos.findClosestByRange (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.hits < s.hitsMax && s.structureType != STRUCTURE_WALL;
						})});
						if (target == null && getStoredEnergy (me) > getSpawnEnergyCapacity (me)) {
							var target = me.pos.findClosestByRange (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
								return s.hits < s.hitsMax && s.hits < getAvgWallStrength (me);
							})});
						}
						if (target != null) {
							me.repair (target);
						}
					};
					__pragma__ ('<use>' +
						'defs' +
						'shared_methods' +
					'</use>')
					__pragma__ ('<all>')
						__all__.attack = attack;
						__all__.decideTask = decideTask;
						__all__.dm = dm;
						__all__.getAvgWallStrength = getAvgWallStrength;
						__all__.getSpawnEnergyCapacity = getSpawnEnergyCapacity;
						__all__.getStoredEnergy = getStoredEnergy;
						__all__.repair = repair;
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
