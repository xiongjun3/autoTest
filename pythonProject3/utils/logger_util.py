

# 绑定logging的句柄
import logging
import os

from utils.file_tools import FileTool

# 绑定logging的句柄
logger = logging.getLogger(__name__)
# 拼接logs的文件夹
file_path = os.sep.join([FileTool.get_interface_dir(), "logs"])
if not os.path.exists(file_path):
    os.mkdir(file_path)
# 拼接log文件夹的路径和句柄
fileHandler = logging.FileHandler(filename=file_path + "/apitest.log", encoding="utf-8")
# 日志格式定义
formatter = logging.Formatter('[%(asctime)s]%(filename)s - %(funcName)s line:%(lineno)d [%(levelname)s]: %(message)s')

# 定义好格式之后，需要把格式绑定到handler上
# 文件句柄绑定格式
fileHandler.setFormatter(formatter)
# 控制台句柄的定义，实例化
streamHandler = logging.StreamHandler()
# 控制台句柄绑定格式
streamHandler.setFormatter(formatter)
# 设置生效
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
# 设置日志的级别
logger.setLevel(logging.INFO)