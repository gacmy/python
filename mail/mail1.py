#refuytizdjkcbbed
# -*- coding: utf-8 -*-
from email.header import Header

from email.mime.text import  MIMEText

from email.utils import  parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = '675766130@qq.com' #发送地址

password = 'refuytizdjkcbbed' #登录密码

to_addr = "gaoanchen@123.com.cn" #收件地址

smtp_server = 'smtp.qq.com'   #smtp服务器

msg = MIMEText('Python 爬虫运行异常,异常信息','plain','utf-8')#发件内容

msg['From'] = _format_addr("Python 爬虫一号<%s>" %from_addr)

msg['To'] = _format_addr("管理员<%s>"%to_addr)

msg['Subject'] = Header('一号爬虫运行异常.','utf-8').encode() #标题

server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)

server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
print "send email success"