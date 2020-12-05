file = open("input.txt", "r")
# file = open("test.txt", "r")
all_passports = []

needed_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


# part one
def passport_processor(lines):
	passport = {}
	valid_passports = 0
	valid_fields = 0
	passport_count = 0
	present = False
	for i in range(len(lines) + 1):
		# blank line is separator for the passports
		# all lines between blank lines are fields for passports
		# extract those lines. then split them into key value pairs
		# check the keys needed. if all keys present then we have a valid passport
		if i < len(lines):
			line = lines[i].strip()
		# print(line, i)
		if len(line.strip()) == 0 or i >= len(lines):
			# passport separator encountered
			# empty the passport string
			# before emptying process the passport
			# p = ""
			passport_count += 1
			for key in passport:
				# print(key)
				if key in needed_fields:
					valid_fields += 1

			# print(valid_fields)
			if valid_fields >= len(needed_fields):
				valid_passports += 1

			# can now purge the passport
			passport.clear()
			valid_fields = 0
		# print("new line")
		# print("next line would start new a passport")
		else:
			# print("passport line encountered!")
			fields = line.split(" ")

			for field in fields:
				key, value = field.split(":")
				# print("Key: ", key,"Value: ", value)
				passport[key] = value

	return valid_passports, passport_count


input_passports = file.readlines()
file.close()
print("Part 1: ", passport_processor(input_passports))


# print(passport)
# part 2
def check_year(year, minimum, maximum):
	if minimum <= int(year) <= maximum:
		return True
	else:
		return False


def part_two(lines):
	passport = {}
	valid_passports = 0
	valid_fields = 0
	passport_count = 0
	present = False
	validity_of_field = False
	for i in range(len(lines) + 1):
		# blank line is separator for the passports
		# all lines between blank lines are fields for passports
		# extract those lines. then split them into key value pairs
		# check the keys needed. if all keys present then we have a valid passport
		if i < len(lines):
			line = lines[i].strip()
		# print(line, i)
		if len(line.strip()) == 0 or i >= len(lines):
			# passport separator encountered
			# empty the passport string
			# before emptying process the passport
			# p = ""
			passport_count += 1
			# print(passport)
			for key in passport:
				# print(key)
				if key in needed_fields:
					# here add the validation logic for each field
					# 1. check for birth, issue and expiration years
					if key in ["byr", "eyr", "iyr"]:
						if key == "byr":
							validity_of_field = check_year(passport[key], 1920, 2002)
						elif key == "iyr":
							validity_of_field = check_year(passport[key], 2010, 2020)
						elif key == "eyr":
							validity_of_field = check_year(passport[key], 2020, 2030)
					# 2. check for height
					if key == "hgt":
						if "cm" in passport[key]:
							hgt = int(passport[key].replace("cm", ""))
							if 150 <= hgt <= 193:
								validity_of_field = True
						elif "in" in passport[key]:
							hgt = int(passport[key].replace("in", ""))
							if 59 <= hgt <= 76:
								validity_of_field = True
					# 3. check for hair color
					if key == "hcl":
						col = passport[key].replace("#", "")
						if len(col) == 6:
							validity_of_field = True
					# 4. check for eye color
					if key == "ecl":
						# print("eye color ", key, "=", passport[key])
						if passport[key] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
							# print("correct",  passport[key])
							validity_of_field = True
					# 5. check for passport id
					if key == "pid":
						if len(passport[key]) == 9:
							validity_of_field = True

					if validity_of_field:
						valid_fields += 1

				# clearing the value
				validity_of_field = False

			# print(valid_fields)
			if valid_fields >= 7:
				valid_passports += 1

			# can now purge the passport
			passport.clear()
			valid_fields = 0
			validity_of_field = False
		else:
			# print("passport line encountered!")
			fields = line.split(" ")
			for field in fields:
				key, value = field.split(":")
				# print("Key: ", key,"Value: ", value)
				passport[key] = value

	return valid_passports, passport_count


print("Part 2: ", part_two(input_passports))
