def text_processing():
	file = open("input.txt", "r")
	lines = file.read().split()
	file.close()
	temp = [int(i) for i in lines]
	return temp


def n_of_adapters(chargers):
	charger_sort = sorted(chargers)
	joltage = 0
	# print(charger_sort)
	cnt1, cnt2, cnt3 = 0, 0, 0
	while charger_sort:
		# print("current joltage: ", joltage)
		# print("Joltage considered here: ", joltage + 1, joltage + 2, joltage + 3)
		# print("current list: ", charger_sort)
		if joltage + 1 in charger_sort:
			joltage = joltage + 1
			# print("found ", joltage)
			charger_sort.remove(joltage)
			cnt1 += 1
		elif joltage + 2 in charger_sort:
			joltage = joltage + 2
			# print("found ", joltage)
			charger_sort.remove(joltage)
			cnt2 += 1
		elif joltage + 3 in charger_sort:
			joltage = joltage + 3
			# print("found ", joltage)
			charger_sort.remove(joltage)
			cnt3 += 1
		# print("*****************************")

	# adding device built-in adapter of 3 joltage
	cnt3 += 1
	# print(charger_sort)
	return cnt1, cnt2, cnt3


chg = text_processing()
diff_1, diff_2, diff_3 = n_of_adapters(chg)
print(diff_1, diff_2, diff_3)
print("Result: ", diff_1 * diff_3)