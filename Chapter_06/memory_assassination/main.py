from gc import collect,mem_free,mem_alloc
print('hello')

collect()
# print(f'total memory : {round((mem_free() + mem_alloc()) / 1024,3)} KB')
print(f'memory before: {round(mem_free() / 1024,2)} KB')


# a = 20
# b = 30
# c = 4000000000000000000000000000009

data = [20,30,4000000000000000000000000000009]

data = sensor_read()
print(data)
del data
del sensor_read
collect()
print(f'memory after: {round(mem_free() / 1024,2)} KB')
