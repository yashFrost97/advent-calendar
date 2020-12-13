def text_processing():
	file = open("input.txt", "r")
	lines = file.read().splitlines()
	file.close()

	code = []

	for line in lines:
		op, value = line.split(" ")
		if '+' in value:
			# positive number
			value = int(value[1:])
		else:
			# negative
			value = int(value[1:]) * -1

		# code tuple.
		code_tuple = [op, value]
		code.append(code_tuple)

	return code


def command(cmd):
	# return index change and accumulator change
	if cmd[0] == "acc":
		return 1, cmd[1]
	if cmd[0] == "nop":
		return 1, 0
	if cmd[0] == "jmp":
		return cmd[1], 0


def loop_check(code):
	acc = 0
	i = 0
	index_tracker = []
	index_tracker.append(i)
	i_change, acc_change = command(code[i])
	i += i_change
	acc += acc_change


	while True:
		# evaluate first cmd
		if i in index_tracker:
			print(i, i_change)
			print(acc)
			return False
		else:
			try:
				index_tracker.append(i)
				i_change, acc_change = command(code[i])
				i += i_change
				acc += acc_change
			except:
				print("out of index")
				return False


def brute_force(code):
	no_loop = False
	for i in range(len(code)):
		if code[i][0] == "jmp":
			temp = "jmp"
			code[i][0] = "nop"
			no_loop = loop_check(code)

			if no_loop:
				print("done!")
				return code
			else:
				code[i][0] = temp
		if code[i][0] == "nop":
			temp = "nop"
			code[i][0] = "jmp"
			no_loop = loop_check(code)
			if no_loop:
				print("done!")
				return code
			else:
				code[i][0] = temp



def final_acc(final_code):
	acc = 0
	i = 0
	# eval first command
	i_change, acc_change = command(final_code[i])
	i += i_change
	acc += acc_change

	while i < len(final_code):
		i_change, acc_change = command(final_code[i])
		i += i_change
		acc += acc_change

	return acc


code = text_processing()
test = brute_force(code)
print(test)



