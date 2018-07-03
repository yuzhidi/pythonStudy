#!/usr/bin/python
import os
if __name__ == '__main__':
	str1 = 'ab c\n\nde fg\rkl\r\n'
	print isinstance(str1, str)
	print str1.splitlines();

	str2 = 'ab c\n\nde fg\rkl\r\n'
	print str2.splitlines(True)

	strEndSep = 'abc/efg/'
	print 'src'+strEndSep
	print "-1:"+strEndSep[-1]
	print "-2:"+strEndSep[-2]
	print "-6:"+strEndSep[-6]
	print "-7:"+strEndSep[-7]

	print '0:-1 is ' + strEndSep[0:-1]

	print os.getcwd()

	strOne ="/"
	print "strOne:" + strOne[-1]

	global gWorkingDir
	gWorkingDir = ''
	print 'gWorkingDir'+gWorkingDir
	if gWorkingDir:
		print 'if:'+gWorkingDir

	gWorkingDir = 'a'
	print 'gWorkingDir'+gWorkingDir
	if gWorkingDir:
		print 'if:'+gWorkingDir

	gWorkingDir = None
	print 'gWorkingDir:'+str(gWorkingDir)
	if gWorkingDir:
		print 'if:'+gWorkingDir