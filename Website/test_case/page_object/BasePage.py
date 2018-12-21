from time import sleep
class Page():
    #初始化浏览器
    def __init__(self,driver):
        self.driver=driver
        self.base_url='http://www.baidu.com'    #要打开的网址
        #超时等待
        self.timeout=10

    #私有的打开网址的方法
    def _open(self,url):
        #目标网站的细分页面地址处理与合并
        url_=self.base_url+url
        #窗口最大化
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        #断言是否为目标网页
        assert self.driver.current_url == url_,'Did not land on %s' %url_

    #通过此公有方法调用私有的打开网页的方法
    def open(self):
        self._open(self.url)

    #定位元素的方法
    def find_element(self,*loc):
        return self.driver.find_element(*loc)