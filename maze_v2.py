import u, m

# wall - "l" or "r" 
def solve(wall = "l"):
	def action():
		directions = [North, East, South, West]
		index = 0
		
		while not (get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Grass):
				# if hugging right wall
				if wall == "r":
					index = (index + 1) % 4
				
					while move(directions[index]) == False:
						index = (index - 1) % 4
				# if hugging left wall
				if wall == "l":
					index = (index - 1) % 4
				
					while move(directions[index]) == False:
						index = (index + 1) % 4
						
		# treasure found
		harvest()
	return action
def maze():
	#create maze
	harvest()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	spawn_drone(solve("l"))
	solve("r")()

while True:
	maze()