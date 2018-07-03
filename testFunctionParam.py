def test(a, b, c):
	print a
	print b
	if c:
		print c
	pass

def test(a, b):
	test(a, b, None)

test(1,2)
test(4,5,6)