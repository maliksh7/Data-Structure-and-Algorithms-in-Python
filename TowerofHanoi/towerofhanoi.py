def tower_of_hanoi(levels = 3):
	move_tower(levels, 'A' , 'B' , 'C')

def move_tower(l, fr , to , ax):
	if l == 1:
		print_move(l , fr , to)
		return

	move_tower(l-1 , fr , ax , to)
	print_move(l, fr, to)
	move_tower(l-1, ax, to, fr)	

def print_move(l, fr, to):
	print("Move: ", l, "from", fr, "to", to)

tower_of_hanoi(3)			