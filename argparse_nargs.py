import argparse

# http://blog.xiayf.cn/2013/03/30/argparse/

parser = argparse.ArgumentParser()

parser.add_argument('--three', nargs=3)
parser.add_argument('--optional', nargs='?')
parser.add_argument('--all', nargs='*', dest='all')
parser.add_argument('--one-or-more', nargs='+')

result = parser.parse_args()

print result

if result.three:	
	print result.three

if result.optional:
	print result.optional

if result.all:
	print result.all

if result.one_or_more:
	print result.one_or_more