"""
@Project ：PythonWebDriverUIFrame 
@File    ：BasePage.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 9:58 
@explain ：浏览器页面查找元素 显示等待
"""
import logging

from selenium.webdriver.support.wait import WebDriverWait

from utils.WebDriverUtil import DriverUtils


class BasePage:

    def __init__(self):
        self.driver = DriverUtils.get_driver()

    def get_element(self, element, timeout=10):
        ele = WebDriverWait(self.driver, timeout, 0.5).until(lambda driver: driver.find_element(*element))
        logging.info("element = {}".format(element))
        return ele


