# Simple custom priority queue using set
#[[(x1,y1), p1],[(x2,y2), p2]...]
def pq_push(queue, item, priority):
	# Add a new item with its priority
	queue.append((item, priority))

def pq_pop(queue):
	if len(queue) == 0:
		return None

	best_index = 0
	best_priority = queue[0][1]

	for i in range(1, len(queue)):
		if queue[i][1] < best_priority:
			best_index = i
			best_priority = queue[i][1]
	
	return queue.pop(best_index)[0]