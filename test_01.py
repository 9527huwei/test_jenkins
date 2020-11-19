# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 ����10:10
# @Author  : WangJuan
# @File    : test_case.py
import allure
import pytest


@allure.feature('test_module_01')
@allure.story('test_story_01')
@pytest.mark.normal
def test_case_01():
    """
    Test case 01
    """
    assert 0


@allure.feature('test_module_01')
@allure.story('test_story_02')
@pytest.mark.critical
def test_case_02():
    """
    Test case 02
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])