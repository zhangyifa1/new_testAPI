####添加加油卡，作业参考test_case#############
import requests
import pytest

from mysql_test2 import DB

@pytest.mark.p0
def test_add():
    db=DB()
    db.execute('delete from cardinfo where cardNumber="zhangyifa110"')
    # db.commit()
    url = "http://115.28.108.130:8080/gasStation/process"
    json ={
    "dataSourceId": "bHRz",
    "methodId": "00A",
    "CardInfo": {
        "cardNumber": "zhangyifa110"

                }
        }
    res = requests.post(url = url ,json =json)
    print (res.text)
    db.execute('select * from cardinfo where cardNumber="zhangyifa110"')
    result = db.execute('select * from cardinfo where cardNumber="zhangyifa110"')
    # print (result)   主动关闭数据库需要调用才能执行，待验证？？？
test_add()
