input_file = open("input.txt", "r")

my_input = []
for line in input_file:
	my_input.append(int(line))

tgt = 2020


def part_one(nums, target):
	# this function would return the indexes at which the the sums is 2020
	table = {}

	for i in range(len(nums)):
		table[nums[i]] = i

	for i in range(len(nums)):
		temp = target - nums[i]

		if temp in table and table[temp] != i:
			return [i, table.get(temp)]


result_index = part_one(my_input, tgt)
print(my_input[result_index[0]], my_input[result_index[1]])
print("Part 1 ans = ", my_input[result_index[0]] * my_input[result_index[1]])
# map = {}
# result = []
# for i in range(len(input)):
# 	map[input[i]] = i
#
# for i in range(len(input)):
# 	num2 = target - input[i]
#
# 	if num2 in map and map[num2] != i:
# 		result.append(i)
# 		result.append(map.get(num2))
#
# print(result)
# print(result[0] * result[1])
