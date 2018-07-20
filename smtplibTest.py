# coding:utf8
import smtplib
sender = ''
my_pass= ''
receivers = ['']


# receivers = ['xxxx@testbird.com']
# if send to testbird.com will cause error
# plib.SMTPDataError: (554, 'DT:SPM 163 smtp12,EMCowADnp0V0QlFb0ozOHg--.23600S2 1532052084,please see http://mail.163.com/help/help_spam_16.htm?ip=61.154.12.206&hostid=smtp12&time=1532052084')

######### 示例：邮箱内容显示

# 发件人：	你的好友<lalalalalalalatest@163.com>
# 收件人：	Leo<leocone@qq.com>
# 时间：	2018年7月20日(周五) 10:21
# 大小：	1.8KB

message = """From: 你的好友 <lalalalalalalatest@163.com>
# receivers = ['wangliang@testbird.com']
# if send to testbird.com will cause error
# plib.SMTPDataError: (554, 'DT:SPM 163 smtp12,EMCowADnp0V0QlFb0ozOHg--.23600S2 1532052084,please see http://mail.163.com/help/help_spam_16.htm?ip=61.154.12.206&hostid=smtp12&time=1532052084')

"""

try:
	obj = smtplib.SMTP('smtp.163.com')
	obj.login(sender, my_pass)
	obj.sendmail(sender, receivers, message)
	print 'Ok, send mail successed'
except Exception as e:
	print e
	raise
else:
	pass
finally:
	pass