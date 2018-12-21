from selenium import webdriver
import os
import smtplib                                     #发送邮件模块
from email.mime.text import MIMEText               #定义邮件内容
from email.mime.text import MIMENonMultipart       #用于传送附件
from email.header import Header                    #定义邮件标题

#截图功能并保存
def insert_img(driver,filename):
    #获取当前目录
    func_path=os.path.dirname(__file__)
    # print(func_path)

    #获取上一级目录
    base_dir=os.path.dirname(func_path)
    # print(base_dir)

    #将目录的路径转换为字符串格式
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')

    #拆分目录获取伤及目录路径
    base=base_dir.split('/Website')[0]
    # print(base)

    #合并获得截图的最终目录并指定存放位置
    filepath=base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)

#发送邮件
def send_mail(latest_report):
    #打开最新测试报告并写入邮件的发送内容中，然后关闭测试报告
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    #邮箱服务器、帐号、密码，此处要确保邮箱开启了IMAP/SMTP服务
    smtpserver='smtp.163.com'
    user=''
    password=''

    #发件人和收件人地址
    sender=''
    receives=['','']

    #定义邮件主题及格式
    subject='测试报告'
    msg=MIMEText(mail_content,'html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=sender
    msg['To']=','.join(receives)

    #邮件登录验证
    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user,password)

    #发送邮件
    print("开始发送")
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print("发送结束")

#查找最新的测试报告
def latest_report(report_dir):
    #加载报告目录的所有报告列表
    lists = os.listdir(report_dir)

    #按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))

    #输出最新报告的路径并返回
    file = os.path.join(report_dir,lists[-1])
    return file

if __name__=='__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.baidu.com")
    insert_img(driver,"baidu.jpg")