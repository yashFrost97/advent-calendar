# solution from https://github.com/mebeim/aoc/blob/master/2020/README.md
# couldnt figure it out
from copy import deepcopy

file = open("input.txt", "r")
original = list(map(list, map(str.rstrip, file.readlines())))
file.close()
MAXROW, MAXCOL = len(original) - 1, len(original[0]) - 1
OCCUPIED, EMPTY, FLOOR = '#L.'
grid = deepcopy(original)


def occupied_neighbours(grid, r, c):
	"""" This function checks the neighbouring seats are occupied or not """
	deltas = ((-1, 0), (1, 0), (0, 1), (0, -1),
	          (-1, 1), (-1, -1), (1, 1), (1, -1))

	total = 0
	for dr, dc in deltas:
		rr, cc = r + dr, c + dc
		# checks only the immediate adjacent seats
		if 0 <= rr <= MAXROW and 0 <= cc <= MAXCOL:
			total += grid[rr][cc] == OCCUPIED

	return total

def evolve_seats(grid):
	while 1:
		previous = deepcopy(grid)

		for r, row in enumerate(previous):
			for c, col in enumerate(row):

				if col == FLOOR:
					continue

				neighbours = occupied_neighbours(previous, r, c)

				if col == EMPTY and neighbours == 0:
					grid[r][c] = OCCUPIED
				if col == OCCUPIED and neighbours >= 4:
					grid[r][c] = EMPTY

		if grid == previous:
			return sum(row.count(OCCUPIED) for row in grid)

		# previous = grid


print(evolve_seats(grid))

# def text_processing():
# 	file = open("test.txt", "r")
# 	lines = file.read().splitlines()
# 	return lines
#
#
# def arrangement(seating_map):
# 	old_map = seating_map.copy()
# 	for row in seating_map:
# 		for i in range(len(row)):
# 			empty = False
# 			# check to fill the seat
# 			if row[i] == "L":
# 				try:
# 					if (row[i-1] == "L" or row[i-1] == ".") and (row[i+1] == "L" or row[i+1] == "."):
# 						row[i] == "L"
# 				except:
# 					# list out of bound
#
# seat_map = text_processing()
# print(seat_map)
# arrangement(seat_map)
