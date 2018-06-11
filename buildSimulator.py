#!/usr/bin/env python
#---*coding=utf-8*---

from subprocess import Popen, PIPE
from sys import argv
import os
import sys
import subprocess
import re

def runCmd(cmd):
    ps = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    outputLines = ps.stdout.readlines()
    return outputLines

def getSimulatorInfo():
    cmd = "instruments -s devices"
    outputLines = runCmd(cmd)
    outputLines.reverse()
    for line in outputLines:
        print line
    # pattern accept:
    # iphone x (11.2) [76bb8e2c-eb3f-4fa3-a52f-728f80a57929] (simulator)
    # pattern omit:
    # "iPad Pro (12.9-inch) (2nd generation) (11.2) [30631354-0FFB-4F70-8B38-4C2CC2131A10] (Simulator)"

        pattern = re.compile("^([A-Za-z0-9\\s\\-]+) \(([^)]+)\) \[.+\] \(Simulator\)")
        matcher = re.search(pattern, line)
        if (matcher):
            simulatorName = matcher.group(1)
            simulatorOS = matcher.group(2)
            return [simulatorName, simulatorOS]


simulatorName, simulatorOS = getSimulatorInfo()

script,runnerPath = argv

cmd = "xcodebuild -project %s -scheme TestRunner -destination 'platform=iOS Simulator,name=%s,OS=%s' build-for-testing"%(runnerPath, simulatorName, simulatorOS)
print cmd
lines = runCmd(cmd)
for line in lines:
    print line
