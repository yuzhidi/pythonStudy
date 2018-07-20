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

print 'https://www.tutorialspoint.com/python/string_translate.htm ----------->'
from string import maketrans

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab)

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
str = str.replace(' ', '_')

print str.translate(trantab, 'xm')

cmd = "xcodebuild -project /Users/wangliang/work/TBiOSRunner/TBRunner/TBRunner.xcodeproj -scheme TestRunner -destination 'platform=iOS Simulator,name=iPhone X,OS=11.2' build-for-testing"
intab = ' \\/\'\",'
outtab = '______'
trantab = maketrans(intab, outtab)
print cmd.translate(trantab)


print 'makefilter------------------------'
def makefilter(keep):
    """ Return a functor that takes a string and returns a copy of that
        string consisting of only the characters in 'keep'.
    """
    import string

    # make a string of all chars, and one of all those NOT in 'keep'
    allchars = string.maketrans('', '')
    delchars = ''.join([c for c in allchars if c not in keep])

    # return the functor
    return lambda s,a=allchars,d=delchars: s.translate(a, d)

import string
identifier = makefilter(string.letters + string.digits + '_')

print identifier
print string.maketrans('','')
cmd = "xcodebuild -project /Users/wangliang/work/TBiOSRunner/TBRunner/TBRunner.xcodeproj -scheme TestRunner -destination 'platform=iOS Simulator,name=iPhone X,OS=11.2' build-for-testing"

print identifier(cmd)

print cmd.split(' ')[0]
print os.path.basename(cmd.split(' ')[0])

cmd = '/usr/local/bin/xcodebuild -project'
print os.path.basename(cmd)

url = 'http://quail.lab.tb/api/task/execution/mYMkKX/'
url = 'http://quail.lab.tb/home/executionDetail/YzlqpX/true'
cmdItems = url.split('/')
print cmdItems
found = None
for cmdItem in cmdItems:
	print cmdItem
	if found:
		print 'found :' + cmdItem
	if 'execution' in cmdItem:
		found = True

print '>>>>>>>>>>>>> by index'
print cmdItems[1]

print "--------------------------------- sub string ---------------------------------------------"
runLogUrl = "http://file.lab.tb/upload/1531703952519_40b446f0_full.zip?download"
runLogUrl = "http://file.lab.tb/upload/1531703952519_40b446f0_full.zip?download"

if runLogUrl.endswith('full.zip?download'):
    delta = 0 - len('?download')
else:
    delta = len(runLogUrl)
    

print runLogUrl[:delta]
