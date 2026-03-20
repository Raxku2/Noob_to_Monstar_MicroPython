# try:
#     # ⚠️ DANGEROUS CODE: The sensor wire might be unplugged!
#     temperature = dht_sensor.read()
#     print(f"Temp is {temperature}")
# 
# except Exception as e:
#     # 🛡️ THE FALLBACK: This only runs if the 'try' block fails
#     print(f"SENSOR OFFLINE! Error details: {e}")
#     temperature = "N/A"  # Set a safe default so the rest of the code survive


# get_api_data = lambda x = 0 : {}
# 
# try:
#     payload = get_api_data()
#     # If payload is missing the "temp" key, this throws a KeyError
#     val = payload["temp"] 
#     # If val is "unknown" instead of a number, this throws a ValueError
#     math = int(val) * 2   
# 
# except KeyError:
#     print("API changed their JSON format! Missing 'temp' key.")
# except ValueError:
#     print("API sent corrupted text instead of a number!")
# finally :
# 	print('end')
    
    
def check_battery(voltage):
    if voltage > 5.0:
        # The code is fine, but the hardware is about to fry. Force a crash!
        raise ValueError("CRITICAL: Overvoltage detected! Halting to save components.")
    return "Battery Normal"

print(check_battery(22))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    