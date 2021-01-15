LEFT, RIGHT, FORWARD = 'LRF'
NORTH, SOUTH, EAST, WEST = 'NSEW'

ROTMAP = {
	(LEFT, 90): lambda x_rot, y_rot: (-y_rot, x_rot),
	(LEFT, 180): lambda x_rot, y_rot: (-x_rot, -y_rot),
	(LEFT, 270): lambda x_rot, y_rot: (y_rot, -x_rot),
	(RIGHT, 90): lambda x_rot, y_rot: (y_rot, -x_rot),
	(RIGHT, 180): lambda x_rot, y_rot: (-x_rot, -y_rot),
	(RIGHT, 270): lambda x_rot, y_rot: (-y_rot, x_rot)
}

MOVEMAP = {
	NORTH: lambda x_move, y_move, n: (x_move, y_move + n),
	SOUTH: lambda x_move, y_move, n: (x_move, y_move - n),
	EAST: lambda x_move, y_move, n: (x_move + n, y_move),
	WEST: lambda x_move, y_move, n: (x_move - n, y_move)
}

file = open("input.txt", "r")
commands = tuple(map(lambda l: (l[0], int(l[1:])), file))
file.close()


# ***********************
# PART 1
# ***********************
x, y = 0, 0
dx, dy = 1, 0

for cmd, units in commands:
	if cmd == FORWARD:
		x += dx * units
		y += dy * units
	elif cmd == LEFT or cmd == RIGHT:
		dx, dy = ROTMAP[cmd, units](dx, dy)
	else:
		# north south east west
		x, y = MOVEMAP[cmd](x, y, units)

print("Part 1: ", abs(x) + abs(y))

# ***********************
# PART 2
# ***********************

x, y = 0, 0
dx, dy = 10, 1

for cmd, units in commands:
	if cmd == FORWARD:
		x += dx * units
		y += dy * units
	elif cmd == LEFT or cmd == RIGHT:
		dx, dy = ROTMAP[cmd, units](dx, dy)
	else:
		# north south east west
		dx, dy = MOVEMAP[cmd](dx, dy, units)


print("Part 2: ", abs(x) + abs(y))
