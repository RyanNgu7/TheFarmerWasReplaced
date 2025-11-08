import u
import m
from bush_hay import bush_field

def carrot_field():
	plant_cost1 = get_cost(Entities.Carrot)[Items.Hay]
	plant_cost2 = get_cost(Entities.Carrot)[Items.Wood]
	f_cost1 = (plant_cost1 * u.size ** 2) * 10
	f_cost2 = (plant_cost1 * u.size ** 2) * 10
	
	if (num_items(Items.Hay) < f_cost1) or (num_items(Items.Wood) < f_cost2):
		for i in range(5):
			bush_field()
	u.move_to(0,0)
	carrot = m.harvest_plant(Entities.Carrot, "f", 0.9)
	column = m.one_column(carrot, 10)
	m.every_array(column, "v")
 
if __name__ == "__main__":
	while True:
		carrot_field()