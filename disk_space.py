#!/usr/bin/env python
#coding=utf-8
from subprocess import Popen, PIPE
import re
def disk_space(pattern="2[0-9]%", message="CAPACITY WARNING"):
    ## take shell command output
    ps = Popen("df -h", shell=True, stdout=PIPE, stderr=PIPE)
    output_lines = ps.stdout.readlines()
    print '------'
    print len(output_lines)
    i = 0
    for line in output_lines:
    	print '------'
    	print str(i) + "," +line
    	i += 1
        line = line.strip()
        print line
        if re.search(pattern, line):
            print "%s %s" %(message, line)
            
if __name__ == '__main__':
    disk_space()