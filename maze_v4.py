from pq import pq_pop, pq_push
import u
# -----------------
# Helper functions
# -----------------

# Check if treasure found
def goal_check():
	return get_entity_type() == Entities.Treasure

# Manhattan distance heuristic
# calculates distance between point a (ax,ay) and b (bx,by)
def heuristic(a, b):
	ax, ay = a
	bx, by = b
	return abs(ax - bx) + abs(ay - by)
	
# Convert two positions to movement direction
def direction_to(current, next_pos):
	cx, cy = current
	nx, ny = next_pos
	if nx > cx:
		return East
	if nx < cx:
		return West
	if ny > cy:
		return North
	if ny < cy:
		return South
	return None
	
# Return neighbors with directions
def get_neighbors(pos):
	x, y = pos
	return [
		((x, y+1), North),
		((x+1, y), East),
		((x, y-1), South),
		((x-1, y), West)
	]
	
# Reconstruct path from came_from dict
def reconstruct_path(came_from, current):
	path = [current]
	while current in came_from:
		current = came_from[current]
		path.insert(0, current)
	return path
	
DIRECTIONS = [North, East, South, West]
# ------------------------------
# Core A* function
# ------------------------------
def a_star(start, goal, known_walls):
	frontier = []	# Walls to explore, priority queue, open set
	visited = set() # tiles already visited
	pq_push(frontier, start, 0)

	came_from = {}
	cost_so_far = {}
	cost_so_far[start] = 0
	
	while len(frontier) > 0:
		current = pq_pop(frontier)

		# Goal reached
		if current == goal:
			return reconstruct_path(came_from, current)
			
		# Skip already expanded nodes
		if current in visited:
			continue
		else:
			visited.add(current)

		neighbors_list = get_neighbors(current)
		for neighbor, direction in neighbors_list:
			# Skip blocked moves
			if (current, direction) in known_walls:
				continue
			
			new_cost = cost_so_far[current] + heuristic(current,neighbor)
			if (neighbor not in cost_so_far) or (new_cost < cost_so_far[neighbor]):
				cost_so_far[neighbor] = new_cost

				priority = new_cost + heuristic(neighbor, goal)		
				pq_push(frontier, neighbor, priority)
				came_from[neighbor] = current

	return None  # no path found

# ------------------------------
# Repeated A* Main Loop
# ------------------------------

def repeated_a_star(relocations, maze_size):
	def action():
		init_x = get_pos_x()
		init_y = get_pos_y()
		do_a_flip()
		solves_done = 0
		known_walls = set()  # ((x,y), direction) for walls
	
		# Plant maze
		plant(Entities.Bush)
		substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		
		while solves_done < relocations:
			if goal_check():
				use_item(Items.Weird_Substance, substance)
				solves_done += 1
				if solves_done >= relocations:
					break
			start = (get_pos_x(), get_pos_y())
			goal = measure()  # could be treasure position or nearest frontier
	
			path = a_star(start, goal, known_walls)
			if not path:
				print("No valid path f")
				return  # No path found
	
			for next_pos in path[1:]:
				
					
				x, y = get_pos_x(), get_pos_y()
	
				# Sense walls in all directions
				for d in DIRECTIONS:
					wall = ((x,y), d)
					if not can_move(d):
						known_walls.add(wall)
					else:
						# Wall removal
						if ((x,y), d) in known_walls:
							known_walls.remove(wall)
	
				# Compute direction to next tile
				move_dir = direction_to((x, y), next_pos)
	
				# Move if possible, else update wall and replan
				if can_move(move_dir):
					move(move_dir)
				else:
					known_walls.add(((x, y), move_dir))
					break  # break to re-run A*
		harvest()
	return action

def maze_v4(relocations):
	# setup
	clear()
	maze_size = 5
	offset = maze_size // 2
	num_mazes = u.size // maze_size # 6 mazes per column/row
	u.move_to(offset,offset)
	
	for big_x in range(num_mazes):
		for big_y in range(num_mazes):
			# spawn drone
			if not spawn_drone(repeated_a_star(relocations, maze_size)):
				repeated_a_star(relocations, maze_size)()
				return
			# move up/down, depending on column
			if (big_y+1) < num_mazes:	# on last maze of column, do not move up/down
				for i in range(maze_size):
					if big_x % 2 == 0:
						move(North)
					else:
						move(South)
		for i in range(maze_size):
			move(East)
			
maze_v4(20)