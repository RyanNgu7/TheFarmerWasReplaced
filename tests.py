import u,m

for i in range(2):
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)
	move(East)
	
u.move_to(0,0)
quick_print("before swap", get_tick_count())
swap(East)
quick_print("after swap",get_tick_count())
m.sleep(200)
quick_print("after sleep",get_tick_count())
