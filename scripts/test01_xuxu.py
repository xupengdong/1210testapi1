# -*- coding:utf-8 -*-
# @Time  : 2021/12/20 14:17
# @Author: xupd
# @File  : test01_xuxu.py
import pytest

from api.api_xuxu import ApiXuXu
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
from tools.tools import Tools
log = GetLog.get_logger()

class TestXuXu:
    # 1.初始化  获取对象
    def setup_class(self):
        self.xuxu = ApiXuXu()

    # 2.登录接口测试方法
    @pytest.mark.parametrize("mobile,code",read_yaml("xuxu_login.yaml"))
    def test01_login(self,mobile,code):
        # 调用登录接口
        r = self.xuxu.api_xuxu_login(mobile,code)
        #打印输出结果
        print("登录的结果为",r.json())
        try:
            # 提取token
            Tools.common_token(r)

            # 断言
            Tools.common_assert(r)
        except Exception as e:
            # 写入日志
            log.error("获取错误日志{}".format(e))
            # 抛出异常
            raise



    # 3.发布文章接口测试方法
    def test02_article(self):

        # 1.调用发布文章接口

        # 2.提取id
        # 3.断言
