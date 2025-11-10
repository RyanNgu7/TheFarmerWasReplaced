import u,m
def bush_array():
	for _ in range(u.size):
		plant(Entities.bush)
		move(North)

def hay_array():
	while True:
		if can_harvest():
			harvest()
		move(North)
u.move_to(0,0)
for _ in range(u.size):
	if get_pos_x() % 2 == 0:
		temp = spawn_drone(bush_array)
	move(East)

wait_for(temp)
for _ in range(u.size):
	if get_pos_x() % 2 == 1:
		if not spawn_drone(hay_array):
			hay_array()
	move(East)
for _ in range(u.size):
	if get_pos_x() % 2 == 1:
		if not spawn_drone(hay_array):
			hay_array()
	move(East)
	
