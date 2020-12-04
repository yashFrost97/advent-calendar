file = open("input.txt", "r")

my_input = []
for line in file:
	my_input.append(line.strip())

file.close()


def text_processing(t):
	l = t.split(" ")
	first, second = [int(x) for x in l[0].split("-")]

	to_check = l[1].replace(":", "")
	password = l[2].strip()
	return first, second, to_check, password


def part_one(text):
	valid = 0
	for t in text:
		# text processing
		lower, higher, to_check, password = text_processing(t)
		# password validator
		cnt = 0
		for p in password:
			if p == to_check:
				cnt += 1

		if lower <= cnt <= higher:
			valid += 1
	return valid


def part_two(text):
	valid = 0
	for t in text:
		# text processing
		first, second, to_check, password = text_processing(t)
		# change to indexing by 1
		start = first - 1
		end = second - 1

		if start <= len(password):
			t1 = password[start]
		if end <= len(password):
			t2 = password[end]

		if [t1,t2].count(to_check) == 1:
			valid += 1

	return valid


print(part_one(my_input))
print(part_two(my_input))
