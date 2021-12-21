# -*- coding:utf-8 -*-
# @Time  : 2021/12/20 15:10
# @Author: xupd
# @File  : tools.py

# 存放公共方法，token和断言公共
import api
class Tools:
    # 提取token
    @classmethod
    def common_token(cls,response):
        token = response.json().get("data").get("token")
        api.headers["token1"] = "xuxu "+token
    # 断言
    @classmethod
    def common_assert(cls,response,status_code=201):
        assert status_code == response.status_code
        assert "ok" == response.json().get("message")
