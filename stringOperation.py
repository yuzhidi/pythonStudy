import re

DOCKER_BIN = "/usr/local/bin/docker";
ONLINE_LOG = "20170427 17:00:41.884 INFO     - change sn:TESTBIRD_HC4AVYC01829_12479 to uuid f09e639d-b4ab-4e12-910d-694d9abe8b3c";
ONLINE_SU8_STRING = "to uuid f09e639d-b4ab-4e12-910d-694d9abe8b3c";

print ONLINE_LOG.find(ONLINE_SU8_STRING)

print ONLINE_LOG.find("adfaf1111111111111")


print ONLINE_LOG.find("201704")
if ONLINE_LOG.find("adfaf1111111111111") > 0:
	print "1111111111"
else:
	print 'not found adfaf1111111111111'
print ONLINE_LOG.split(' ')
data = ONLINE_SU8_STRING.split(' ')
a,b,c = data
print a + b + c 


patternTime = re.compile("(\S+?)\s(.*?)\s") 

m = re.search(patternTime, ONLINE_LOG)
if m:
	print "found"
	print m.group(1) + " , " + m.group(2)
	if m.group(1) == "20170427":
		print "equal"

if 3 > 5 or 4 > 1:
	print "4>1"