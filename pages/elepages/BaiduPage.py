"""
@Project ：PythonWebDriverUIFrame 
@File    ：BaiduPage.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:30 
@explain ：百度页面元素
"""
from selenium.webdriver.common.by import By


class BaiduPage:

    def __init__(self):

        # 百度搜索输入框元素
        self.search_input = By.ID, "kw"
        # 百度点击按钮元素
        self.search_button = By.ID, "su"
