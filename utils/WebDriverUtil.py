"""
@Project ：PythonWebDriverUIFrame 
@File    ：WebDriverUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:15 
@explain ：封装浏览器驱动对象
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from api import SYSTEM_URL


class DriverUtils:
    _driver = None

    """
    This is a method about get WebDriver.

    """

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            # cls._driver = webdriver.Chrome()
            # 使用这段代码可以自动下载浏览器驱动 无需手动更新
            # 使用了第三方库 webdriver_manager 安装：pip install webdriver_manager
            # cls._driver = webdriver.Chrome(ChromeDriverManager().install())
            cls._driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            cls._driver.maximize_window()
            # 获取 env 中的 值
            cls._driver.get(SYSTEM_URL)
        return cls._driver

    """
    This is a method about quit WebDriver.
    """

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls.get_driver().quit()
            cls._driver = None


