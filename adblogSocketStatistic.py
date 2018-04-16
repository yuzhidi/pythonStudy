#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from subprocess import Popen, PIPE
import sys, os, getopt
import subprocess
import time
import re

patternRS = re.compile("- RS\((\\d+)\\): (created|closed)")
patternLS = re.compile("- LS\((\\d+)\\): (created|closed)")

def statistical():
    fo = open(logFile)

    setRS = set()
    setLS = set()
    lines = fo.readlines()
    for line in lines:
        m = re.search(patternRS, line)
        if m:
            print line
            print m.group(1)
            if m.group(2) == "created":
                print "created"
                if m.group(1) in setRS:
                    print "error: %s has created" % (m.group(1))
                else:
                    setRS.add(m.group(1))
            elif m.group(2) == "closed":
                print "closed"
                if m.group(1) not in setRS:
                    print "error: %s has closed" % (m.group(1))
                else:
                    setRS.remove(m.group(1))
        else:
            m = re.search(patternLS, line)
            if m:
                print line
                print m.group(1)
                if m.group(2) == "created":
                    print "created"
                    if m.group(1) in setLS:
                        print "error: %s has created" % (m.group(1))
                    else:
                        setLS.add(m.group(1))
                elif m.group(2) == "closed":
                    print "closed"
                    if m.group(1) not in setLS:
                        print "error: %s has closed" % (m.group(1))
                    else:
                        setLS.remove(m.group(1))
    print setRS
    print setLS

def usage():
    print ' -f log file \n' \
          ' -i ip address\n' \
          ' -p port number\n' \
          ''

def handleOpt():
    try:
        options, args = getopt.getopt(sys.argv[1:], "f:i:p:", ['file=', "ip=", "port="])
        for name, value in options:
            if name in ('-f', '--file'):
                global logFile
                logFile = value
            elif name in ('-i', '--ip'):
                print value
            elif name in ('-p', '--port'):
                print value
    except getopt.GetoptError:
        usage()

if __name__ == '__main__':
    handleOpt()
    statistical()