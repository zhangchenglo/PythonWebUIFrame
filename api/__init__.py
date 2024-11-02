"""
@Project ：PythonWebDriverUIFrame 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 9:58 
@explain ：
"""
import logging
import time

from conftest import init_log_config
from utils import ReadEnvParamsUtil

SYSTEM_URL = ReadEnvParamsUtil.get_env_params("BASE_URL")

init_log_config()
logging.info("log at {}".format(time.strftime('%Y-%m-%d %H:%M:%S')))