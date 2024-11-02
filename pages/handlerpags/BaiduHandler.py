"""
@Project ：PythonWebDriverUIFrame 
@File    ：BaiduHandler.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:40 
@explain ：针对返回的百度元素进行操作
"""
import allure

from base.BaseHandler import BaseHandler
from pages.elepagesimpl.BaiduPageImpl import BaiduPageImpl


class BaiduHandler(BaseHandler):

    def __init__(self):
        super().__init__()
        self.baidu_page_impl = BaiduPageImpl()

    @allure.step("在百度搜索输入框中输入搜索内容")
    def input_search_content(self, content):
        self.input_content(self.baidu_page_impl.find_search_input_ele(), content)

    @allure.step("点击百度搜索按钮")
    def click_search_button(self):
        self.ele_click(self.baidu_page_impl.find_search_button_ele())
