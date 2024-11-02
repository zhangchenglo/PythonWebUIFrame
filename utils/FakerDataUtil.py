"""
@Project ：PythonWebDriverUIFrame 
@File    ：FakerDataUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:04 
@explain ：常用数据构造
"""
import random

from faker import Faker

faker = Faker("zh-CN")


# 随机生成用户名
def faker_user_name():
    return faker.unique.name()


# 随机生成手机号
def faker_phone_number():
    return faker.unique.phone_number()


# 随机生成文本信息 max_nb_chars(最大字符长度)
def faker_random_text():
    """
    :return: 返回字符长度为 20 的随机文本
    """
    return faker.text(max_nb_chars=20, ext_word_list=None)


# 随机生成公司名称
def faker_company():
    return faker.unique.company()


# 随机生成地址/住址信息
def faker_address():
    return faker.address()


def random_generate_zero_or_one():
    """
    :return: 随机生成整数  0 或者 1
    """
    random_num = random.randint(0, 1)
    return random_num


def random_generate_true_or_false():
    """
    :return: 随机生成 True 或者 False
    """
    result = bool(random.getrandbits(1))
    return result


def faker_email():
    """
    :return: 随机生成邮箱
    """
    email = faker.unique.email()
    return email


def faker_province():
    """
    :return: 随机生成 省份
    """
    province = faker.province()
    return province


def faker_job():
    """
    :return: 随机生成职位
    """
    job = faker.job()
    return job


def faker_password():
    """
    :return: 随机密码
    length 长度
    special_chars 特殊字符
    digits 数字
    upper_case 大写
    lower_case 小写
    """
    password = faker.unique.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def faker_string():
    """
    :return: 随机生成字符串
    """
    pystring = faker.unique.pystr()
    return pystring


def faker_number():
    """
    :return: 随机生成 int 整数
    """
    pyint = faker.pyint()
    return pyint











