raw_data = [15, -4, 0, 42, 999, 8, -1]


while len(raw_data) > 0: 
    
    
    num = raw_data.pop(0)
    
    
    if num <= 0:  
        continue
    elif num == 999:
        print('SYSTEM HALT')
        break 
    else:
        
        print(f'Valid entry: {num}')