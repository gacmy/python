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

msg = MIMEText('''

一、本周工作总结

# 日常工作
   无

# 核心项目  

* 可听app V2.7.18
     * 本周完成：
        -对播放器图片加载增加缓存机制
        -兑换码功能接口联调
        -自定义圆形图片优化内存回收
        -音频封面图更改
        -进行压力测试
        -修复禅道bug
        -发布小米首发版本2.7.18
        -集成内存工具,检测内存，优化
        -发布2.7.18版本，代码进行备份
        -内存分析工具分析内存测试内存泄露
        -2.7.27 查看prd，和ui设计图，对优惠券模块进行准备工作


#非项目性工作开展情况 
   *项目 
     -暂无




二、下周工作计划

#日常工作
  -全面屏刘海屏进行项目升级适配
  



# 核心项目  
  * 可听app V2.7.27
    -2.7.27功能进行开发



        
#非项目性工作开展情况 
 暂无


三、问题及反馈
       
  暂无

''','plain','utf-8')#发件内容

msg['From'] = _format_addr("高安晨<%s>"%from_addr)

msg['To'] = _format_addr("某某某<%s>"%to_addr)

msg['Subject'] = Header('发送邮件的标题...','utf-8').encode() #标题

server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)

server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
print "send email success"