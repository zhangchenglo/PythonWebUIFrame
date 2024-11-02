"""
@Project ：PythonWebDriverUIFrame 
@File    ：BaiduPageImpl.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:33 
@explain ：百度元素实现
"""
from base.BasePage import BasePage
from pages.elepages.BaiduPage import BaiduPage


class BaiduPageImpl(BasePage):

    def __init__(self):
        super().__init__()
        self.baidu_page = BaiduPage()

    def find_search_input_ele(self):
        return self.get_element(self.baidu_page.search_input)  # 返回百度输入框元素

    def find_search_button_ele(self):
        return self.get_element(self.baidu_page.search_button)  # 返回百度搜索按钮元素



