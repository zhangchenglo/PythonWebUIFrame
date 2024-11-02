"""
@Project ：PythonWebDriverUIFrame 
@File    ：ScreenShotUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:14 
@explain ：截图工具类 并添加到 allure 报告当中
"""
import allure

from utils.WebDriverUtil import DriverUtils

"""
通过调用 allure 自带的attach方法 进行自动化结果的截图
"""


def screen_shot(screen_shot_name):
    """
    :param screen_shot_name: 截图名称
    :return: 返回allure截图
    """
    allure.attach(DriverUtils.get_driver().get_screenshot_as_png(), screen_shot_name, allure.attachment_type.PNG)

