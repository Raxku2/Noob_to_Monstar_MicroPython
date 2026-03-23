from urandom import  getrandbits

player = ''

chance = getrandbits(1)

r1c1 = 1
r1c2 = 2
r1c3 = 3
r2c1 = 4
r2c2 = 5
r2c3 = 6
r3c1 = 7
r3c2 = 8
r3c3 = 9

def board():
	print(f" {r1c1} | {r1c2} | {r1c3} ")
	print(f" {r2c1} | {r2c2} | {r2c3} ")
	print(f" {r3c1} | {r3c2} | {r3c3} ")


def winCheck(playerId):
	if (r1c1 == r1c2 == r1c3 == playerId) or (r2c1 == r2c2 == r2c3 == playerId) or (r3c3 == r3c1 == r3c2 == playerId) or (r1c1 == r2c1 == r3c1 == playerId) or (r1c2 == r2c2 == r3c2 == playerId) or (r1c3 == r2c3 == r3c3 == playerId) or (r1c1 == r2c2 == r3c3 == playerId) or (r1c3 == r2c2 == r3c1 == playerId):
		return True 
	else :
		return False


while True :
	
	board()

	if chance == 1:
		player = "O"
	else :
		player = "X"

	choice = int(input(f"Player {player} : "))


	if choice == 1:
		if r1c1 == "O" or r1c1 == "X":
			continue 
		r1c1 = player
	
	elif choice == 2:
		if r1c2 == "O" or r1c2 == "X":
			continue 
		r1c2 = player
	
	elif choice == 3:
		if r1c3 == "O" or r1c3 == "X":
			continue 
		r1c3 = player
	
	elif choice == 4:
		if r2c1 == "O" or r2c1 == "X":
			continue 
		r2c1 = player
	
	elif choice == 5:
		if r2c2 == "O" or r2c2 == "X":
			continue 
		r2c2 = player
	
	elif choice == 6:
		if r2c3 == "O" or r2c3 == "X":
			continue 
		r2c3 = player
	
	elif choice == 7:
		if r3c1 == "O" or r3c1 == "X":
			continue 
		r3c1 = player
	
	elif choice == 8:
		if r3c2 == "O" or r3c2 == "X":
			continue 
		r3c2 = player
	
	elif choice == 9:
		if r3c3 == "O" or r3c3 == "X":
			continue 
		r3c3 = player
	else :
		break 

	if winCheck(player):
		print(f"Player {player} win!!")
		break 

	if chance == 1:
		chance = 0
	else :
		chance = 1
