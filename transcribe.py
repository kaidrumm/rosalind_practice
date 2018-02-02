f = open('input.txt', 'r')

def replace(c):
	if c == 'T':
		return 'U'
	else:
		return c

for line in f:
	line = "".join(map(replace, line))

print(line)