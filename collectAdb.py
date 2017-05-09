#!/usr/bin/python
# coding=utf-8
'''

Created on 2017-5-6

@author: Leo
'''
from subprocess import Popen, PIPE
import shlex
import os.path
import datetime
import subprocess
import time
import re
import socket

'''
20170427 17:00:41.884 INFO	  - change sn:TESTBIRD_HC4AVYC01829_12479 to uuid f09e639d-b4ab-4e12-910d-694d9abe8b3c
20170430 17:02:01.604 INFO	  - transport: f09e639d-b4ab-4e12-910d-694d9abe8b3c removed
'''
patternLogTime = re.compile("(\S+?)\s(.*?)\s")
patternDeviceName = re.compile("(\S+)\s+device usb");
patternDeviceInfo = re.compile("product:(.*)\smodel:(.*)\sdevice:(.*)");
patternDockerPsAdb = re.compile(".*(r-stf-adb.*)");
RIO_ADB_LOG_TMP_FILE = "/tmp/rio.adb.log"
ADB_DEVICES_TMP_FILE = "/tmp/adbdevices"
DOCKER_BIN = "/usr/bin/docker"

def getReportFileName():
	return "/tmp/deviceAdbReport_" + socket.gethostname() + "_" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".csv" 

def execute_command(cmdstring, cwd=None, timeout=None, shell=False):
	"""执行一个SHELL命令
			封装了subprocess的Popen方法, 支持超时判断，支持读取stdout和stderr
		   参数:
		cwd: 运行命令时更改路径，如果被设定，子进程会直接先更改当前路径到cwd
		timeout: 超时时间，秒，支持小数，精度0.1秒
		shell: 是否通过shell运行
	Returns: return_code
	Raises:  Exception: 执行超时
	"""
	if shell:
		cmdstring_list = cmdstring
	else:
		'''
		adb devices will be split ! fuck!
		'''
		cmdstring_list = shlex.split(cmdstring)
	if timeout:
		end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)

	#没有指定标准输出和错误输出的管道，因此会打印到屏幕上；
	sub = subprocess.Popen(cmdstring_list, cwd=cwd, stdin=subprocess.PIPE,shell=shell,bufsize=4096)

	#subprocess.poll()方法：检查子进程是否结束了，如果结束了，设定并返回码，放在subprocess.returncode变量中
	while sub.poll() is None:
		time.sleep(0.1)
		if timeout:
			if end_time <= datetime.datetime.now():
				raise Exception("Timeout：%s"%cmdstring)

	return str(sub.returncode)

def findAdbDocker():
		# TODO docker path
		cmd = DOCKER_BIN + " ps";
		print cmd
		ps = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		output_lines = ps.stdout.readlines()
		for line in output_lines:
			print line
			m = re.search(patternDockerPsAdb, line)
			if m:
				print m.group(1)
				return m.group(1)

def getAdblog(adbDocker):
	cmd = DOCKER_BIN + " exec " + adbDocker + " cat rio.adb.log.0  > " + RIO_ADB_LOG_TMP_FILE;
	print cmd
	execute_command(cmd)
	if not os.path.exists(RIO_ADB_LOG_TMP_FILE):
		print RIO_ADB_LOG_TMP_FILE + " is not exists!"
		return False
	return True


def getResult():
	print "getResult Enter"
	reportFile = getReportFileName()
	reportfileHandle = open ( reportFile, 'w' )
	reportfileHandle.write ( 'serial,product,model,device,online,offline,plug time,unplug time\n' )
	'''
	TODO need save host ip?
	'''
	#get device serial first
	'''
	cmd = DOCKER_BIN  + " exec " + adbDocker + " adb devices"

	print cmd
	adbdeviceCmd = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

	output_lines = adbdeviceCmd.stdout.readlines()
	print len(output_lines)
	output_lines = adbdeviceCmd.stderr.readlines()
	print len(output_lines)
	'''

	with open(ADB_DEVICES_TMP_FILE) as adbDevicesFp:
		for line in iter(adbDevicesFp.readline, ''):
	#for line in output_lines:
			print " ----------- " + line
			serial = ""
			product = ""
			model = ""
			device = ""
			online = 0
			offline = 0
			plugAndUnDate = None 
			plugTime = ""
			unplugTime = ""

			m = re.search(patternDeviceName, line)
			if m:
				serial = m.group(1)
			else:
				print 'not get serial'
				continue

			m = re.search(patternDeviceInfo, line)
			if m:
				product = m.group(1)
				model = m.group(2)
				device = m.group(3)

			# check key words in log file	
			with open(RIO_ADB_LOG_TMP_FILE) as logFp:
				for line in iter(logFp.readline, ''):
					onLineLog = "to uuid " + serial
					offlineLog = serial + " removed"

					if line.find(onLineLog) > 0:
						m = re.search(patternLogTime, line)
						if m:
							print 'pluginDate:' + m.group(1)

							if plugAndUnDate:
								if plugAndUnDate != m.group(1):
									print 'new date'
									if online > 0 or offline > 0:
										reportContent = serial + "," + product + "," + model + "," + device + "," + str(online) + "," + str(offline) + "," + plugTime + "," + unplugTime + "\n"
										reportfileHandle.write(reportContent)
										online = 0
										offline = 0
										plugTime = ""
										unplugTime = ""

							plugAndUnDate = m.group(1)

							online += 1
							if plugTime:
								plugTime += m.group(1) + " " + m.group(2) + " "
							else:
								plugTime = m.group(1) + " " + m.group(2) + " "

					elif line.find(offlineLog) > 0:
						m = re.search(patternLogTime, line)
						if m:
							print 'unpluginDate:' + m.group(1)
							if plugAndUnDate:
								if plugAndUnDate != m.group(1):
									print "new date"
									if online > 0 or offline > 0:
										reportContent = serial + "," + product + "," + model + "," + device + "," + str(online) + "," + str(offline) + "," + plugTime + "," + unplugTime + "\n"
										reportfileHandle.write(reportContent)
										online = 0
										offline = 0
										plugTime = ""
										unplugTime = ""
							plugAndUnDate = m.group(1)

							offline += 1


							if unplugTime:
								unplugTime += m.group(1) + " " + m.group(2) + " "
							else:
								unplugTime = m.group(1) + " " + m.group(2) + " "

			if online > 0 or offline > 0:
				reportContent = serial + "," + product + "," + model + "," + device + "," + str(online) + "," + str(offline) + "," + plugTime + "," + unplugTime + "\n"
				reportfileHandle.write(reportContent)

			# reset
			serial = ""
			product = ""
			model = ""
			device = ""
			online = 0
			offline = 0
			plugTime = ""
			unplugTime = ""
			plugAndUnDate = None

		reportfileHandle.close()


def getAdbDevices(adbDocker):
	#cmd = DOCKER_BIN  + " exec " + adbDocker + " adb devices > " + ADB_DEVICES_TMP_FILE;
	cmd = DOCKER_BIN  + " exec " + adbDocker + " adb devices  "
	print cmd
	execute_command(cmd)
	if not os.path.exists(ADB_DEVICES_TMP_FILE):
		print ADB_DEVICES_TMP_FILE + " is not exists!"
		return False
	return True

if __name__ == '__main__':
	print 'start'
	adbDocker = findAdbDocker()
	if adbDocker == None:
		print "adb docker not found"
		exit()
	else:
		print adbDocker

	cmd = DOCKER_BIN  + " exec " + adbDocker + " adb devices -l > " + ADB_DEVICES_TMP_FILE;
	print cmd
	
	shellFile = open ("/tmp/runShell.sh", "w")
	shellFile.truncate()
	shellFile.write(cmd)
	shellFile.close()
	execute_command("/bin/bash /tmp/runShell.sh")


	cmd = DOCKER_BIN + " exec " + adbDocker + " cat rio.adb.log.0  > " + RIO_ADB_LOG_TMP_FILE;
	shellFile = open ("/tmp/runShell.sh", "w")
	shellFile.truncate()
	shellFile.write(cmd)
	shellFile.close()
	execute_command("/bin/bash /tmp/runShell.sh")
	print cmd
#	if not getAdbDevices(adbDocker):
#		exit()

#	if not getAdblog(adbDocker):
#		exit()

	getResult()

