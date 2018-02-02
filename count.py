f = open('input.txt', 'r')

a = 0
c = 0
g = 0
t = 0

for line in f:
	i = 0
	for char in line:
		if char == "A":
			a +=1
		elif char == "C":
			c +=1
		elif char == "G":
			g += 1
		elif char == "T":
			t += 1
		else:
			print("Error, invalid nucleotide")

print(a, c, g, t)