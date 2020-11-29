# -*- coding:utf-8 -*-
# @Time    : 2020/11/29 17:27
# @Author  : xiangxuan
import pytest


# 测试相等
def test_add():
    assert 3 + 4 == 7


# 测试不相等
def test_add2():
    assert 27 + 22 != 50


# 测试大于等于
def test_add3():
    assert 27 + 22 <= 50


# 测试小于等于
def test_add4():
    assert 27 + 22 >= 50


# 测试大于
def test_add5():
    assert 27 + 22 < 50


# 测试小于
def test_add6():
    assert 27 + 22 > 50


def test_in():
    a = "hello world"
    b = "he"
    assert b in a


# 测试不相等
def test_not_in():
    a = "hello world"
    b = "hi"
    assert b not in a


if __name__ == '__main__':
    pytest.main(["-s"])
