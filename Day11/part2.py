# solution from https://github.com/mebeim/aoc/blob/master/2020/README.md
# couldnt figure it out
from copy import deepcopy

file = open("input.txt", "r")
original = list(map(list, map(str.rstrip, file.readlines())))
MAXROW, MAXCOL = len(original) - 1, len(original[0]) - 1
OCCUPIED, EMPTY, FLOOR = '#L.'
grid = deepcopy(original)


def occupied_neighbours_insight(grid, r, c):
	"""" This function checks the neighbouring seats are occupied or not """
	deltas = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))

	total = 0
	for dr, dc in deltas:
		rr, cc = r + dr, c + dc

		# this loop checks in the direction beyond the first seat
		while 0 <= rr <= MAXROW and 0 <= cc <= MAXCOL:
			if grid[rr][cc] != FLOOR:
				if grid[rr][cc] == OCCUPIED:
					total += 1
				break

			rr += dr
			cc += dc

	return total


def evolve_seats(grid):
	while 1:
		previous = deepcopy(grid)

		for r, row in enumerate(previous):
			for c, col in enumerate(row):

				if col == FLOOR:
					continue

				neighbours = occupied_neighbours_insight(previous, r, c)

				if col == EMPTY and neighbours == 0:
					grid[r][c] = OCCUPIED
				if col == OCCUPIED and neighbours >= 5:
					grid[r][c] = EMPTY

		if grid == previous:
			return sum(row.count(OCCUPIED) for row in grid)

		# previous = grid


print("Part 2: ",evolve_seats(grid))
