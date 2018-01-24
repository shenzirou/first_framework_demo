"""
浏览器引擎类
"""
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):

        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '\config\config.ini'
        print(file_path)
        # 但是对于有BOM(如Windows下用记事本指定为utf-8)的文件,需要使用 utf-8-sig, 使用utf-8没办法。
        # 【我没试过，http://blog.csdn.net/liujingqiu/article/details/77677256】
        # 对于我写的代码 此处是utf-8-sig 或者 utf-8 都可以
        config.read(file_path,encoding="utf-8")

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            self.driver = webdriver.Firefox()
            logger.info("firefox.")
        elif browser == "Chrome":
            self.driver = webdriver.Chrome()
            logger.info("Chrome.")
        elif browser == "IE":
            self.driver = webdriver.Ie()
            logger.info("Ie.")

        self.driver.get(url)
        logger.info("Open url: %s" % url)
        self.driver.maximize_window()
        logger.info("Maximize the current window.")
        self.driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        # self.driver = driver
        return self.driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("Now, Close and quit the browser.")
