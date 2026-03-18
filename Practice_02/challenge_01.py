raw_payloads = [
    {"id": 1, "temp": 22.5, "status": "OK"},
    {"id": 2, "status": "ERROR", "error_code": 404},
    {"id": 3, "temp": 25.1, "status": "OK"},
    {"id": 4, "temp": -99, "status": "OK"}, # Faulty reading
    {"id": 5, "status": "OK"}               # Missing temp key entirely
]


	
def sanitize_payloads(payload_list):
	for data in payload_list:
		if data.get('status') != 'OK':
			continue
		
		if not data.get('temp') or data.get('temp') < 0:
			data['temp'] = 0.0
			
		
	payload_list.sort(key= lambda k : k['id'])
	return (payload_list)
	
	
print(sanitize_payloads(raw_payloads))