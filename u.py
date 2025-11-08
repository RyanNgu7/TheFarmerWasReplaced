size = get_world_size()
# pass -1 to stay still in that axis
def move_to(d_x = -1, d_y = -1):
	if d_x == -1:
		d_x = get_pos_x()
	if d_y == -1:
		d_y = get_pos_y()
	
	c_x = get_pos_x() # current x
	c_y = get_pos_y() # current y
	middle = size / 2
	
	steps_x = d_x - c_x
	steps_y = d_y - c_y
	
	if steps_x > 0:
		for i in range(steps_x):
			move(East)
	elif steps_x < 0:
		for i in range(-steps_x):
			move(West)
			
	if steps_y > 0:
		for i in range(steps_y):
			move(North)
	elif steps_y < 0:
		for i in range(-steps_y):
			move(South)
			
def frugal_plant(d_ground, d_plant):
	for x in range(size):
		for y in range(size):
			# Ensure correct ground
			if not get_ground_type() == d_ground:
				harvest()
				till()
			
			# Ensure correct plant
			if not get_entity_type() == d_plant:
				harvest()
				plant(d_plant)
			
			move(North)
		move(East)

def water(min_water):
	def action():
		if get_water() < min_water:
			use_item(Items.Water)
	return action
		
# spams fertilizer and plant until the crop
def full_fert():
	while not can_harvest():
		use_item(Items.Fertilizer)
	
# flip n times
def flip_n(n):
	for i in range(n):
		do_a_flip()