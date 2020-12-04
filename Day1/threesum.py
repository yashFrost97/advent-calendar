input_file = open("../Day2/input.txt", "r")

nums = []
for line in input_file:
	nums.append(int(line))

set_nums = set(nums)
tgt = 2020


def threesum(numbers, set_numbers):
	for n1 in numbers:
		for n2 in numbers:
			temp = tgt - n1 - n2
			if temp in set_numbers:
				return temp * n1 * n2


print(threesum(nums, set_nums))
