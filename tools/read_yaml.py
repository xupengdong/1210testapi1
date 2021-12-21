# -*- coding:utf-8 -*-
# @Time  : 2021/12/20 15:50
# @Author: xupd
# @File  : read_yaml.py
# @Date : 2021/7/30 11:02
"""
为了不是服务于一个yaml文件，可以将路劲设置为通用的路径，需要将config.py中的项目路径引用过来
"""
import yaml
# 定义函数
from config import BASE_PATH
import os


def read_yaml(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    # 创建空的列表，组装测试数据
    arr = []
    # 打开文件（获取文件流）
    with open(file_path,'r',encoding="utf-8") as f:

        # 调用yaml.safe_load（f）.value()获取文件流内容,需要遍历取出
        for datas in yaml.safe_load(f).values():
            # datas.values()是列表里字典形式，需要将起转换成列表或元组
            arr.append(tuple(datas.values()))

    return arr

    # 返回结果
if __name__ == '__main__':
    print(read_yaml("crd_login.yaml"))
