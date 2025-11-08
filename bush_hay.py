import u,m

def bush_single():
	x = get_pos_x()
	y = get_pos_y()
	
	if x % 2 == 0:
		if y % 2 == 0:
			m.harvest_plant(Entities.Tree, "f", 0.2)()
		else:
			use_item(Items.Weird_Substance)
			m.harvest_plant(Entities.Grass, "f", 0.2)()
	else:
		if y % 2 == 1:
			m.harvest_plant(Entities.Tree, "f", 0.2)()
		else:
			m.harvest_plant(Entities.Grass, "f", 0.2)()

def bush_field():
	m.every_tile(bush_single)

if __name__ == "__main__":
	while True:
		bush_field()