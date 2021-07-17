"""
============================
@auther:多测师-黄sir
@time:2021/7/15:16:03
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
# 此模块用来执行所有的测试用例
import unittest
from public.utils.HTMLTestRunner3_New import HTMLTestRunner
from public.utils.mail3 import SendMail
from config.Config import *
from time import strftime
def run_all():
    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,pattern='Test*.py')
    print(discover)
    now = strftime('%Y-%m-%d-%H-%M-%S')
    filename = report_path+'\\'+str(now)+'_UI-Auto-report.html'
    f = open(file=filename,mode='wb')
    runner = HTMLTestRunner(stream=f,
                            title='BBS论坛UI自动化测试报告',
                            description='用例执行情况如下：'
                            )
    runner.run(discover)
    f.close()
    # sendmail = SendMail(send_msg=filename,attachment=filename)
    # sendmail.send_mail()
run_all()








