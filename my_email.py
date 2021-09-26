from smtplib import SMTP_SSL
# eamil包的下载地址
# https://pypi.tuna.tsinghua.edu.cn/simple/email/
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# smtplib模块主要负责发送邮件：是一个发送邮件的动作，连接邮箱服务器，登录邮箱，发送邮件（有发件人，收信人，邮件内容）。
# email模块主要负责构造邮件：指的是邮箱页面显示的一些构造，如发件人，收件人，主题，正文，附件等。
def my_email():
    host_server = 'smtp.qq.com'  # qq邮箱smtp服务器
    sender_qq = '1299639230@qq.com'  # 发件人邮箱
    pwd = 'jivgmmllksqogiji'
    receiver = '1299639230@qq.com'  # 收件人邮箱
    # receiver = '1039620449 @ qq.com'
    mail_title = '每日打卡成功'  # 邮件标题
    mail_content = "打卡成功"  # 邮件正文内容
    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    # msg["To"] = Header("测试邮箱",'utf-8')
    msg['To'] = receiver
    # 邮件正文内容
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    smtp = SMTP_SSL(host_server)  # ssl登录
    # login(user,password):
    # user:登录邮箱的用户名。
    # password：登录邮箱的密码，像笔者用的是网易邮箱，网易邮箱一般是网页版，需要用到客户端密码，需要在网页版的网易邮箱中设置授权码，该授权码即为客户端密码。
    smtp.login(sender_qq, pwd)

    # sendmail(from_addr,to_addrs,msg,...):
    # from_addr:邮件发送者地址
    # to_addrs:邮件接收者地址。字符串列表['接收地址1','接收地址2','接收地址3',...]或'接收地址'
    # msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
    try:
        smtp.sendmail(sender_qq, receiver, msg.as_string())
        print("执行成功")
    except Exception as e:
        print('发生错误', e)


    # quit():用于结束SMTP会话。
    smtp.quit()


if __name__ == '__main__':
    my_email()
