import pymysql

from utils.logger_util import logger


def query_db(sql):
    # 建立数据库链接
    conn = pymysql.Connect(host="rds.nonprod.iglooinsure.com", port=3306, database="uic_eb_qa", user="uic_eb_qa",
                           password="vD9jQxPbmw8ofjKEbN2G6wJi", charset="utf8")
    # 建立游标
    cursor = conn.cursor()
    # 使用游标执行SQL
    cursor.execute(sql)
    # 存储查询的数据
    datas = cursor.fetchall()
    logger.info(f"获取数据的行数{cursor.rowcount}")
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # 返回查询的数据
    return datas





