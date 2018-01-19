
#!/usr/bin/python

import getopt
import sys


def usage():
    print ' -h help \n' \
          ' -i ip address\n' \
          ' -p port number\n' \
          ''

def handleOpt():
    try:
        options, args = getopt.getopt(sys.argv[1:], "hp:i:", ['help', "ip=", "port="])
         for name, value in options:
            if name in ('-h', '--help'):
                usage()
            elif name in ('-i', '--ip'):
                print value
            elif name in ('-p', '--port'):
                print value
    except getopt.GetoptError:
        usage()

if __name__ == '__main__':
	handleOpt()
