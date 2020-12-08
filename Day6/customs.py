file = open("input.txt", "r")
input = file.readlines()
file.close()




def part_one(input):
	seen_letters = set()
	count = 0
	for i in range(len(input)):

		if input[i] != "\n":
			input[i] = input[i].replace("\n", "")
			for letter in input[i]:
				if letter not in seen_letters:
					seen_letters.add(letter)

		if input[i] == "\n" or i > len(input):
			# new group would be encountered
			# purge the previous results
			count += len(seen_letters)
			seen_letters.clear()
	count += len(seen_letters)
	return count


def part_two(input):
	seen_letters = set()
	count = 0
	group = []
	for i in range(len(input)):

		if input[i] != "\n":
			input[i] = input[i].replace("\n", "")
			group.append(set(input[i]))

		if input[i] == "\n" or i > len(input):
			# new group would be encountered
			# purge the previous results
			count += len(set.intersection(*group))
			group.clear()
	count += len(set.intersection(*group))
	return count


print(part_one(input))
print(part_two(input))