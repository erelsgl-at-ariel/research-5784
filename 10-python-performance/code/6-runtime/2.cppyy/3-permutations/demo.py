import itertools

print("Permutations of range:")
for p in itertools.permutations(range(1,5)):
	print(p)

print("Permutations of string:")
for p in itertools.permutations("abcd"):
	print("".join(p))

