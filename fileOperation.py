fileHandle = open ( '/tmp/pythonFileOpTest.txt', 'w' ) 
fileHandle.write ( 'This is a test.\nReally, it is.\r\n' ) 
fileHandle.close() 

# with open('/Users/wangliang/Study/HotPot/tbRemote.py') as fp:
#     for line in iter(fp.readline, ''):
#     	print line


print '>>>>>>>>>>>>>>>>>>>> no iter'
fileHandle = open ( '/tmp/pythonFileOpTest.txt', 'w' )
toMatch = 0
braceMatched = 0
leftBrace = 0
rightBrace = 0

def checkBrace(line):
	global toMatch
	global braceMatched
	global leftBrace
	global rightBrace
	leftBrace = leftBrace + line.count('{')
	rightBrace = rightBrace + line.count('}')
	print 'leftBrace:' + str(leftBrace)
	print 'rightBrace:' + str(rightBrace)
	if leftBrace and leftBrace == rightBrace:
		print '+++++++++++++++++++++++++++1 :' + str(leftBrace)
		braceMatched = braceMatched + 1

	if rightBrace and toMatch == braceMatched:
		print '****************************reset :'
		print toMatch
		print braceMatched
		toMatch = 0
		braceMatched = 0
		leftBrace = 0
		rightBrace = 0

	print 'checkEnd ' + str(toMatch)

with open('/Users/wangliang/Study/HotPot/3318bf0a912a460cb1f372a5d21ac126/roc/roc.log.20180723090320.aaag-keyword-3318bf0a912a460cb1f372a5d21ac126-udid-e3c78110ca75220f0a7ce2c8a9b66a2a86564759') as fp:
	for line in fp.readlines():
		if toMatch:
			print line
			fileHandle.write(line)
			checkBrace(line)


		if 'WDACommunication' in line:
			print line
			fileHandle.write (line) 
			if 'responseJson' in line  or 'doPost' in line or 'getAlertInfo' in line:
				print '>>>>>>>>>>>>>> toMatch=1'
				toMatch = 1
				checkBrace(line)


fileHandle.close()
