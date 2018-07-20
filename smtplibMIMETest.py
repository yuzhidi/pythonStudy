import smtplib
from email.mime.text import MIMEText

sender = 'wxtysg@163.com'  # 发件人邮箱账号
my_pass= 'gahghfh'  # 发件人邮箱授权码
receiver="888888@qq.com" #接收人邮箱
def mail():
    ret = True
    try:
        content = "hello world"# 邮件内容
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = sender  #发件人邮箱账号
        msg['To']=receiver
        msg['Subject'] = "Python发送邮件测试"  # 邮件的主题
#创建连接对象并连接到服务器
        server = smtplib.SMTP("smtp.163.com")# 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, my_pass)# 发件人邮箱账号、授权码
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()  # 关闭连接
    except Exception as e: 
        ret = False
        print(e)
    return ret

ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")