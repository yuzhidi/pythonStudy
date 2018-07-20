#!/usr/bin/env python
#---*coding=utf-8*---

from subprocess import Popen, PIPE
import os
import sys
import subprocess
import re

def run_command(args):
	# if type(args)==str:
	# 	args = args.split()

    ps = Popen(args, shell=True, stdout=PIPE, stderr=PIPE)
    outputLines = ps.stdout.readlines()
    print outputLines

def matchIphone(str):
	print "matchIphone>>>>>>>>>"
	pattern = re.compile("^([A-Za-z0-9\\s\\-]+) \(([^)]+)\) \[.+\]")
	pattern = re.compile("^([A-Za-z0-9\\s\\-]+) \(([^)]+)\) \[.+\] \(Simulator\)")
	matcher = re.search(pattern, str)

	if matcher:
		print matcher.group(1)
		print matcher.group(2)
	print "matchIphone<<<<<<<<"

src0 = "iPhone X (11.2) [76BB8E2C-EB3F-4FA3-A52F-728F80A57929] (Simulator)"
src1 = "iPhone SE (11.2) [1ABCDB74-F69C-4B29-940E-03201C8C875A] (Simulator)"
src11= "iPhone 7 (11.2) [703BF214-113A-4265-9B3F-39EFAC425C58] (Simulator)"
src2 = "iPhone 7 Plus (11.2) + Apple Watch Series 2 - 42mm (4.2) [C5467490-F237-4E30-B959-03571B1E9CA7] (Simulator)"
src3 = "iPad Pro (12.9-inch) (2nd generation) (11.2) [30631354-0FFB-4F70-8B38-4C2CC2131A10] (Simulator)"
src4 = "iPhoneSE_ios11.0 (11.0) [954722bb10d4106050f0b5db77e9f9b2c1f45619]"
matchIphone(src0)
matchIphone(src1)
matchIphone(src11)
matchIphone(src2)
matchIphone(src3)
matchIphone(src4)


text="(content:\"rcpt to root\";pcre:\"word\";)"
rule1="content:\".+\""
rule2="content:\".+?\""
pattern = re.compile(rule2)
matcher = re.search(pattern, text)
if matcher:
		print matcher.group(0)

patternDjangoDocker = re.compile("([a-zA-Z0-9]+)\s+hub.testbird.com/django");
djangoPsline = '3247ef1bdab5        hub.testbird.com/django/quail:baseimage-1567   "/django-entrypoint.s"   25 hours ago        Up 25 hours         80/tcp, 443/tcp                                                                   docker_mobiletest.gf.com.cn_1'

print 'test django ps line'
matcher = re.search(patternDjangoDocker, djangoPsline)
if matcher:
	print matcher.group(0)
	print matcher.group(1)

# run_command("xcodebuild -project /Users/wangliang/work/TBiOSRunner/TBRunner/TBRunner.xcodeproj -scheme TestRunner -destination 'platform=iOS Simulator,name=iPhone X,OS=11.2' build-for-testing")
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
print identifier("xcodebuild -project /Users/wangliang/work/TBiOSRunner/TBRunner/TBRunner.xcodeproj -scheme TestRunner -destination 'platform=iOS Simulator,name=iPhone X,OS=11.2' build-for-testing")


