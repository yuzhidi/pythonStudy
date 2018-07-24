#-*- coding:utf-8 -*-
#07.urllib2_get.py

import urllib
import urllib2

url = "http://file.lab.tb/upload/aea0d0688dc246ab8809c1dfac45e2af.js"
word = {"wd":"传智播客"}
word = urllib.urlencode(word) #转换成url编码格式(字符串)

newurl = url + "?" + word

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib2.Request(newurl,headers = headers)

response = urllib2.urlopen(request)

print(response.read())

print ' >>>>>>>>>>>>>>>>>> urllib.URLopener'
#------------------------------------
testfile = urllib.URLopener()
testfile.retrieve("http://file.lab.tb/upload/aea0d0688dc246ab8809c1dfac45e2af.js", "leo-retrieve.js")

testfile.retrieve("http://quail.lab.tb/api/task/execution/mYMkKX/", "/tmp/mYYYYYYYYY")
#--------------------------------------

print ' >>>>>>>>>>>>>>>>>> import requests'
import requests

print '>>>>>>>>>>>>>>>>>>>>>>>>> test HTTP 404 Not Found'
url = 'http://quail.lab.tb/api/testcase/app/2832cb97e74f44369efd2d460d4/'
r = requests.get(url)
print r.ok
print r.content

# urllib2.tocke
# r = urllib2.urlopen(url)
# print(r.read())

print '################## get token'
quail_user_email = 'xxx'
quail_user_password ='tb123456'
ObtainAuthTokenAPI = 'http://quail.lab.tb/api/customer/obtain-auth-token/?email=%s&password=%s' % (quail_user_email, quail_user_password)
r = requests.get(ObtainAuthTokenAPI)
print r.ok

quail_user_email = 'xubo@testbird.com'
ObtainAuthTokenAPI = 'http://quail.lab.tb/api/customer/obtain-auth-token/?email=%s&password=%s' % (quail_user_email, quail_user_password)
r = requests.get(ObtainAuthTokenAPI)
print r.ok

TOKEN = 'dc8847f0b5b7334b39cbfe13094ad4e61ed8500b'
HEADERS = {'Authorization': 'token {}'.format(TOKEN)}

print '############################### test not exist'
url = 'http://quail.lab.tb/api/testcase/app/2832cb369efd2d460d40ae9a/'
r = requests.get(url, headers=HEADERS)
print r.ok
print r.content

print '############################### test ok'
url = 'http://quail.lab.tb/api/testcase/app/2832cb97e74f44369efd2d460d40ae9a/'
r = requests.get(url, headers=HEADERS)
print r.ok
print len(r.content)

# url = "http://file.lab.tb/upload/aea0d0688dc246ab8809c1dfac45e2af.js"
# r = requests.get(url)
# print len(r.content)

# url = 'http://quail.lab.tb/api/task/execution/mYMkKX'
# r = requests.get(url)
# print len(r.content)




