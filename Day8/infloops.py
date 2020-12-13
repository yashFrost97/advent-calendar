def command(cmd):
	# return index change and accumulator change
	if cmd[0] == "acc":
		return 1, cmd[1]
	if cmd[0] == "nop":
		return 1, 0
	if cmd[0] == "jmp":
		return cmd[1], 0


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
		print(acc)
		break
	else:
		index_tracker.append(i)
		i_change, acc_change = command(code[i])
		i += i_change
		acc += acc_change
