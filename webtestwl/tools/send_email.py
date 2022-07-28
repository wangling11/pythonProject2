# -- coding: utf-8 --
# @Time : 2022/5/27 15:50
# @Author : wangling
# @Email : 731569578@qq.com
# @File : send_email.py
# @Software: PyCharm
class sendEmail:
    def send_email(self):
        #email_to  收件方
        # filepath 你要发送附件的地址
        #如 名字所示 Multipart 就是分多个附件
        msg= MiMEMultipart();
