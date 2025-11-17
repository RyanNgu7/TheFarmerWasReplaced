size = get_world_size()

# t_x,t_y - target (x,y); pass -1 to stay
# in in x or y axis
def move_to(t_x, t_y):
	# calculate distances from c_x to t_x
	c_x = get_pos_x()
	direct_dx = t_x - c_x
	if (direct_dx != 0) and t_x >= 0:
		wrap_dx = size - abs(direct_dx)
		if abs(direct_dx) <= abs(wrap_dx):		# use direct path
			if direct_dx > 0:	
				for i in range(direct_dx):
					move(East)
			else:
				for i in range(-direct_dx):
					move(West)
		else:									# use wrap path
			if direct_dx > 0:
				for i in range(wrap_dx):
					move(West)
			else:
				for i in range(wrap_dx):
					move(East)

	# calculate distances from c_y to t_y
	c_y = get_pos_y()
	direct_dy = t_y - c_y
	if (direct_dy != 0) and t_y >= 0:
		wrap_dy = size - abs(direct_dy)
		if abs(direct_dy) <= abs(wrap_dy):		# use direct path
			if direct_dy > 0:	
				for i in range(direct_dy):
					move(North)
			else:
				for i in range(-direct_dy):
					move(South)
		else:									# use wrap path
			if direct_dy > 0:
				for i in range(wrap_dy):
					move(South)
			else:
				for i in range(wrap_dy):
					move(North)
			
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