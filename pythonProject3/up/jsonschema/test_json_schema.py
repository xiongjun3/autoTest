import json
from genson import SchemaBuilder

# 生成schema格式
from jsonschema import validate, ValidationError

from utils.logger_util import logger


def test_genson():
    # 实例化SchemaBuilder,schema构建的实例
    builder = SchemaBuilder()
    # 添加符合的json数据
    builder.add_object({
    "company_name": "company_924f249e",
    "company_id": "UIC30457668",
    "headcount": 0,
    "sales_channel": "direct_business",
    "channel_detail": "detail",
    "promotion_link": "https://sompouic.qa.axinan.com/h5/product?companyId=UIC30457668",
    "contact_info": {
        "name": "",
        "position": "",
        "mobile": "",
        "email": ""
    },
    "creator": "jun.xiong@iglooinsure.com"
    })
    # json.dump来编码JSON数据,用于处理文件
    # builder.to_schema() 转为schema类型
    print(builder.to_schema())
    # 将生成的schema放在一个文件中demo_schema.json
    json.dump(builder.to_schema(), open("demo_schema.json","w", encoding="utf-8"))



# 封装校验
def schema_validate(obj,schema):
    try:
        # 进行jsonschema的校验尝试
        # validate() 先验证自身提供的模式是否有效，再验证json数据格式是否正确
        # instance用来接收被测json，schema用来接收目标schema
        validate(instance=obj,schema=schema)
    # 抓取不同的错误进行堆栈的返回，并且定义校验的成功与否
    except ValidationError as e:
        logger.info(e.path)
        path = "-->".join(i for i in e.path)
        logger.error(f"验证出错，出错的位置是{path},出错的信息{e.message}")
        return False
    except Exception as e:
        logger.error(f"验证出错，出错的信息{e}")
        return False
    else:
        # 如果未出现错误则返回成功
        logger.info(f"校验成功")
        return True

def test_schema_validate():
    obj={
    "company_name":"company_91508b96",
    "company_id":"UIC83877119",
    "headcount":0,
    "sales_channel":"agent",
    "channel_detail":"detail",
    "promotion_link":"https://sompouic.qa.axinan.com/h5/product?companyId=UIC83877119",
    "contact_info":{
        "name":"xiongjun",
        "position":"chengdu",
        "mobile":"0123451234",
        "email":"e@qq.com"
    },
    "creator":"jun.xiong@iglooinsure.com"
}
    # json.load来解码JSON数据,用于处理文件
    # 如果JSON数据实例是无效的，则抛出 jsonschema.exceptions.ValidationError 异常
    # 如果schema模式本身是无效的，则抛出 jsonschema.exceptions.SchemaError 异常
    _schema = json.load(open("demo_schema.json", encoding="utf-8"))
    assert schema_validate(obj, schema=_schema)









