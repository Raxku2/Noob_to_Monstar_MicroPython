fragmented_data = [1, [2, 3], [[4], 5], 6, [[[7]]]]

def flatten_data(nested_list):
	for data in nested_list:
		if type(data) == list:
			yield from flatten_data(data)
		
		if type(data) in [int,str,dict]:
# 			print(data)
			yield data
		
	

# print([item for item in flatten_data(fragmented_data)])
for item in flatten_data(fragmented_data):
	print(item)