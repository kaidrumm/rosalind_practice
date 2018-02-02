import sys

summary = {}
for word in sys.argv[1].split():
	if word in summary:
		summary[word] += 1
	else:
		summary[word] = 1

for key, value in summary.items():
	print(key, value)