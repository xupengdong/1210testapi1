# -*- coding:utf-8 -*-
# @Time  : 2021/12/20 11:32
# @Author: xupd
# @File  : api_xuxu.py
# 大驼峰形式命名类名
import api
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()
class ApiXuXu:
    # 1.初始化  将域名和接口路径组合
    def __init__(self):
        self.login_url=api.host+"/login"
        log.info("正在打印登录url{}".format(self.login_url))
        self.article_url=api.host+"/article"
    # 2.登录接口
    def api_xuxu_login(self,mobile,code):
        """

        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        # 1.定义数据
        data = {"mobile": mobile, "code": code}
        # 2.请求接口
        return requests.post(url=self.api_xuxu_login,json=data,headers=api.headers)

    # 3.文章发布接口
    def api_xuxu_article(self,title,content):
        """

        :param title: 标题
        :param content: 正文
        :return: 响应对象
        """
        # 1.定义数据
        data = {"title":title,"content":content}
        # 2.请求接口
        return requests.post(url=self.api_xuxu_article,json=data,headers=api.headers)
