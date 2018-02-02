import sys

def sum(a, b):
	sum = 0
	for i in range(a, b+1):
		if (i % 2 == 1):
			sum += i
	return sum

print(sum(int(sys.argv[1]), int(sys.argv[2])))