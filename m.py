import u
soil_plants = [Entities.Carrot, Entities.Pumpkin, Entities.Cactus, Entities.Sunflower]

def every_tile(func):
	def row():
		for _ in range(get_world_size() - 1):
			func()
			move(East)
		func()

	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

def single_plant(d_ground, d_plant):
	def action():
		harvested = False
		if get_ground_type() != d_ground:
			harvest()
			harvested = True
			till()
		if get_entity_type() != d_plant:
			if not harvested:
				harvest()
			plant(d_plant)
	return action  # <-- return the inner callable

# harvests and plants in a single tile  
# does not harvest premature plants      
# modes: 
#  "g" for greedy - harvest crop if it does not match desired
#  "f" for frugal - harvest crop only if ready, then plant
def harvest_plant(d_plant, mode, water_level = 0, fert = False):
	def action():
		# harvest based on mode
		if mode == "g":
			if get_entity_type() != d_plant:
				harvest()
		elif mode == "f":
			if not can_harvest() and fert == True:
				use_item(Items.Fertilizer)
			if can_harvest():
				harvest()
		# till when required
		if get_ground_type() != Grounds.Soil and d_plant in soil_plants:
			till() 
		elif get_ground_type() != Grounds.Grassland and d_plant not in soil_plants:
			till()
			
		# plant if desired crop is not grass
		if d_plant != Entities.Grass:
			plant(d_plant)
			
		# water if needed
		if water_level != 0:
			u.water(water_level)
	return action
	
# plants in a single tile      
# modes: 
#  "g" for greedy - harvest crop if it does not match desired
#  "f" for frugal - harvest crop only if ready, then plant
def just_plant(d_plant, water_level = False, fert = False):
	def action():
		# harvest if incorrect plant detected
		if get_entity_type() != d_plant:
			harvest()

		# till when required
		if d_plant in soil_plants:                
			if get_ground_type() != Grounds.Soil:
				till()
		elif get_ground_type() == Grounds.Soil:
			till()
			
			
		# plant if desired crop is not grass
		if d_plant != Entities.Grass:
			plant(d_plant)
			
		# water if needed
		if water_level != 0:
			u.water(water_level)
			
		if fert:
			u.full_fert()
	return action

def every_array(func, orientation = "h"):
	if orientation == "h":
		next_array_dir = North
	elif orientation == "v":
		next_array_dir = East
		
	for _ in range(get_world_size()):
		if not spawn_drone(func):
			func()
		move(next_array_dir)

# wait until drones are completed their sub-tasks before continuing
def pause():
	while num_drones() > 1:
		pass

# runs a function across an array n times
def one_column(func, n):
	def action():    
		for i in range(n * u.size):
			func()
			move(North)
	return action
	
# pass in coordinates to move to and harvest
def target_harvest(x,y, fert = False):
	def action():
		u.move_to(x,y)
		if fert:
			u.full_fert()
		harvest()
	return action
	
def sleep(interval):
	for i in range(interval - 3):
		pass
		