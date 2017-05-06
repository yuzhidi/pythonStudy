import os.path

def funcA(a):
	print 'funcA' + a
	if os.path.exists("/tmp"):
		print "/tmp exists"
	if not os.path.exists("/tmp"):
		print "not exists"
	else:
		print "test else"

def funcB():
	print 'funcB'
	funcA('hello')

if __name__ == '__main__':
    funcB()
