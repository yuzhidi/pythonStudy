# -*- coding: utf-8 -*-
import paramiko
 
 
pkey='path-to-key-file'
key=paramiko.RSAKey.from_private_key_file(pkey)
paramiko.util.log_to_file('paramiko.log')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.load_system_host_keys()
ssh.connect('182.150.24.81',username = 'core',pkey=key)
stdin,stdout,stderr=ssh.exec_command('hostname')
print(stdout.read())
stdin,stdout,stderr=ssh.exec_command('ls')
print(stdout.readlines())


