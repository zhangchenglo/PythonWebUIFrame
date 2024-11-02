"""
@Project ：PythonWebDriverUIFrame 
@File    ：OcrVerifyCodeUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:19 
@explain ：使用人工智能识别技术 ocr 识别验证码 使用到第三方库：ddddocr
"""
import ddddocr

"""

利用ocr识别技术进行验证码的简单识别 有错误率  

"""


def util_verify_code(ele_png):

    ocr = ddddocr.DdddOcr()
    verify_code = ocr.classification(ele_png)  # 使用allure截图之后，将截图文件参数传入即可
    print("识别图片结果为：", verify_code)
    return verify_code
