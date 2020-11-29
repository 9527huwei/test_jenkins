# -*- coding:utf-8 -*-
# @Time    : 2020/11/29 17:25
# @Author  : xiangxuan

import pytest


def value():
    pa = [
        (2, 2),
        (5, 3),
        (4, 4)
    ]
    return pa


@pytest.mark.parametrize("a, b", value())
def test_01(a, b):
    print(a)
    print(b)
    assert a == b


def test_02():
    """
    这里会有一个坑，想法是测三种场景，实际第二种场景报错后不会运行第三种情况，建议使用上面的参数化方式。
    """
    x = [
        (2, 2),
        (5, 3),
        (4, 4)
    ]
    for a, b in x:
        assert a == b


# 可以在参数内使用高级用法
@pytest.mark.parametrize("a, b", [(2, 2), (5, 3), (4, 4), pytest.param(42, 42, marks=pytest.mark.xfail)])
def test(a, b):
    print(a)
    print(b)
    assert a == b


if __name__ == '__main__':
    pytest.main(['-s'])
