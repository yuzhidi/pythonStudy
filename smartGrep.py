# -*- coding: utf-8 -*

#
# Copyright © 2018. TestBird. All rights reserved.
#

import argparse

toMatch = 0
braceMatched = 0
leftBrace = 0
rightBrace = 0

def checkBrace(line):
	global toMatch
	global braceMatched
	global leftBrace
	global rightBrace
	leftBrace = leftBrace + line.count('{')
	rightBrace = rightBrace + line.count('}')
	# print 'leftBrace:' + str(leftBrace)
	# print 'rightBrace:' + str(rightBrace)
	if leftBrace and leftBrace == rightBrace:
		# print '+++++++++++++++++++++++++++1 :' + str(leftBrace)
		braceMatched = braceMatched + 1

	if rightBrace and toMatch == braceMatched:
		# print '****************************reset :'
		# print toMatch
		# print braceMatched
		toMatch = 0
		braceMatched = 0
		leftBrace = 0
		rightBrace = 0

	# print 'checkEnd ' + str(toMatch)

def doGrep():
	global toMatch
	global braceMatched
	global leftBrace
	global rightBrace

	with open(gArgs.src) as fp:
		for line in fp.readlines():
			if toMatch:
				print line.strip()
				checkBrace(line)

			if gArgs.WDACommunication and 'WDACommunication' in line:
				print line
				if 'responseJson' in line  or 'doPost' in line or 'getAlertInfo' in line:
					# print '>>>>>>>>>>>>>> toMatch=1'
					toMatch = 1
					checkBrace(line)
			elif gArgs.keywords:
				for keyword in gArgs.keywords:
					if keyword in line:
						print line

def addKeywords(keyword):
	if not gArgs.keywords:
		gArgs.keywords = []

	gArgs.keywords.append(keyword)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--src', help='source file')
    parser.add_argument('--WDACommunication', action="store_true", default=False, help='grep WDACommunication')
    parser.add_argument('--sendExecutionStatus', action="store_true", default=False, help='grep sendExecutionStatus')
    parser.add_argument('--roc', action="store_true", default=False, help='enable --WDACommunication')
    parser.add_argument('--dst', help='save result to file')
    parser.add_argument('--keywords', nargs='+', help='grep keyword')
    parser.add_argument('--checkBraceWords')


    global gArgs
    gArgs = parser.parse_args()

    if gArgs.roc:
		gArgs.WDACommunication = True
		gArgs.sendExecutionStatus = True

    if gArgs.sendExecutionStatus:
        addKeywords('sendExecutionStatus')

    doGrep()
