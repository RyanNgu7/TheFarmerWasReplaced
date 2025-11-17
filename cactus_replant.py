import u,m

# orientation: "h" or "v"
# must spawn drone start of array
def replant_sort(orientation):
	def wrapper():
		if orientation == "h":
			# first cactus
			if get_ground_type() != Grounds.Soil:
					till()
			plant(Entities.Cactus)
			move(East)
			
			#middle cacti
			for _ in range(u.size-2):
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Cactus)
				prev = measure(West)
				while prev > measure():
					harvest()
					plant(Entities.Cactus)
				move(East)
			
			# last cacti
			if get_ground_type() != Grounds.Soil:
					till()
			plant(Entities.Cactus)
			prev = measure(West)
			while prev > measure():
				harvest()
				plant(Entities.Cactus)
			while not can_harvest():
				pass
		else:
			# first cacti
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			move(North)
			
			# middle cacti
			for i in range(u.size-2):
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Cactus)
				prev = measure(South)
				while prev > measure():
					harvest()
					plant(Entities.Cactus)
				move(North)
			
			# last cacti
			if get_ground_type() != Grounds.Soil:
					till()
			plant(Entities.Cactus)
			prev = measure(South)
			while prev > measure():
				harvest()
				plant(Entities.Cactus)
			while not can_harvest():
				pass
	return wrapper

def cactus_field():
	minion_arr = []
	
	# Sort horizontally
	u.move_to(0,0)
	orientation = "h"
	switch_dir = North
	for _ in range(u.size-1):
		minion = spawn_drone(replant_sort(orientation))
		minion_arr.append(minion)
		move(switch_dir)
	replant_sort(orientation)()
	
	# Sort vertically
	u.move_to(0,0)
	for m in minion_arr:	# wait for all drones to die
		wait_for(m)
	orientation = "v"
	switch_dir = East
	for _ in range(u.size-1):
		minion = spawn_drone(replant_sort(orientation))
		minion_arr.append(minion)
		move(switch_dir)
	replant_sort(orientation)()
	
	# harvest
	for m in minion_arr:	# wait for all drones to die
		wait_for(m)
	harvest()

if __name__ == "__main__":
	times = []
	clear()
	set_execution_speed(10000)
	while True:
		start = get_time()
		cactus_field()
		end = get_time()
		times.append(end-start)
		
