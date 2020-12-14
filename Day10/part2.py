from collections import defaultdict


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


def combinations(chargers):
	# possibilities is the array which keeps track of possibilities of combinations from 0 to n
	charger_sort = sorted(chargers)
	charger_sort.append(max_joltage(chargers) + 3)
	charger_sort.insert(0, 0)
	poss = [1] * len(charger_sort)

	for i in range(1, len(charger_sort)):
		poss[i] = poss[i - 1]
		# to check and add the difference of 2 and 3
		if i > 1 and charger_sort[i] - charger_sort[i-2] <= 3:
			poss[i] += poss[i-2]
		if i > 2 and charger_sort[i] - charger_sort[i-3] <= 3:
			poss[i] += poss[i-3]

	return poss[-1]
	# possibilities = defaultdict(int)
	# possibilities[0] = 1
	#
	# for charger in chargers:
	# 	for difference in range(1, 4):
	# 		next_chg = charger + difference
	# 		if next_chg in chargers:
	# 			possibilities[next_chg] += possibilities[chargers]
	#
	# return possibilities[max_joltage(chargers)]


def max_joltage(chargers):
	return max(chargers) + 3


chg = text_processing()
diff_1, diff_2, diff_3 = n_of_adapters(chg)
print(diff_1, diff_2, diff_3)
print("Result: ", diff_1 * diff_3)
print(max_joltage(chg))
print(combinations(chg))
