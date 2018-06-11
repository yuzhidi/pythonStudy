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

[no0, no1] = notArrayReturn()
print "%s,%s"%(no0, no1)