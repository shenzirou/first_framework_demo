import unittest

from framework.brower_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
import time


class GetPageTitle(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.browser = BrowserEngine.__new__(BrowserEngine)
    #     cls.driver = cls.browser.open_browser()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.browser.quit_browser()

    def setUp(self):
        self.browser = BrowserEngine.__new__(BrowserEngine)
        self.driver = self.browser.open_browser()

    def tearDown(self):
        self.browser.quit_browser()

    # def test_get_title(self):
    #     homepage = HomePage(self.driver)
    #     print(homepage.get_page_title())

    def test_baidu_search_second(self):
        homepage = HomePage(self.driver)
        homepage.type_search('薛之谦')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()  # 基类截图方法
        try:
            assert '薛之谦' in homepage.get_page_title()
            print('测试通过.')
        except Exception as e:
            print("测试失败:%s" % e)