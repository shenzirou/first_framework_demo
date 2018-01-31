"""
测试脚本
"""
import time
import unittest
from framework.brower_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

"""
unittest
一个单元测试框架
共享测试用例中的初始化和关闭退出代码
最小单元是test,即一个测试用例
1）测试固件
包含“测试代码之前的准备部分”setUp()和“测试结束之后的清扫代码”tearDown()
2）测试用例
以test开头的函数
"""


class BaiduSearch(unittest.TestCase):

    """
    def setUp(self):
    def tearDown(self):
    用这两个方法时，下面测试用例只会执行最后面一个
    若想执行全部得改成类方法
    def setUpClass(cls):
    def tearDownClass(cls):
    """
    @classmethod
    def setUpClass(cls):
        """
        前提准备工作
        :return:
        """
        cls.engine = BrowserEngine.__new__(BrowserEngine)
        cls.driver = cls.engine.open_browser()

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作
        :return:
        """
        cls.engine.quit_browser()
        # self.driver.quit()

    def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search('胡歌')
        time.sleep(1)
        homepage.get_windows_img()  # 基类截图方法
        try:
            assert '胡歌' in self.driver.title
            print('测试通过.')
        except Exception as e:
            print('测试失败.', format(e))

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



if __name__ == '__main__':
    unittest.main()
