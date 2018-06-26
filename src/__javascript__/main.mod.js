	(function () {
		var dm = __init__ (__world__.shared_methods).dm;
		var consts = __init__ (__world__.consts);
		var towerControl = __init__ (__world__.towerControl);
		var harvester = __init__ (__world__.harvester);
		var static_harvester = __init__ (__world__.static_harvester);
		var hauler = __init__ (__world__.hauler);
		var upgrader = __init__ (__world__.upgrader);
		var builder = __init__ (__world__.builder);
		var manual1 = __init__ (__world__.manual1);
		var manual2 = __init__ (__world__.manual2);
		var manual3 = __init__ (__world__.manual3);
		var main = function () {
			var harvesters = 0;
			var static_harvesters = 0;
			var haulers = 0;
			var upgraders = 0;
			var builders = 0;
			var __iterable0__ = _.pairs (Memory.creeps);
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var name = __left0__ [0];
				var creep = __left0__ [1];
				if (!((name in Game.creeps))) {
					delete Memory.creeps [name];
				}
			}
			var __iterable0__ = Object.keys (Game.creeps);
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var creepName = __iterable0__ [__index0__];
				var creep = Game.creeps [creepName];
				if (creep.memory.role == 'harvester') {
					harvester.run (creep);
					harvesters++;
				}
				if (creep.memory.role == 'static_harvester') {
					static_harvester.run (creep);
					static_harvesters++;
				}
				if (creep.memory.role == 'hauler') {
					hauler.run (creep);
					haulers++;
				}
				if (creep.memory.role == 'upgrader') {
					upgrader.run (creep);
					upgraders++;
				}
				if (creep.memory.role == 'builder') {
					builder.run (creep);
					builders++;
				}
				if (creep.memory.role == 'manual') {
					manual1.run (creep);
				}
			}
			var __iterable0__ = _.pairs (Game.rooms);
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var key = __left0__ [0];
				var room = __left0__ [1];
				var __iterable1__ = _.pairs (room.find (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
					return s.structureType == STRUCTURE_TOWER;
				})}));
				for (var __index1__ = 0; __index1__ < __iterable1__.length; __index1__++) {
					var __left0__ = __iterable1__ [__index1__];
					var key2 = __left0__ [0];
					var tower = __left0__ [1];
					towerControl.run (tower);
				}
			}
			var __iterable0__ = Object.keys (Game.spawns);
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var spawnName = __iterable0__ [__index0__];
				var spawn = Game.spawns [spawnName];
				if (spawn.spawning != null) {
					continue;
				}
				if (harvesters < consts.TARGET_HARVESTERS) {
					spawn.spawnCreep (harvester.BODY_1, nameCreep ('harvester'), {'memory': {'role': 'harvester'}});
				}
				else if (static_harvesters < consts.TARGET_STATIC_HARVESTERS) {
					spawn.spawnCreep (static_harvester.BODY_0, nameCreep ('static_harvester'), {'memory': {'role': 'static_harvester'}});
				}
				else if (haulers < consts.TARGET_HAULERS) {
					spawn.spawnCreep (hauler.BODY_2, nameCreep ('hauler'), {'memory': {'role': 'hauler'}});
				}
				else if (upgraders < consts.TARGET_UPGRADERS) {
					spawn.spawnCreep (upgrader.BODY_2, nameCreep ('upgrader'), {'memory': {'role': 'upgrader'}});
				}
				else if (builders < consts.TARGET_BUILDERS) {
					spawn.spawnCreep (builder.BODY_2, nameCreep ('builder'), {'memory': {'role': 'builder'}});
				}
			}
			dm (' ', 0);
		};
		var nameCreep = function (role) {
			if (role == 'harvester') {
				var target = consts.TARGET_HARVESTERS;
			}
			else if (role == 'static_harvester') {
				var target = consts.TARGET_STATIC_HARVESTERS;
			}
			else if (role == 'hauler') {
				var target = consts.TARGET_HAULERS;
			}
			else if (role == 'upgrader') {
				var target = consts.TARGET_UPGRADERS;
			}
			else if (role == 'builder') {
				var target = consts.TARGET_BUILDERS;
			}
			var pre = (role [0].upper () + role.__getslice__ (1, null, 1)) + ' ';
			var i = 0;
			while (true) {
				i++;
				var name = str (pre + str (i));
				if ((name in Game.creeps)) {
					continue;
				}
				else {
					return name;
				}
			}
		};
		module.exports.loop = main;
		__pragma__ ('<use>' +
			'builder' +
			'consts' +
			'defs' +
			'harvester' +
			'hauler' +
			'manual1' +
			'manual2' +
			'manual3' +
			'shared_methods' +
			'static_harvester' +
			'towerControl' +
			'upgrader' +
		'</use>')
		__pragma__ ('<all>')
			__all__.dm = dm;
			__all__.main = main;
			__all__.nameCreep = nameCreep;
		__pragma__ ('</all>')
	}) ();
