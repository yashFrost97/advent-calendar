file = open("input.txt", "r")
input = file.readlines()
file.close()

for i in range(len(input)):
	input[i] = input[i].replace("\n", "")

seats = []


def part_one(my_input):
	max_id = 0
	for inp in my_input:
		lower = 0
		upper = 127
		for j in inp[:-3]:

			if j == 'F':
				upper = int((lower + upper) / 2)
			if j == 'B':
				lower = int((lower + upper) / 2) + 1

		row = lower
		lower = 0
		upper = 7
		for j in inp[-3:]:

			if j == 'L':
				upper = int((lower + upper) / 2)
			if j == 'R':
				lower = int((lower + upper) / 2) + 1

		col = lower

		id = row * 8 + col
		seats.append(id)
		max_id = max(max_id, id)

	return max_id


def part_two(my_input):
	max_id = 0
	for inp in my_input:
		lower = 0
		upper = 127
		for j in inp[:-3]:

			if j == 'F':
				upper = int((lower + upper) / 2)
			if j == 'B':
				lower = int((lower + upper) / 2) + 1

		row = lower
		lower = 0
		upper = 7
		for j in inp[-3:]:

			if j == 'L':
				upper = int((lower + upper) / 2)
			if j == 'R':
				lower = int((lower + upper) / 2) + 1

		col = lower

		id = row * 8 + col
		seats.append(id)
	sorted_seats = sorted(seats)

	for i in range(len(sorted_seats) - 1):
		if sorted_seats[i] + 2 == sorted_seats[i + 2]:
			return sorted_seats[i] + 1

	return 0


print(part_one(input))
print(part_two(input))
