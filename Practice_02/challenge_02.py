CALIBRATION_FACTOR = 1.5

def process_telemetry(*readings, **config):	
	print(list(map(lambda r: None if (r * CALIBRATION_FACTOR) > 100  and config.get('strict_mode',0) ==True else (r * CALIBRATION_FACTOR) , readings)))


process_telemetry(1,1.2,2.1,200.2,2,2.3,1,pol=True,strict_mode=True )
