import u
import m
from pumpkin_v2 import pumpkin_field
def sort(sort_dir, switch_array):
	u.move_to(0,0)
	for i in range(u.size):                    
		for j in range(u.size - 1):            # 1 loop = 1 array
			swapped = False
			for k in range(u.size - j - 1):    # one pass
				if measure() > measure(sort_dir):
					swap(sort_dir)
					swapped = True
				move(sort_dir)
			if swapped == False:
				break
			# move to beg. of array after a pass is sorted
			if sort_dir == East:
				u.move_to(0,-1)
			else:
				u.move_to(-1,0)    
		# move to beg. of array after a row is sorted                
		if sort_dir == East:
			u.move_to(0,-1)
		else:
			u.move_to(-1,0)   
		move(switch_array)

# orientation: "h" (vertical) or "v" (horizontal)
def sort_array(orientation):
	def action():
		# move to starting position of array
		if orientation == "h":
			sort_dir = East
			u.move_to(0,-1)
		elif orientation == "v":
			sort_dir = North
			u.move_to(-1,0)
			
		for j in range(u.size - 1):            # size-1 passes
			swapped = False
			for k in range(u.size - j - 1):    # one pass
				#current = measure()
				#next = measure(sort_dir)
				#if next == None:
				 #   do_a_flip()
				if measure() > measure(sort_dir):
					swap(sort_dir)
					swapped = True
				move(sort_dir)
				
			# after pass, reset pos
			if orientation == "h":
				u.move_to(0,-1)
			elif orientation == "v":
				u.move_to(-1,0)                    
			
			# if no swaps made, stop sorting
			if swapped == False:
				break
	return action

def cactus_field():
	plant_cost = get_cost(Entities.Cactus)[Items.Pumpkin]
	field_cost = plant_cost * u.size ** 2
	if num_items(Items.Pumpkin) < field_cost:
		for i in range(5):
			mega_pumpkin()
		
	# plant field
	u.move_to(0,0)
	m.every_tile(m.harvest_plant(Entities.Cactus, "g"))
	m.pause()
	# sort horizontally
	m.every_array(sort_array("h"), "h")
	
	m.pause()
	
	# sort vertically
	m.every_array(sort_array("v"), "v")
	
	m.pause()

	harvest()
	
if __name__ == "__main__":
	while True:
		cactus_field()