def funcA(a):
	print 'funcA' + a

def funcB():
	print 'funcB'
	funcA('hello')

if __name__ == '__main__':
    funcB()
