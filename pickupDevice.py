
import re

device  = "ae9f2d10aac64ca39f7e161e75c670e3 device usb:5-1.3"
deviceAll = "f2d588                 device usb:337641472X product:cancro model:MI_3C device:cancro"
dockerPs = "49aafa03c592        hub.testbird.com/tbstf/adb:v0.1.10             \"/bin/sh -c 'adb -a -\"   7 days ago          Up 7 days                               r-stf-adb-3-a67da6a0"

pattern1 = re.compile("(\S+)\s+device usb")
patternInfo = re.compile("product:(.*)\smodel:(.*)\sdevice:(.*)")
patternDockerPsAdb = re.compile("(r-stf-adb.*)");

m = re.search(pattern1, device)
if m:
	print m.group(0,1)
m = re.match(pattern1, "sdfsdf")
if m:
	print "not ok"
m = re.search(pattern1, deviceAll)
if m:
	print m.group(0,1)
m = re.search(patternInfo, deviceAll)
if m:
	print m.group(0,1,2,3)

m = re.search(patternDockerPsAdb, dockerPs)
if m:
	print m.group(0,1)
