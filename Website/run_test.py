import unittest
from AutoTest_project.Website.test_case.model.function import *
from BSTestRunner import BSTestRunner
import time

report_dir='./test_report'
test_dir='./test_case'

print("start run test case")
#下行代码中pattern后面可以接匹配字符串如=“test*.py”
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_login.py")

now=time.strftime("%Y-%m-%d %H-%M-%S")
report_name=report_dir+'/'+now+'result.html'

print("start write report")
#运行前需要把BSTestRunner.py文件中120行处的Unicode换成str 为了防止有中文时出现乱码
with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title="Test Report",description="login test")
    runner.run(discover)
    f.close()
print("find latest report")
latest_report=latest_report(report_dir)

print("send email report")
# send_mail(latest_report)
print("test is end")