# coding=utf-8
'''

Created on 2017-5-6

@author: Leo
'''
from subprocess import Popen, PIPE
import shlex
import datetime
import subprocess
import time
import re

'''
20170427 17:00:41.884 INFO	  - change sn:TESTBIRD_HC4AVYC01829_12479 to uuid f09e639d-b4ab-4e12-910d-694d9abe8b3c
20170430 17:02:01.604 INFO	  - transport: f09e639d-b4ab-4e12-910d-694d9abe8b3c removed
'''
patternLogTime = re.compile("(\S+\s.*?)\s")
patternDeviceName = re.compile("(\S+)\s+device usb");
patternDeviceInfo = re.compile("product:(.*)\smodel:(.*)\sdevice:(.*)");
patternDockerPsAdb = re.compile("(r-stf-adb.*)");
patternDockerPsTest = re.compile(".*(rio.lab.tb.*)");
RIO_ADB_LOG_TMP_FILE = "/tmp/rio.adb.log"
ADB_DEVICES_TMP_FILE = "/tmp/adbdevices"
REPORT_FILE = "/tmp/statisticalAdbreport.csv"
DOCKER_BIN = "/usr/local/bin/docker"


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
		ps = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		output_lines = ps.stdout.readlines()
		for line in output_lines:
			print line
			m = re.search(patternDockerPsAdb, line)
			if m:
				print m.group(1)
				return m.group(1)

def findTestDocker():
		# TODO docker path
		cmd = DOCKER_BIN + " ps";
		ps = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
		output_lines = ps.stdout.readlines()
		for line in output_lines:
			print line
			m = re.search(patternDockerPsTest, line)
			if m:
				print m.group(1)
				return m.group(1)

def getAdblog(adbDocker):
	cmd = DOCKER_BIN + " " + adbDocker + " cat rio.adb.log.0 > " + RIO_ADB_LOG_TMP_FILE;
	execute_command(cmd)
	if not os.path.exists(RIO_ADB_LOG_TMP_FILE):
		print RIO_ADB_LOG_TMP_FILE + " is not exists!"
		return False
	return True


def getResult():
	reportFileHandle = open ( REPORT_FILE, 'w' )
	'''
	TODO need save host ip?
	'''
	reportfileHandle.write ( 'serial,product,model,device,online,offline,plug time,unplug time\n' )
	cmd = DOCKER_BIN  + " " + adbDocker + " adb devices"
	adbdeviceProcess = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	output_lines = adbdeviceProcess.stdout.readlines()
	for line in output_lines:
			serial = None
			product = ""
			model = ""
			device = ""
			online = 0
			offline = 0
			plugTime = None
			unplugTime = None

			m = re.search(patternDeviceName, line)
			if m:
				deviceSerial = m.group(1)
			else:
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
						online += 1
						m = re.search(patternLogTime, line)
						if m:
							plugTime += m.group(1) + " "

					elif line.find(offlineLog) > 0:
						offline += 1
						m = re.search(patternLogTime, line)
						if m:
							unplugTime += m.group(1) + " "

			if online > 0 or offline > 0:
				reportContent = serial + "," + product + "," + model + "," + device + "," + online + "," + offline + "," + plugTime + "," + unplugTime + "\n"
				reportfileHandle.write(reportContent)

			# reset
			serial = None
			product = ""
			model = ""
			device = ""
			online = 0
			offline = 0
			plugTime = None
			unplugTime = None

	reportFileHandle.close()


def getAdbDevices(adbDocker):
	cmd = DOCKER_BIN  + " " + adbDocker + " adb devices >> " + ADB_DEVICES_TMP_FILE;
	execute_command(cmd)
	if not os.pth.exists(ADB_DEVICES_TMP_FILE):
		print ADB_DEVICES_TMP_FILE + " is not exists!"
		return False
	return True

if __name__ == '__main__':
	findTestDocker()
	adbDocker = findAdbDocker()
	if adbDocker == None:
		print "adb docker not found"
		exit()
	else:
		print adbDocker

	if not getAdblog(adbDocker):
		exit()

	if not getAdbDevices(adbDocker):
		exit()

	getResult()

