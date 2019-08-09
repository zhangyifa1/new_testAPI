import pytest
import requests

@pytest.mark.p0
@pytest.mark.demo
def test_1():
    assert 1 + 1 ==2

@pytest.mark.p1
@pytest.mark.demo
def test_2():
    assert 2 + 2 ==4

@pytest.mark.skip        ######无条件跳过该用例，即不执行
def test_3():
    pass

@pytest.mark.xfail       ########已知失败，即目前存在bug的用例
def test_4():
    pass

a =2
@pytest.mark.skipif(a>1,reason="功能还没开发好")
def test_5():
    pass

# data = [(1,2,3),(2,-4,2),(2,3,5),(1.1,2.2,1.1)]
# @pytest.mark.parametrize('a,b,expected',data)
# def test_add():
#     a=1
#     b=2
#     expected=3            ###expected代表期望值
#     url ='http://115.28.108.130:5000/add/?a={a}&b={b}'
#     res = requests.get(url = url)
#     assert str(expected) == res.text


######例如执行p0的用例并打印报告：pytest test_biaoqian.py -m "p0" --html=report.html