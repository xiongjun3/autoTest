import requests

from utils.logger_util import logger


class BaseApi:
    def __init__(self):
        pass

    def send(self, method, url, tool, **kwargs):
        # **kwargs不限制长度的健值对传参
        # 判断tool，如果tool是requests，就是用requests来发送请求
        if tool == "requests":
            data = {
                "method": method,
                "url": url
            }
            # 把可变关键字传递更新到字典中
            data.update(kwargs)
            logger.info(kwargs)
            # 调用requests的接口发起请求，并把参数传递进去
            res = requests.request(**data)
            logger.info(res.text)
            return res
        else:
            return True



