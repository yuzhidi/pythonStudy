#!/usr/bin/env python
from subprocess import Popen, PIPE
import sys, os
import subprocess
import time
import re

patternLsUsb = re.compile("ID (.*):(.{4})")

testData = '''
Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 011: ID 04e8:6860 Samsung Electronics Co., Ltd Galaxy (MTP)
Bus 001 Device 010: ID 2717:ff68
Bus 001 Device 008: ID 05c6:9039 Qualcomm, Inc.
Bus 001 Device 007: ID 1a40:0101 Terminus Technology Inc. Hub
Bus 001 Device 006: ID 0fce:51c2 Sony Ericsson Mobile Communications AB
Bus 001 Device 005: ID 1a40:0101 Terminus Technology Inc. Hub
Bus 001 Device 019: ID 05c6:9039 Qualcomm, Inc.
Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 009: ID 2717:ff68
Bus 003 Device 008: ID 2717:0368
Bus 003 Device 007: ID 109b:911f Hisense
Bus 003 Device 006: ID 2717:ff48
Bus 003 Device 005: ID 1a40:0101 Terminus Technology Inc. Hub
Bus 003 Device 014: ID 0bb4:05ec HTC (High Tech Computer Corp.)
Bus 003 Device 003: ID 1a40:0101 Terminus Technology Inc. Hub
Bus 003 Device 015: ID 05c6:9039 Qualcomm, Inc.
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 012 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 011 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 009 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 010 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 008 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 007 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
'''
def ps():
		cmd = "ps";
		ps = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		output_lines = ps.stdout.readlines()
		for line in output_lines:
			print line

def lsusb():
		cmd = "lsusb";
		ps = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		output_lines = ps.stdout.readlines()
		for line in output_lines:
			print line
		return output_lines

def testPattern(data):
	content = ""
	if data == testData:
		data = data.split("\n")
	for line in data:
		print line
		# not add as Bus 010 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
		if (line.endswith('Linux Foundation 2.0 root hub') or line.endswith('Linux Foundation 3.0 root hub')
		    or line.endswith('Linux Foundation 3.0 root hub\n') or line.endswith('Linux Foundation 2.0 root hub\n')):
			continue
		m = re.search(patternLsUsb, line)
		if m:
			print "Matching"
			print m.group(1)
			print m.group(2)
			rule='SUBSYSTEM=="usb",ATTRS{idVendor}=="%s",ATTRS{idProduct}=="%s", MODE="0666"\n' % (m.group(1), m.group(2))
			content += rule
	#return content
	f = open('/tmp/tb-android.rules', 'w')
	f.write(content)	
	f.close()

def moveTBrules():
		print "maybe you will enter password"
		cmd = "sudo cp /tmp/tb-android.rules /etc/udev/rules.d/tb-android.rules";
		ps = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		output_lines = ps.stdout.readlines()
		for line in output_lines:
			print line

def printComingAction():
	print "you should do: sudo service udev restart"
	print "if not success do: sudo restart udev"
	print "then do: adb kill-server; adb start-server"
	print "plug off then plug in devices"

if __name__ == '__main__':

	# here debug
	isTestData = False
	if isTestData:
		testPattern(testData)
	else:
		lsusbData = lsusb()
		print lsusbData
		testPattern(lsusbData)
		moveTBrules()
		printComingAction()
