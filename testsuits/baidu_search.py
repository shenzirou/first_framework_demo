"""
测试脚本
"""
import time
import unittest
from framework.brower_engine import BrowserEngine

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

    def setUp(self):
        """
        前提准备工作
        :return:
        """
        self.engine = BrowserEngine.__new__(BrowserEngine)
        self.driver = self.engine.open_browser()


    def tearDown(self):
        """
        测试结束后的操作
        :return:
        """
        self.engine.quit_browser()
        # self.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element_by_id('kw').send_keys("胡歌")
        time.sleep(1)
        try:
            assert '胡歌' in self.driver.title
            print('测试通过.')
        except Exception as e:
            print('测试失败.', format(e))


if __name__ == '__main__':
    unittest.main()
