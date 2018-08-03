# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendMail(object):
    def __init__(self, username, passwd, recv, title, content, file=None, email_host='smtp.163.com', port=25):
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.email_host = email_host
        self.port = port

    def send_mail(self):
        msg = MIMEMultipart()
        # 发送内容的对象
        if self.file:  # 处理附件的
            att = MIMEText((open(self.file, 'r').read()),"plain","utf-8")
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"' % self.file
            msg.attach(att)
        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        # 将多个账号'aaa.@qq.com;bbbb@163.com' 以分号分割，分割为list
        self.recv = self.recv.split(';')
        if isinstance(self.recv, list):
            msg['To'] = ','.join(self.recv)
        else:
            msg['To'] = self.recv  # 接收者账号列表
        if self.username.endswith('qq.com'):  # 如果发送者是qq邮箱
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()


if __name__ == '__main__':
    m = SendMail(
        username='zzzzz@163.com', passwd='xxxxxxx', file='a.txt', recv='xxxxxx@qq.com;xxxxxx@qq.com',
        title='多个收件人', content='哈哈哈啊哈哈哈哈', email_host='smtp.163.com', port=25
    )
    m.send_mail()