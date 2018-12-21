import unittest
from AutoTest_project.driver.driver import browser

class StarEnd(unittest.TestCase):
    #开始测试的准备
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    #测试结束的善后工作
    def tearDown(self):
        self.driver.quit()

