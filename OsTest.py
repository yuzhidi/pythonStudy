import os
print os.getcwd()

print("1 get pathname:",os.path.dirname('/Users/liuxiaolong/PycharmProjects/untitled/sw724.vaps'))
print("2 get filename:",os.path.basename('/Users/liuxiaolong/PycharmProjects/untitled/sw724.vaps'))
print("3 get pathname:",os.path.dirname('sw724.vaps'))
print("4 get filename:",os.path.basename('sw724.vaps'))
print '-------------------'
print("get pathname:",os.path.dirname('/sw724.vaps'))
print("get pathname:",os.path.dirname('/sw724.vaps/'))
print("get pathname /:",os.path.dirname('/sw724.vaps//'))
print("get filename:",os.path.basename('/sw724.vaps/'))

print('url basename:', os.path.basename('http://file.lab.tb/upload/1531380628510_43487ded.jpg'))

if not os.path.basename('/sw724.vaps/'):
	print "only dir"


print("get filename:",os.path.basename('onlyname'))

print '>>>>>>>>>>>>>>>>>>>>>>>>>> os.walk'
for root, dirs, files in os.walk('/Users/wangliang/Study/HotPot/QUAIL-6314', False):
	print 'dir-------'
	print dirs
	print 'files-------'
	print files
	for item0 in files:
		print '======================'
		print item0
		print type(item0)
		if type(item0) != list:
			continue
		for file in item0:
			print file
			# if file.startswith('')

