
# coding=utf-8
'''
Created on 2013年11月22日
 
@author: crazyant.net
'''
import commands
import pprint
 
def cmd_exe(cmd_String):
    print "will exe cmd,cmd:"+cmd_String
    return commands.getstatusoutput(cmd_String)
 
if __name__=="__main__":
    #pprint.pprint(cmd_exe("ls -la"))
    print (cmd_exe("ls -la"))