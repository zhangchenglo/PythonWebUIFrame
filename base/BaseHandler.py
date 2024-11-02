"""
@Project ：PythonWebDriverUIFrame 
@File    ：BaseHandler.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:22 
@explain ：封装元素常用操作
"""
import logging
import time

from selenium.webdriver.support.select import Select

from utils.WebDriverUtil import DriverUtils

"""
This is about the encapsulation method of the business processing layer base class

"""


class BaseHandler:

    driver = DriverUtils.get_driver()

    """
    input
    """

    def input_content(self, element, content):
        """
        针对输入框元素输入内容方法
        :param element: 页面目标元素对象
        :param content: 输入框输入内容
        :return:
        """
        element.clear()
        element.send_keys(content)
        logging.info("input_text = {}".format(content))

    """
    click
    """

    def ele_click(self, element):
        """
        按钮点击方法
        :param element: 页面元素对象
        :return:
        """
        element.click()
        logging.info("click")

    """
    Select : 
        select_by_visible_text (文本值)
    """

    def ele_select(self, element, text):
        """
        下拉选择方法( 非input标签 )
        :param element: 页面目标元素
        :param text: 下拉元素对应的文本值(value)
        :return:
        """
        Select(element).select_by_visible_text(text)
        time.sleep(2)
        logging.info("ele_select = {}".format(text))

    """
    switch to iframe
    """

    def switch_iframe(self, element):
        """
        切换iframe标签方法
        :param element: 找到iframe目标元素
        :return:
        """
        try:
            self.driver.switch_to.frame(element)
        except Exception as e:
            print("iframe 切换错误，元素找不到,这是打印日志信息---->", e)

    """
    js
    """

    def execute_js(self, js):
        """
        执行js代码方法
        :param js: 执行JavaScript代码操作前端元素
        :return:
        """
        try:
            self.driver.execute_script(js)
        except Exception as e:
            print("js 执行错误, 打印日志信息---->", e)
