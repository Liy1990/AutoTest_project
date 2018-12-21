from AutoTest_project.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By

class LoginPage(Page):
    #目标网页页签地址
    url='/'

    #用户名、密码和登录按钮定位元素
    username_loc=(By.NAME,'username')
    password_loc=(By.NAME,'password')
    submit_loc=(By.NAME,'Submit')

    #输入用户名的方法
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    #输入密码的方法
    def type_password(self,password):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(password)

    #点击登录按钮的方法
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

     #登录的方法
    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    loginPass_loc=(By.LINK_TEXT,'我的空间')
    loginFail_loc=(By.NAME,'username')

    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc).text
