import u

while True:
	for i in range(u.size):
		if can_harvest():
			harvest()
		if get_pos_x() % 2 == 0:            # x is even
			if get_pos_y() % 2 == 0:        # y is even
				plant(Entities.Tree)
			else:
				if get_ground_type() == Grounds.Soil:
					till()
		else:                               # x is odd    
			if not get_pos_y() % 2 == 0:  # y is odd
				plant(Entities.Tree)
			else:
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Carrot)
		move(East)
	move(North)
	