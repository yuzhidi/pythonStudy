# -*- coding: utf-8 -*
# Print iterations progress
import sys
import time
import datetime

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
def chineseWeek(index) :
    if index == 0:
        return '星期一'
    if index == 1:
        return '星期二'
    if index == 2:
        return '星期三'
    if index == 3:
        return '星期四'
    if index == 4:
        return '星期五'
    if index == 5:
        return '星期六'
    if index == 6:
        return '星期天'


def printProgressBar (index, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    if index <= 0 or iteration <= 0:
        return
    elif iteration < index - 6:
        return
    elif iteration < index:
        sys.stdout.write(RED)
    elif iteration == index:
        #sys.stdout.write(YELLOW)
        sys.stdout.write(GREEN)
    elif iteration < index + 7:
        print('')
        return
    #    sys.stdout.write(GREEN)
    else:
        return

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(' \r%3s / %s %s |%s| %s%% %s' % (iteration, total, prefix, bar, percent, suffix))
    # Print New Line on Complete
    if iteration == total:
        print()

def indexOfTodayInYear() :
    now = datetime.datetime.now()
    #print now.year, now.month, now.day, now.hour, now.minute, now.second
    #p = [31,28,31,30,31,30,31,31,30,31,30,31] # 平年
    #w = [31,29,31,30,31,30,31,31,30,31,30,31] # 闰年

    #year =int(input("请输入年："+'\n'))
    #month =int(input("请输入月："+'\n'))
    #day=int(input("请输入日："+'\n'))
    year = now.year
    month = now.month
    day = now.day

    strX = chineseWeek(now.weekday())
    weekNumber = time.strftime("%W")
    arr=[31,28,31,30,31,30,31,31,30,31,30,31]
    total=365
    sum=day
    for i in range(0,month-1):
        sum+=arr[i]
    if year%4==0:
        if year%100==0 and year%400!=0:
            print ("\n\n\n\n\n                  %s年%s月%s日 %s 这是今年的第%d天 第%s周" % (now.year, now.month, now.day, strX,  sum, weekNumber))
            #print("这是今年的第%d天" % sum)
        else:
            sum=sum+1
            total=total+1
            print ("\n\n\n\n\n                  %s年%s月%s日 %s 这是今年的第%d天 第%s周" % (now.year, now.month, now.day, strX,  sum, weekNumber))
            #print("这是今年的第%d天" % sum)
    else:
        print ("\n\n\n\n\n                %s年%s月%s日 %s 这是今年的第%d天 第%s周" % (now.year, now.month, now.day, strX,  sum, weekNumber))
        #print("这是今年的第%d天" % sum)

    ret = []
    ret.append(total)
    ret.append(sum)
    return ret
#
# Sample Usage
#

#from time import sleep

print ""
yearDays,indexOfYear = indexOfTodayInYear()
#print yearDays
#print indexOfYear
# A List of Items
items = list(range(0, int(yearDays)))
l = len(items)

# Initial call to print 0% progress
printProgressBar(indexOfTodayInYear,0, l, prefix = ':', suffix = '', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    #sleep(0.1)
    # Update Progress Bar
    printProgressBar(indexOfYear, i + 1, l, prefix = ':', suffix = '', length = 50)


print ""
