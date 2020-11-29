# -*- coding:utf-8 -*-
# @Time    : 2020/11/29 16:34
# @Author  : xiangxuan

import pytest


def setup_module(module):
    """
    module级别的setup，它会在本module(test.py)里
    所有test执行之前，被调用一次。
    注意，它是直接定义为一个module里的函数
    """
    print("#### setup before module")


def teardown_module(module):
    """
    module级别的teardown，它会在本module(test.py)里
    所有test执行完成之后，被调用一次。
    注意，它是直接定义为一个module里的函数
    """
    print("#### teardown after module")


def setup_function(function):
    """
    功能函数的始末
	每一个函数方法前
    """
    print("#### setup_function")


def teardown_function(function):
    """
    功能函数的始末
	每一个函数方法后
    """
    print("#### teardown_function")


def test_case001():
    assert 1 == 1
    print("#### test_case001")


def test_case002():
    assert 1 == 1
    print("#### test_case002")


# 注意以类方法形式编写用例时，请不要带__init__方法
class TestSohu(object):

    @classmethod
    def setup_class(cls):
        """
        class级别的setup函数，它会在这个测试类TestSohu里
        所有test执行之前，被调用一次.
        注意它是一个@classmethod
        """
        print("~~~~ setup before class TestSohu")

    @classmethod
    def teardown_class(cls):
        """
       class级别的teardown函数，它会在这个测试
       类TestSohu里所有test执行完之后，被调用一次.
       注意它是一个@classmethod
       """

        print("~~~~ teardown after class TestSohu")

    def setup_method(self, method):
        """
        这是一个method级别的setup函数，它会在这个测试
        类TestSohu里，每一个test执行之前，被调用一次.
        """
        print("~~~~ setup before each method")

    def teardown_method(self, method):
        """
        这是一个method级别的teardown函数，它会在这个测试
        类TestSohu里，每一个test执行之后，被调用一次.
        """
        print("~~~~ teardown after each method")

    def test_login(self):
        assert True == True
        print("~~~~ test_login")

    def test_logout(self):
        assert True == True
        print("~~~~ test_logout")


if __name__ == '__main__':
    pytest.main(['-s'])
