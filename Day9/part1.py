def text_processing():
	file = open("input.txt", "r")
	lines = file.read().split()
	file.close()
	temp = [int(i) for i in lines]
	return temp


def sliding_window(input, window):
	preamble = []
	for i in range(window, len(input)):
		print("loop ", i, "*"*5)
		total = input[i]
		preamble.clear()
		valid = False
		for j in range(i-window, i):
			preamble.append(input[j])

		for index1 in range(len(preamble) - 1):
			for index2 in range(index1 + 1, len(preamble)):
				temp = preamble[index1] + preamble[index2]
				if temp == total:
					valid = True

		if not valid:
			print(preamble)
			print("position ", i)
			print("wrong number, ", total)
			break



inp = text_processing()
# print(len(inp))
sliding_window(inp, 25)
