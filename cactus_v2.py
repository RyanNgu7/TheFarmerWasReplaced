import u,m

m_drones = max_drones()

# Wait until a given time
def sync(go_time):
	while get_time() < go_time:
		pass	
def plant_row():
	for i in range(u.size):
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		move(East)
	
def sub_cactus(go_time, swap_dir, move_dir):
	def wrapper():
		sync(go_time) # wait
		
		# swaps
		for i in range(u.size):
			for j in range(u.size-1):
				if measure() > measure(swap_dir):
					swap(swap_dir)
				else:
					m.sleep(200)
			move(move_dir)
	return wrapper
def cactus_field():
	# plant field
	m.every_tile(m.just_plant(Entities.Cactus))
	u.move_to(0,0)
	
	# row sorting
	go = get_time() + 2.1 # takes ~2s to spawn all drones
	swap_dir = East
	move_dir = North
	for i in range(u.size - 1):
		last_drone = spawn_drone(sub_cactus(go, swap_dir, move_dir))
		move(swap_dir)
		
	# column sorting
	
	u.move_to(0,0)
	wait_for(last_drone)
	swap_dir = North
	move_dir = East
	go = get_time() + 2.1 # takes ~3s to spawn all drones
	for i in range(u.size - 1):
		last_drone = spawn_drone(sub_cactus(go, swap_dir, move_dir))
		move(swap_dir)
	wait_for(last_drone)
	harvest()
	
while True:
	start = get_time()
	cactus_field()
	end = get_time()
	quick_print(end - start, "Seconds")