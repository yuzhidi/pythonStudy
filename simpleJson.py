#!/usr/bin/python
import json
import pprint

data = [
{ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } , {'e' : 3}
]

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print 'json.loads:%s' % text
print text


print data[0]
print data[0]['c']

print '>>>>>>>>>>> 1 >>>>>>>>>>>>>>>>'
jsonData = json.dumps(data)
print jsonData

print '>>>>>>>>>>> 2 >>>>>>>>>>>>>>>>'
data =  { 'a' : 1, 'b' : 2,
 'c' : 3, 'd' : 4, 'e' : 5 }
print data['b']
# print data['w']

testIpTable = [
	{
		'ip' : '192.168.110.165',
		'quail' : 'quail.lab.tb'
	},
	{
		"ip" : '192.168.110.200',
		'quail' : 'quail2.lab.tb'
	}
]


print '>>>>>>>>>>> 3 >>>>>>>>>>>>>>>>'
print testIpTable[0]
print testIpTable[0]['ip']

print '>>>>>>>>>>> 4 >>>>>>>>>>>>>>>>'
jsonData = json.dumps(testIpTable)
print jsonData

print '>>>>>>>>>>> 5 >>>>>>>>>>>>>>>>'
dataLoads = json.loads('{"name": "Frank", "age": 39}')
print dataLoads['name']

#
# json must use " " not ''
#
dataLoads = json.loads('[ { "ip" : "192.168.110.165", "quail" : "quail.lab.tb" }, { "ip" : "192.168.110.200", "quail" : "quail2.lab.tb" } ]')
print dataLoads[1]['quail']

print '>>>>>>>>>>> 6 >>>>>>>>>>>>>>>>'
fo = open("/tmp/testIpTable0", "rw+")

fileData = fo.read()

fo.close()

print 'file content:\n %s' % fileData
print json.dumps(fileData)

dataLoads = json.loads(fileData)
print 'ip in file : %s' % dataLoads[0]['ip']

fileData = fileData.replace('\n', '').replace('\t','');
print fileData
print json.dumps(fileData)


print '>>>>>>>>>>> 7 >>>>>>>>>>>>>>>>'
fo = open("/Users/wangliang/Study/pythonStudy/adbdevicesList", "r")
fileData = fo.read()
fo.close()
print fileData

print '>>>>>>>>>>> 7 PrettyPrinter >>>>>>>>>>>>>>>>'
pp = pprint.PrettyPrinter(indent=4)

dataLoads = json.loads(fileData)
pp.pprint(dataLoads)

pString = pp.pformat(dataLoads)
print pString

# print aDevice['model']
# print 'model in file : %s' % dataLoads[0]['model']
