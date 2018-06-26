	__nest__ (
		__all__,
		'static_harvester', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var containerIsMineDrop = __init__ (__world__.shared_methods).containerIsMineDrop;
					var dm = __init__ (__world__.shared_methods).dm;
					var BODY_0 = [WORK, WORK, WORK, WORK, WORK, MOVE];
					var run = function (me) {
						dm (me.name + ' RUN');
						if (me.memory.target == null) {
							initialise (me);
						}
						if (me.pos.x != Game.getObjectById (me.memory.target).pos.x || me.pos.y != Game.getObjectById (me.memory.target).pos.y) {
							me.moveTo (Game.getObjectById (me.memory.target));
						}
						else {
							var target = me.pos.findClosestByPath (FIND_SOURCES);
							var code = me.harvest (target);
							if (code == OK || code == -(6)) {
								// pass;
							}
							else {
								me.say ('ERROR', code);
							}
						}
						dm (me.name + ' END');
					};
					var initialise = function (me) {
						dm ('Initialising', 1);
						var containers = me.room.find (FIND_STRUCTURES, {'filter': (function __lambda__ (s) {
							return s.structureType == STRUCTURE_CONTAINER;
						})});
						var __iterable0__ = _.pairs (containers);
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var key = __left0__ [0];
							var container = __left0__ [1];
							var targeted = false;
							dm ('Container found: ' + container.id, 2);
							dm ((container.id + ' is mine drop: ') + str (containerIsMineDrop (container)), 3);
							if (containerIsMineDrop (container)) {
								var __iterable1__ = _.pairs (Game.creeps);
								for (var __index1__ = 0; __index1__ < __iterable1__.length; __index1__++) {
									var __left0__ = __iterable1__ [__index1__];
									var key2 = __left0__ [0];
									var creep = __left0__ [1];
									if (creep.memory.role == 'static_harvester') {
										dm ('Static harvester found: ' + creep.name, 3);
										dm ((creep.name + ' target: ') + creep.memory.target, 4);
										dm ('Mine drop is creeps target: ' + str (creep.memory.target == container.id), 4);
										if (creep.memory.target == container.id) {
											var targeted = true;
											break;
										}
									}
								}
								dm ('Mine drop already targeted: ' + str (targeted), 3);
								if (targeted == false) {
									dm ('TARGET SET: ' + container.id, 3);
									me.memory.target = container.id;
								}
							}
						}
					};
					__pragma__ ('<use>' +
						'defs' +
						'shared_methods' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BODY_0 = BODY_0;
						__all__.containerIsMineDrop = containerIsMineDrop;
						__all__.dm = dm;
						__all__.initialise = initialise;
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
