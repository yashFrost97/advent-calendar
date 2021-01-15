import math
from itertools import count
from functools import reduce
from operator import itemgetter, mul

file = open("input.txt", "r")
time = int(file.readline())
input_bus = file.readline().strip().split(",")
file.close()

buses = []

for i, v in filter(lambda iv: iv[1]!= 'x', enumerate(input_bus)):
	buses.append((-i, int(v)))

# def lcm(a, b):
# 	return a * b // math.gcd(a, b)

# t, step = buses[0]
# for delta, period in buses[1:]:
# 	for t in count(t, step):
# 		if (t + delta) % period == 0:
# 			break
	
# 	step = lcm(step, period)

# print("part 2: ", t)

def egcd(a, b):
	if a == 0:
		return(b, 0, 1)
	g, y, x = egcd(b % a, a)
	return(g, x - (b // a) * y, y)

def modinv(a, b):
	g, inv, y = egcd(a, b)
	assert g == 1 
	return inv % b

def chinese_remainder_theorem(equations):
	x = 0
	P = reduce(mul, map(itemgetter(1), equations))

	for ai, pi in equations:
		ni = P // pi
		inv = modinv(ni, pi)
		x = (x + ai * ni * inv) % P

	return x

print("Soln: ", chinese_remainder_theorem(buses))