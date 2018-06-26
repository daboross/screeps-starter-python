	__nest__ (
		__all__,
		'consts', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var TARGET_HARVESTERS = 0;
					var TARGET_UPGRADERS = 2;
					var TARGET_BUILDERS = 4;
					var TARGET_STATIC_HARVESTERS = 2;
					var TARGET_HAULERS = 4;
					var DEBUG_MESSAGES = false;
					__pragma__ ('<all>')
						__all__.DEBUG_MESSAGES = DEBUG_MESSAGES;
						__all__.TARGET_BUILDERS = TARGET_BUILDERS;
						__all__.TARGET_HARVESTERS = TARGET_HARVESTERS;
						__all__.TARGET_HAULERS = TARGET_HAULERS;
						__all__.TARGET_STATIC_HARVESTERS = TARGET_STATIC_HARVESTERS;
						__all__.TARGET_UPGRADERS = TARGET_UPGRADERS;
					__pragma__ ('</all>')
				}
			}
		}
	);
