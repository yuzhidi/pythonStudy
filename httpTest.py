import httplib
conn = httplib.HTTPConnection("file.lab.tb/upload/aea0d0688dc246ab8809c1dfac45e2af.js")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print data1
