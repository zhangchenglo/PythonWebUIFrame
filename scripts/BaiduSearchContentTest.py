"""
@Project ：PythonWebDriverUIFrame 
@File    ：BaiduSearchContentTest.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:49 
@explain ：测试用例 百度搜索
"""
import time

import allure
import pytest
from faker import Faker

from pages.proxypages.BaiduProxy import BaiduProxy
from utils import ScreenShotUtil
from utils.WebDriverUtil import DriverUtils


# @pytest.mark.skip("暂时跳过")
@pytest.mark.run(order=1)  # 控制测试用例执行顺序
@allure.description("这是关于百度搜索内容的测试")
class TestBaiduSearchContent:

    def setup_class(self):
        self.baidu_proxy = BaiduProxy()
        self.faker = Faker(locale="zh-CN")  # faker 造数据

    def teardown_class(self):
        DriverUtils.quit_driver()  # 退出浏览器驱动

    @allure.severity(allure.severity_level.BLOCKER)     # bug 严重等级
    def test_baidu_search_content(self):
        """
        :return: 搜索百度验证百度搜索功能 因此搜索输入内容的不合理性无关搜索功能
        """
        self.baidu_proxy.search_content(self.faker.name())   # faker.name() 随机生成用户名
        time.sleep(3)  # 强制等待 3 秒
        ScreenShotUtil.screen_shot("百度搜索内容截图")



