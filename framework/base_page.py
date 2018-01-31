import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from selenium import webdriver
from framework.logger import Logger


# 创建logger实例
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    页面基类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器 结束操作
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进
    def forward(self):
        self.driver.forward()
        logger.info("在页面上点击前进.")

    # 浏览器后退
    def back(self):
        self.driver.back()
        logger.info("在页面上点击后退.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d s."%seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭并退出浏览器.")
        except NameError as e:
            logger.error("退出浏览器失败: %s."%e)

    # 保存图片
    def get_windows_img(self):
        """
        将图片直接保存到项目下.\screenshots下
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/' \
                    + time.strftime('%Y%m%d%H%M', time.localtime()) + '.png'
        try:
            self.driver.get_screenshot_as_file(file_path)
            logger.info("已经截图并保存到文件：%s"%file_path)
        except NameError as e:
            logger.error("截图失败:%s."%e)
            # 截图失败重新调用此方法
            self.get_windows_img()

    # 定位元素
    def find_element(self, selector):
        """
        根据 => 切割字符串
        页面里定位元素的方法：
        submit_btn = "id=>su"
        login_lnk = "xpath=>//*[@id='u1']/a[7]"
        :param selector:
        :return:
        """

        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("通过 %s 已经成功的找到元素: %s ."%(selector_by,selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s"%e)
                self.get_windows_img()  # 截图
        elif selector_by == 'n' or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_by)
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("已经通过 %s 成功找到元素: %s ."%(selector_by,selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException : %s"%e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("请输入一个有效类型的目标元素.")

        return element

    # 输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("在输入框已经输入：\'%s\' ."%text)
        except NameError as e:
            logger.error("输入失败: %s" %e)
            self.get_windows_img()

    # 点击
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("\'%s\'元素被点击."%el.text)
        except NameError as e:
            logger.error("点击失败:\'%s\'"%e)

    def get_page_title(self):
        logger.info("当前页标题:\'%s\'"%self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("休眠%ds" % seconds)

