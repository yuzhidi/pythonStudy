fileHandle = open ( '/tmp/pythonFileOpTest.txt', 'w' ) 
fileHandle.write ( 'This is a test.\nReally, it is.\r\n' ) 
fileHandle.close() 

with open('/tmp/pythonFileOpTest.txt') as fp:
    for line in iter(fp.readline, ''):
    	print line

    	with open('/tmp/pythonFileOpTest.txt') as fp:
    		for line in iter(fp.readline, ''):
    			print line
