import time
from typing import List
import pytest

# 转换yaml文件里的中文编码，不显示乱码
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 日志文件按时间命名，自动生成
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    # rootdir根路径
    # 首选会找pytest.ini的路径
    # 其次会找朋友conftest.py的路径
    # 如果上面两个路径都没有用rootdir就会报错
    # 也可以用os.path.dirname(__file__)
    rootdir = request.config.rootdir
    log_name = rootdir + '_output/log_/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)