def text_processing():
	file = open("input.txt", "r")
	t = int(file.readline())
	bID = list(map(int, filter(lambda x: x != 'x', file.readline().rstrip().split(","))))
	return t, bID

def part1(ttl, busID):
	can_depart = []
	# for id in busID:
	# 	if ttl % id == 0:
	# 		can_depart[id] = (ttl // id) * id
	# 	else:
	# 		can_depart[id] = ((ttl // id) + 1 ) * id

	for i in range(len(busID)):
		if ttl % busID[i] == 0:
			can_depart.insert(i, (ttl // busID[i]) * busID[i]) 
		else:
			can_depart.insert(i, ((ttl // busID[i]) + 1 ) * busID[i]) 

	time = min(can_depart)
	time_to_wait = time - ttl
	bus_to_take = busID[can_depart.index(min(can_depart))]
	return bus_to_take * time_to_wait



leave_at, busID = text_processing()
# print(busID)
# for b in busID:
# 	print(b)

print("Solution Part 1:", part1(leave_at, busID)) 