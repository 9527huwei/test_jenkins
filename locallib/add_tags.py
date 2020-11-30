#-*- coding:utf-8 -*-
# @Time    : 2020/11/30 7:29
# @Author  : xiangxuan


import time
import allure


def add_tag(tag_name):
    """
    添加一个标签
    :param tag_name: 标签名字
    :return:
    """
    localtime = time.asctime(time.localtime(time.time()))
    with allure.step("根据时间创建一个标签，标签名字是：" + tag_name):
        allure.attach("添加结果：成功")
