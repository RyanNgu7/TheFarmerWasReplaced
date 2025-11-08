import u
u.frugal_plant(Grounds.Soil, Entities.Pumpkin)
while True:
	not_ready = []
	
	# populate not_ready
	for x in range(u.size):
		for y in range(u.size):
			not_ready.append((x,y))
	
	while len(not_ready) > 0:
		x,y = not_ready[0]
		u.move_to(x,y)
		temp = not_ready.pop(0)
		if not can_harvest():
			plant(Entities.Pumpkin)
			not_ready.append(temp)
			if len(not_ready) < u.size:
				use_item(Items.Fertilizer)
	harvest()
	
