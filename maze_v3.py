import u, m

def mini_maze(iterations, maze_size):
	def action():
		init_x = get_pos_x()
		init_y = get_pos_y()
		do_a_flip()
		
		for i in range(iterations):
			# create maze
			plant(Entities.Bush)
			substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, substance)
			
			# define directions (turning logic)
			directions = [North, East, South, West]
			index = 0
			
			# find treasure
			while get_entity_type() != Entities.Treasure:
				index = (index - 1) % 4
			
				while move(directions[index]) == False:
					index = (index + 1) % 4
							
			# treasure found
			harvest()
			u.move_to(init_x,init_y)
	return action
	
def maze_v3(iterations):
	# setup
	clear()
	maze_size = 5
	offset = maze_size // 2
	num_mazes = u.size // maze_size # 6 mazes per column/row
	u.move_to(offset,offset)
	
	for big_x in range(num_mazes):
		for big_y in range(num_mazes):
			# spawn drone
			if not spawn_drone(repeated_a_star(iterations, maze_size)):
				mini_maze(iterations, maze_size)()
			# move up/down, depending on column
			if (big_y+1) < num_mazes:	# on last maze of column, do not move up/down
				for i in range(maze_size):
					if big_x % 2 == 0:
						move(North)
					else:
						move(South)
		for i in range(maze_size):
			move(East)

if __name__ == "__main__":
	while True:
		maze_v3(300)		
#clear()
#u.move_to(5,5)
#mini_maze(100,5)()