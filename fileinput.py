f = open('input.txt', 'r')
g = open('output.txt', 'w')

i = 0
for line in f:
	i += 1
	if(i%2 == 0):
		g.write(line)