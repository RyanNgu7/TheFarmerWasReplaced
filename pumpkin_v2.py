import u
import m
from carrot import carrot_field

fert_thresh = 5
# spams fertilizer and plant until ready
def pumpkin_fert():
	while not can_harvest():
		use_item(Items.Fertilizer)
		plant(Entities.Pumpkin)

def sub_pumpkin(sub_not_ready):
	def action():
		while len(sub_not_ready) > 0:
			x,y = sub_not_ready[0]
			u.move_to(x,y)
			temp = sub_not_ready.pop(0)
			if not can_harvest():
				plant(Entities.Pumpkin)
				u.water(0.5)
				sub_not_ready.append(temp)
				if len(sub_not_ready) <= fert_thresh:
					pumpkin_fert()
					sub_not_ready.pop()
	return action

def pumpkin_field():
	# harvest carrots if needed
	pumpkin_cost = get_cost(Entities.Pumpkin)[Items.Carrot]
	field_cost = pumpkin_cost * u.size ** 2
	if num_items(Items.Carrot) < field_cost * 2:
		for i in range(5):
			carrot_field()
			
	u.move_to(0,0)
	# fill farm
	m.every_tile(m.harvest_plant(Entities.Pumpkin, "g", 0.5))
	
	# wait for all drones to finish planting
	m.pause()
	# populate not_ready
	not_ready = []
	for x in range(u.size):
		for y in range(u.size):
			not_ready.append((x,y))
	
	num_pumpkins = len(not_ready)
	m_drones = max_drones()
	base_size = num_pumpkins // m_drones
	remainder = num_pumpkins % m_drones
	

	start = 0
	for i in range(m_drones):
		if i < remainder:
			extra = 1
		else:
			extra = 0
		end = start + base_size + extra
		sublist = not_ready[start:end]
		if not spawn_drone(sub_pumpkin(sublist)):
			sub_pumpkin(sublist)()
		start = end      
	m.pause()
	harvest()

if __name__ == "__main__":
	while True:
		pumpkin_field()