import u,m

# start, end - range of columns to be measured
# returns a dict of sets with coor
def sunflower_zone(start, end):
	def action():
		# initialize dict
		sub_dict = {}
		for i in range(7, 16):
			sub_dict[i] = []
		
		# measure 1 col at a time
		for x in range(start, end):
			u.move_to(x,0)
			for y in range(u.size):
				m.just_plant(Entities.Sunflower, True)()
				petals = measure()
				coords = (x,y)
				sub_dict[petals].append(coords)
				move(North)
		return sub_dict
	return action

def sunflower_field():
	# harvest carrots if needed
	single_cost = get_cost(Entities.Sunflower)[Items.Carrot]
	field_cost = single_cost * u.size ** 2
	if num_items(Items.Carrot) < field_cost:
		for _ in range(5):
			carrot_field()
	
	# initialize main_dict
	main_dict = {}
	for i in range(7, 16):
		main_dict[i] = []
	
	u.move_to(0,0)

	# calculate zones for each drone
	m_drones = max_drones()
	base_size = u.size // m_drones
	remainder = u.size % m_drones
	drone_list = []
	start = 0
	for i in range(m_drones):
		if i < remainder:
			extra = 1
		else:
			extra = 0
		end = start + base_size + extra
		drone = spawn_drone(sunflower_zone(start, end))
	
		if drone:
			drone_list.append(drone)
		else:
			main_dict = sunflower_zone(start,end)()
		
		start = end
	
	# merge sub_dicts into main_dict
	for drone in drone_list:                        # traverse list of drones
		sub_dict = wait_for(drone)                  # retrieve dict from worker drone
		for key in range(15,6,-1):
			for value in sub_dict[key]:
				main_dict[key].append(value)
				
	# harvest sunflowers in order
	middle = u.size // 2
	u.move_to(middle, middle)
	#u.flip_n(7)
	for most_petals in range(15,6, -1):    
		most_p_list = main_dict[most_petals]
		# iterate through each list
		while len(most_p_list) > 0:
			x,y = most_p_list.pop(0)
			drone = spawn_drone(m.target_harvest(x,y,True))

		#wait_for(drone) # wait for last drone
			
if __name__ == "__main__":
	while True:
		sunflower_field()

