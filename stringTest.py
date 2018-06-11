#!/usr/bin/python

if __name__ == '__main__':
	str1 = 'ab c\n\nde fg\rkl\r\n'
	print isinstance(str1, str)
	print str1.splitlines();

	str2 = 'ab c\n\nde fg\rkl\r\n'
	print str2.splitlines(True)