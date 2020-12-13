file = open("input.txt", "r")
lines = file.readlines()
file.close()

bags = {}
count = 0
for line in lines:
	colors = line.split("contain")
	bags[colors[0].strip()] = colors[1].strip()

print(len(bags))

for line in lines:
	colors = line.split("contain")
	right_side = colors[1].strip().split(",")
	if "shiny" in colors[1].strip():
		count += 1
	else:
		for b in right_side:
			bag = b[2:].strip()
			if bag in bags.keys():
				if "shiny" in bags[bag]:
					count += 1

print(count)
