def text_processing():
	file = open("input.txt", "r")
	lines = file.read().split()
	file.close()
	temp = [int(i) for i in lines]
	return temp


def sliding_window(input, window):
	preamble = []
	for i in range(window, len(input)):
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
			return i, total
			break


def contiguous(input, position, wrong):
	for size in range(2, len(input[:position - 1])):
		window = input[size:]
		i = 1
		while i < len(input[:position]) - size:
			if sum(window) == wrong:
				return window
			i += 1
			window = input[i:size + i]


inp = text_processing()
# print(len(inp))
position, wrong_number = sliding_window(inp, 25)
wind = contiguous(inp, position, wrong_number)

ma = max(wind)
mi = min(wind)

print(ma + mi)

