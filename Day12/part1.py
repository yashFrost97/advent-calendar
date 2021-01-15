DirectionsDict = {
	"N" : (0, 1),
	"S" : (0, -1),
	"E" : (1, 0),
	"W" : (-1, 0)
}

def text_processing():
	file = open("input.txt", "r")
	directions = list(map(str.rstrip, file.readlines()))
	return directions


def traverse(directions):
	# 0 is east, 90 is north, 180 is west, 270 is south
	facing = 0
	# amount moved
	# x is along east and west. +ve is east, -ve is west
	# y is along north and south +ve is north, -ve is south
	dx = 0
	dy = 0

	for dir in directions:
		dirMove = dir[0]
		units = int(dir[1:])

		if dirMove in directions:
			x, y = directions[dirMove]
			dx += x * units
			dy += y * units

		elif dirMove == "L":
			facing = (facing + units) % 360
		elif dirMove == "R":
			facing = (facing - units) % 360

		else:
			if facing == 0:
				dx += units
			elif facing == 90:
				dy += units
			elif facing == 180:
				dx -= units
			elif facing == 270:
				dy -= units
	print(dx, dy)
	return manhattan_distance(dx, dy)


def manhattan_distance(x, y):
	return abs(x) + abs(y)


# def traverse(directions):
# 	ship_face = "E" # init position
# 	ship_dir = {"E" : 0, "W" : 0, "N" : 0, "S" : 0}
# 	ship_left = {"E" : "S", "S" : "W", "W" : "N", "N" : "W"}
# 	ship_right = {"E" : "N", "N" : "W", "W" : "S", "S" : "E"}
# 	for dir in directions:
# 		dirMove = dir[0]
# 		units = int(dir[1:])
#
# 		if dirMove == "E" or dirMove == "W" or dirMove == "N" or dirMove == "S":
# 			ship_dir[dirMove] += units
# 		if dirMove == "L":
# 			temp = 0
# 			while temp != units:
# 				ship_face = ship_left[ship_face]
# 				temp += 90
# 		if dirMove == "R":
# 			temp = 0
# 			while temp != units:
# 				ship_face = ship_left[ship_face]
# 				temp += 90
# 		if dirMove == "F":
# 			ship_dir[ship_face] += units
#
# 		# print(ship_face, dirMove, units)
# 		# print("ship directions", ship_dir)
# 		# print("***************************************")
#
#
# 	# print("ship directions", ship_dir)
# 	# print(ship_face)
# 	print(manhattan_distance(ship_dir))
#
#


dir = text_processing()
print(traverse(dir))