password = "Secure9X"


has_number = False

for char in password:
    if "0" <= char <= "9":
        has_number = True
        break
    
if len(password) >= 8 and has_number:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")