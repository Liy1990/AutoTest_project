import unittest
from AutoTest_project.Website.test_case.model import function,myunit
from AutoTest_project.Website.test_case.page_object.LoginPage import *
from time import sleep

class LoginTest(myunit.StarEnd):
    def test_login1_normal(self):
        '''username and password is normal'''
        print("test_login1_mormal is start test")
        po=LoginPage(self.driver)
        po.Login_action('51zxw',123456)
        sleep(2)

        self.assertEqual(po.type_loginPass_hint(),'我的空间')
        function.insert_img(self.driver,"51zxw_login1_normal.jpg")
        print("test_login1_normal test end")

    def test_login2_PasswordError(self):
        '''username is OK and password is error'''
        print("test_login2_PasswordError is start test")
        po=LoginPage(self.driver)
        po.Login_action('51zxw',12333)
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"51zxw_login2_normal.jpg")
        print("test_login2_fail test end")

    def test_login3_Empty(self):
        '''username and password is empty'''
        print("test_login2_PasswordError is start test")
        po=LoginPage(self.driver)
        po.Login_action('','')
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"51zxw_login3_empty.jpg")
        print("test_login3_empty test end")

if __name__ == '__main__':
    unittest.main()