from framework.base_page import BasePage

"""
POM（Page Object Model）框架设计中一种设计思想,
将页面元素和业务逻辑和测试脚本分离到两个不同类文件
"""
class HomePage(BasePage):

    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)