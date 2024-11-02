"""
@Project ：PythonWebDriverUIFrame 
@File    ：UploadLocalFileByPywinautoUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:17 
@explain ：通过文件弹出框选择 上传本地文件 使用 Pywinauto 第三方库
"""
import time

import pywinauto

"""
 pywinauto 调取win本地软件 
 实现加载本地文件
 上传文件
"""


def upload_file_by_pywinauto(file_path):
    """
    :param file_path: 文件上传的路径
    :return:
    """
    # 使用pywinauto创建一个操作桌面窗口的对象
    app = pywinauto.Desktop()
    # 选择文件上传的窗口 窗口句柄默认为‘打开’
    dialog = app["打开"]
    # 文件上传的时间
    dialog["Edit1"].type_keys(file_path)  # 打开的文件窗口输入框元素名称 Edit1
    time.sleep(1)
    dialog["Button1"].click()  # 打开本地的文件窗口点击按钮元素名称 Button1