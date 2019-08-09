"pytest的用例编写"
import requests
import pytest

from mysql_test import DB
db =DB()
# db.execute('select * from user')

@pytest.mark.p0
@pytest.mark.login
@pytest.mark.api_test
# def test_login1():
#     ###数据准备
#     db.execute('insert into user vaules("337873969","张易发","e10adc3949ba59abbe56e057f20f883e")')
#     url = "http://115.28.108.130:5000/api/user/login/"
#     data = {
#         "name":"张易发",
#         "password":"123456"
#     }
#     res = requests.post(url = url,data = data)
#     assert 200 == res.ststus_code
#     assert "登陆成功" in res.text

# class TestLogin(object):
#     def test_login1(self):
#     url1 = "http://115.28.108.130:5000/api/user/login/"
#     data = {
#         "name":"张三",
#         "password":"123456"
#     }
#     res = requests.post(url = url1,data = data)
#     assert 200 == res.ststus_code
#     assert "登陆成功" in res.text
#
#     def test_login2(self):
#     url2 = "http://115.28.108.130:5000/api/user/login/"
#     data = {
#         "name":"李四",
#         "password":"123456"
#     }
#     res = requests.post(url = url2,data = data)
#     assert 200 == res.ststus_code
#     assert "登陆成功" in res.text


############注册接口################
def test_zhuce():
    db.execute('delete from user where name = "张易发" ')       ######数据准备
    url = "http://115.28.108.130:5000/api/user/reg"
    data = {
        "name":"张易发",
        "password":"123456"
    }
    res = requests.post(url = url, json = data)
    db.execute('insert into user values(112233,"张易发","e10adc3949ba59abbe56e057f20f883e") ')
    result = db.execute('select * from user where name ="张易发" ')
    print (result)
    assert "张易发" in result[0][1]                 #######数据库断言
    db.execute('delete from user where name="张易发" ')        #######数据清理
    ##db.close()                   放开之后会报错
test_zhuce()





