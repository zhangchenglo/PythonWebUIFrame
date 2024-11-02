"""
@Project ：PythonWebDriverUIFrame 
@File    ：ReadEnvParamsUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:06 
@explain ：读取系统 .env 文件参数 value 值
"""
import os

from dotenv import load_dotenv

# 安装方式 pip install python-dotenv


def get_env_params(params):
    load_dotenv()  # 加载env变量
    return os.environ.get(params)