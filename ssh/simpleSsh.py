# -*- coding: utf-8 -*
import getopt
import sys
import paramiko

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
                elif name in ('-p', '--port'):
                    print "port: %s" % value
                elif name in ('-u', '--username'):
                    print "username: %s" % value
                elif name in ('-w', '--password'):
                    print "password: %s" % value
                elif name in ('-c', '--command'):
                    print "command: %s" % value
                elif name in ('-m', '--remote'):
                    print "remote: %s" % value
    except getopt.GetoptError:
        usage()

if __name__ == "__main__":
    handleOpt()
    conn = SSHConnection('192.168.111.9', 22, 'xuanqi', 'a123456')
    # conn.exec_command('ps')
    conn.exec_command('ls -l')
    data = conn.exec_command('adb devices')  #cd需要特别处理
    print "data:\n%s" % data
    # conn.download("/home/xuanqi/log4crc", "/tmp/log4crc")
    conn.close()
