import argparse

# http://blog.xiayf.cn/2013/03/30/argparse/


parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="count", type=int)

result = parser.parse_args(['-a', '-bval', '-c', '3'])
print result
#
print result.b
print result.count

result = parser.parse_args(['-bval'])
print result

if result.a or result.b or result.count:
	print "or:" + str(result)

result = parser.parse_args()
print result

if result.a or result.b or result.count:
	print "or2:" + str(result)