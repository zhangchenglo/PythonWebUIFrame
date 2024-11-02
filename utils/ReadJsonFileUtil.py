"""
@Project ：PythonWebDriverUIFrame 
@File    ：ReadJsonFileUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:12 
@explain ：读取本地 Json 数据工具类
"""
import json


def get_data(filepath):
    """
    :param filepath: json文件路径
    :return: 返回list集合
    """
    # 创建一个空列表 用于存储数据
    list_data = []
    # 调用with open 方法打开本地文件
    # with open 方法不用手动去关闭流
    with open(filepath, "r", encoding="utf8") as f:
        data = json.load(f)  # 调用load方法加载本地的json文件
        for json_data in data:
            t = tuple(json_data.values())  # 取得json文件数据 将其转化为元组
            list_data.append(t)  # 将从json文件当中取得的值重新添加到空列表当中
        return list_data