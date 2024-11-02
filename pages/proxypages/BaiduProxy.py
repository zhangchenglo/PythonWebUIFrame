"""
@Project ：PythonWebDriverUIFrame 
@File    ：BaiduProxy.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:44 
@explain ：百度搜索业务流程处理
"""
from pages.handlerpags.BaiduHandler import BaiduHandler


class BaiduProxy:

    def __init__(self):
        self.baidu_handler = BaiduHandler()

    def search_content(self, content):
        """
        :param content:  百度搜索输入框内容
        :return: 根据输入框内容进行百度搜索
        """
        self.baidu_handler.input_search_content(content)
        self.baidu_handler.click_search_button()



