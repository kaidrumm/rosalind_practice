def hypotenuse(a, b):
	return math.sqrt(a * a + b * b)

def slice(string, a, b, c, d):
	print(a.__class__.__name__)
	return string[a:b+1] + " " + string[c:d+1]

string = input("Please enter the string: ")
a = int(input("Index A: "))
b = int(input("Index B: "))
c = int(input("Index C: "))
d = int(input("Index D: "))

print(slice(string, a, b, c, d))