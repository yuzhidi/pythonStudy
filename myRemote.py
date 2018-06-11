# -*- coding: utf-8 -*
import os
import getopt
import sys
import paramiko
import re
import json
import pprint

gIp = '192.168.111.9'
gPort = 22
gUsername = 'xuanqi'
gPassword = 'a123456'
gCommand = ''
gRemoteFile = ''
gPrint = True

PatternDeviceName = re.compile("(\S+)\s+device usb");
PatternDeviceInfo = re.compile("product:(.*)\smodel:(.*)\sdevice:(.*)");

def usage():
    print ' -h help \n' \
        ' -i --ip address\n' \
        ' -p --port number\n' \
        ' -u --username ssh user name\n' \
        ' -w --password ssh password\n' \
        ' -c --command command will execute on remote host\n' \
        ' -m --remote file path\n'


class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()

    # 建立连接
    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport

    #下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    #上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    #执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            print data.strip()   #打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print err.strip()    #输出错误结果
            return err

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()

def openConnection():
    pass

def closeConnection():
    pass

def getHostConfig():
    pass

def getFileFromAndroid():
    pass

def getMyLogFile():
    pass

def getMyLogFileAll():
    pass

def AndroidCmdPS():
    pass

def getDeviceList(data):
    deviceList = []
    lines = data.splitlines()
    # print lines
    for line in lines:
        #print "line %s" % line
        m = re.search(PatternDeviceName, line)
        if m:
            deviceSerial = m.group(1)
        else:
            continue

        m = re.search(PatternDeviceInfo, line)
        if m:
            product = m.group(1)
            model = m.group(2)
            device = m.group(3)
            #print "product:%s, model:%s, device:%s" % (product, model, device)
            deviceInfo = {}
            deviceInfo['uuid'] = deviceSerial
            deviceInfo['product'] = product
            deviceInfo['model'] = model
            deviceInfo['device'] = device
            deviceInfo['ip'] = gIp
            # for grep easy
            deviceInfo['uuid_ip'] = deviceSerial + '_'  + gIp
            deviceList.append(deviceInfo)
    return deviceList

def deviceList2File(deviceList):
    #
    # save device info to file
    #
    uuidFilePath = os.getcwd() + os.sep + 'adbdevicesList'
    print uuidFilePath
    fo = open(uuidFilePath, "w+")
    json.dump(deviceList, fo, indent=4)
    fo.close()
    if gPrint:
        print json.dumps(deviceList, indent=4)
    pass

def adbDevices():
    conn = SSHConnection(gIp, gPort, gUsername, gPassword)
    data = conn.exec_command('adb devices -l')
    deviceList = getDeviceList(data)
    deviceList2File(deviceList)

    conn.close()

def testDownload():
    conn.download("/home/xuanqi/log4crc", "/tmp/log4crc")
    pass

def handleOpt():
    try:
        options, args = getopt.getopt(sys.argv[1:], "hi:p:u:w:c:m:", ['help', "ip=", "port=", "username=", "password=", "command=", "remote="])
        if len(sys.argv) == 1:
            usage()
            for name, value in options:
                if name in ('-h', '--help'):
                    usage()
                elif name in ('-i', '--ip'):
                    print "ip: %s" % value
                    gIp = value
                elif name in ('-p', '--port'):
                    print "port: %s" % value
                    gPort = value
                elif name in ('-u', '--username'):
                    print "username: %s" % value
                    gUsername = value
                elif name in ('-w', '--password'):
                    print "password: %s" % value
                    gPassword = value
                elif name in ('-c', '--command'):
                    print "command: %s" % value
                    gCommand = value
                elif name in ('-m', '--remote'):
                    print "remote: %s" % value
                    gRemoteFile = value
    except getopt.GetoptError:
        usage()


if __name__ == "__main__":
    handleOpt()
    adbDevices()
