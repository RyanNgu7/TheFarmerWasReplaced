import u,m
OPP_DIRS = {North: South,
		   East: West,
		   South: North,
		   West: East}
   
# compare current cactus with next cactus.
# if current cactus is greater than next cactus, swap
def measure_swap(measure_dir):
	global swapped
	if measure_dir == East:
		left = measure()
		right = measure(East)
	elif measure_dir == West:
		left = measure(West) 
		right = measure()
	elif measure_dir == North:
		left = measure()
		right = measure(North)
	elif measure_dir == South:
		left = measure(South)
		right = measure()
	
	if (left > right):
		swap(measure_dir)
		swapped = True

# till, plant, and swap cacti in the direction of measure_dir
def till_plant(measure_dir):
	global swapped
	# till
	if get_ground_type() != Grounds.Soil:
		till()
	# plant 
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)

	# swap
	previous = measure(measure_dir)
	current = measure()
	
	if previous and (previous > current):
		swap(measure_dir)
		swapped = True

# sorts a single array of cacti
# ensure drone starts at beg. of array
def cocktail_array(sort_dir, plant = True):
	def action():
		rev_sort_dir = OPP_DIRS[sort_dir]
		global swapped
		start = 0
		end = u.size-1
		
		if sort_dir == East:
			u.move_to(start,-1)	# y-axis stays the same
		else:
			u.move_to(-1,start)	# x-axis stays the same
			
		# initial plant and single pass from start to end
		for _ in range(start,end):
			till_plant(rev_sort_dir)
			move(sort_dir)
		till_plant(rev_sort_dir)
		end -= 1
	
		# stop sorting if no swaps after a pass
		if (swapped == False):
			return
		
		# loop until sorted
		while swapped == True:
			swapped = False
			
			# move to end
			if sort_dir == East:
				u.move_to(end,-1)	# y-axis stays the same
			else:
				u.move_to(-1,end)	# x-axis stays the same

			# sort from END to START
			for _ in range(end, start+1, -1):
				measure_swap(rev_sort_dir)
				move(rev_sort_dir)
			measure_swap(rev_sort_dir)
			start += 1

			# stop sorting if no swaps
			if (swapped == False):	
				break

			# move to start
			if sort_dir == East:
				u.move_to(start,-1)	# y-axis stays the same
			else:
				u.move_to(-1,start)	# x-axis stays the same

			# sort from START to END
			for _ in range(start,end-1):
				measure_swap(sort_dir)
				move(sort_dir)
			measure_swap(sort_dir)
			end -= 1

	return action

def cactus_field():
	minion_arr = []
	# Sort horizontally
	u.move_to(0,0)
	sort_dir = East
	switch_dir = North
	for _ in range(u.size-1):
		minion = spawn_drone(cocktail_array(sort_dir))
		minion_arr.append(minion)
		move(switch_dir)
	cocktail_array(sort_dir)()
	
	# Sort vertically
	u.move_to(0,0)			# start pos
	for m in minion_arr:	# wait for all drones to die
		wait_for(m)
	minion_arr = []			# clear minion_arr
	sort_dir = North
	switch_dir = East
	for _ in range(u.size-1):
		minion = spawn_drone(cocktail_array(sort_dir,False))
		minion_arr.append(minion)
		move(switch_dir)
	cocktail_array(sort_dir)()
	for m in minion_arr:
		wait_for(m)
	harvest()

if __name__ == "__main__":
	while True:
		cactus_field()

#clear()
#cocktail_array(East)()
#cocktail_array(North)()