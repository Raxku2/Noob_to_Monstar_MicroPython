raw_voltages = [-5.0, 12.5, 105.0, 8.2, 0.0]

positive_filter = lambda x : x if x > 0 else None 
positive_only = list(filter(positive_filter, raw_voltages))

print(positive_only)
capped_voltages = list(map(lambda x: x if x <= 24.0 else 24.0, positive_only))

print(capped_voltages)


