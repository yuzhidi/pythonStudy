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
    repeatCount = 0
    fo = open(logFile)

    setRS = set()
    setLS = set()
    lines = fo.readlines()
    for line in lines:
        m = re.search(patternRS, line)
        if m:
            # print line
            # print m.group(1)
            if m.group(2) == "created":
                # print "created"
                if m.group(1) in setRS:
                    print "error: %s has created" % (m.group(1))
                    repeatCount += 1
                else:
                    setRS.add(m.group(1))
            elif m.group(2) == "closed":
                # print "closed"
                if m.group(1) not in setRS:
                    print "error: %s has closed" % (m.group(1))
                else:
                    setRS.remove(m.group(1))
        else:
            m = re.search(patternLS, line)
            if m:
                # print line
                # print m.group(1)
                if m.group(2) == "created":
                    # print "created"
                    if m.group(1) in setLS:
                        print "error: %s has created" % (m.group(1))
                    else:
                        setLS.add(m.group(1))
                elif m.group(2) == "closed":
                    # print "closed"
                    if m.group(1) not in setLS:
                        print "error: %s has closed" % (m.group(1))
                    else:
                        setLS.remove(m.group(1))
    fo.close();
    print "Remote socket :"
    print setRS
    print "Local socket :"
    print setLS
    print "RS: %d + LS: %d = %d" % (len(setRS), len(setLS), int(len(setRS) + len(setLS)))
    print "repeatCount RS:%d" % (repeatCount)
    isFirst = True

    grepLSCmd = "grep -nE \""
    for localSocket in setLS:
        if isFirst:
            isFirst = False
            grepLSCmd += "LS\(%s\)" % (localSocket)
        else:
            grepLSCmd += "|LS\(%s\)" % (localSocket)
    grepLSCmd += "\" " + logFile
    # print grepLSCmd
    grepScriptFilePath = "/tmp/grepLSCmd.sh"
    grepScript = open(grepScriptFilePath, "w")
    grepScript.write(grepLSCmd)
    grepScript.close()
    print "cp %s ." % (grepScriptFilePath)


def usage():
    print 'usage:\n' \
          ' -f log file \n' \
          ' -i ip address\n' \
          ' -p port number\n' \
          ''

def handleOpt():
    try:
        options, args = getopt.getopt(sys.argv[1:], "f:g:p:", ['file=', "grep=", "port="])
        # print args
        if len(options) == 0:
            usage()
            exit(1)

        for name, value in options:
            if name in ('-f', '--file'):
                global logFile
                logFile = value
            elif name in ('-g', '--grep'):
                print value

            elif name in ('-p', '--port'):
                print value
    except getopt.GetoptError:
        usage()

if __name__ == '__main__':
    handleOpt()
    statistical()