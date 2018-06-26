	__nest__ (
		__all__,
		'manual2', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var run = function (me) {
						// pass;
					};
					__pragma__ ('<use>' +
						'defs' +
					'</use>')
					__pragma__ ('<all>')
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
