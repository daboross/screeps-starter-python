	__nest__ (
		__all__,
		'upgrader', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var refill = __init__ (__world__.shared_methods).refill;
					var dm = __init__ (__world__.shared_methods).dm;
					var BODY_0 = [MOVE, WORK, CARRY];
					var BODY_1 = [MOVE, MOVE, MOVE, WORK, WORK, CARRY, CARRY, CARRY, CARRY];
					var BODY_2 = [MOVE, MOVE, MOVE, MOVE, MOVE, MOVE, WORK, WORK, CARRY, CARRY, CARRY, CARRY, CARRY, CARRY];
					var run = function (me) {
						dm (me.name + ' RUN', 0);
						decideTask (me);
						if (me.memory.upgrading) {
							upgrade (me);
						}
						else {
							refill (me);
						}
						dm (me.name + ' END', 0);
					};
					var decideTask = function (me) {
						if (me.carry.energy == 0) {
							if (me.memory.upgrading) {
								me.say ('Refilling');
							}
							me.memory.upgrading = false;
						}
						else if (me.carry.energy == me.carryCapacity) {
							if (!(me.memory.upgrading)) {
								me.say ('Upgrading');
							}
							me.memory.upgrading = true;
						}
					};
					var upgrade = function (me) {
						var target = me.room.controller;
						if (me.upgradeController (target, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE) {
							me.moveTo (target);
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
						__all__.decideTask = decideTask;
						__all__.dm = dm;
						__all__.refill = refill;
						__all__.run = run;
						__all__.upgrade = upgrade;
					__pragma__ ('</all>')
				}
			}
		}
	);
