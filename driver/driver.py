from selenium import webdriver

def browser():

    #加载浏览器驱动
    driver=webdriver.Firefox()
    #PhantomJS是无头浏览器，使用时需要把安装包放到selenium的安装目录下即可
    # driver=webdriver.PhantomJS

    #测试打开百度网页
    # driver.get("http://www.baidu.com")

    return driver

if __name__=='__main__':
    browser()
