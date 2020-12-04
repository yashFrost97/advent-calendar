file = open("input.txt", "r")

slope = []
for line in file:
	slope.append(line.strip())

file.close()


def slope_traversal(graph, right=3, down=1):
	col_pointer = 0
	treecount = 0
	for row in graph[::down]:
		col_pointer = col_pointer % len(row)
		if row[col_pointer] == '#':
			treecount += 1
		col_pointer += right

	return treecount


ans1 = slope_traversal(slope, 1, 1)
ans2 = slope_traversal(slope, 3, 1)
ans3 = slope_traversal(slope, 5, 1)
ans4 = slope_traversal(slope, 7, 1)
ans5 = slope_traversal(slope, 1, 2)

print("Product is ", ans1 * ans2 * ans3 * ans4 * ans5)