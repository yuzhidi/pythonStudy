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
url = "http://file.lab.tb/upload/aea0d0688dc246ab8809c1dfac45e2af.js"
r = requests.get(url)
print len(r.content)

url = 'http://quail.lab.tb/api/task/execution/mYMkKX'
r = requests.get(url)
print len(r.content)




