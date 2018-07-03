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

if not os.path.basename('/sw724.vaps/'):
	print "only dir"
print("get filename:",os.path.basename('onlyname'))
