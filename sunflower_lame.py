import u
import m

def sunflower_lame():
	plant_cost1 = get_cost(Entities.Sunflower)[Items.Carrot]
	f_cost1 = (plant_cost1 * u.size ** 2)
	
	#if (num_items(Items.Hay) < f_cost1) or (num_items(Items.Wood) < f_cost2):
		#for i in range(5):
		#	bush_field()
	u.move_to(0,0)
	sunflower = m.harvest_plant(Entities.Sunflower, "f", 0.9)
	column = m.one_column(sunflower, 10)
	m.every_array(column, "v")
 
if __name__ == "__main__":
	while True:
		sunflower_lame()