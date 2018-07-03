from array import array

def notArrayReturn() :
	print "notArrayReturn"
#	return ["a", "b"]
# 'd' not reverse()
a = array('d', [1.0, 2.0, 3.14])
a.reverse()
print a
a = ['a','b']
a.reverse()
print a
for s in a:
	print s
innerString=""
for s in ['c', 'ddd']:
	innerString += ': ' + s
	print s
print "innerString:"+innerString

# [no0, no1] = notArrayReturn()
# print "%s,%s"%(no0, no1)
def funcA():
	innerString2='b'
	return "funcA"
def printA(data):
	print data

printA(funcA())

# print "innerString2:" + innerString2

testNotFound= ['a', 'b', 'file not found']
if 'file not found' in testNotFound:
	print 'fine not found'

print 'test print last' + testNotFound[-1]

# testNotFound= ['a', 'b', 'file not found', 2]
# if 'file not found' in testNotFound:
# 	print 'fine not found'

# print 'test print last' + testNotFound[-1]