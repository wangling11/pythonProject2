# -- coding: utf-8 --
# @Time : 2022/7/26 18:54
# @Author : wangling
# @Email : 731569578@qq.com
# @File : test_add.py
# @Software: PyCharm
import os
import unittest
import json;
from jsonpath import jsonpath;

from webtestwl.Common.myddt import ddt,data
from webtestwl.Common.do_excel import Do_Excel
from webtestwl.Common.do_path import datas_dir
from webtestwl.Common.my_logger import logger
from webtestwl.Common.do_config import conf;
from webtestwl.Common.do_requests import send_requests;
from webtestwl.Common.handle_phone import get_new_phone,get_old_phone;
from webtestwl.Common.handle_data import replace_case_by_regular,clear_EnvData_attrs,EnvData;
from webtestwl.Common.handle_db import HandleDB;


filename = os.path.join(datas_dir, "api_cases.xlsx")
base_url = conf.get("server", "base_url")
# os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
exc = Do_Excel(filename, "加标");
cases = exc.read_all_datas()
logger.info("******测试数据：{}************".format(cases))
exc.close_file()
db = HandleDB();

"""
添加项目接口
前置条件：1 登陆  分普通用户和管理员用户
"""
class TestAdd(unittest.TestCase):
    def setUpClass(cls) -> None:
        logger.info("******测试用例的前置条件************")
        # 首先得是登录状态 然后才能加标
        # 清理 EnvData里设置的属性
        clear_EnvData_attrs()

        # 得到登陆的用户名和密码
        user, passwd = get_old_phone()
        # 登陆接口调用。
        resp = send_requests("POST", "member/login", {"mobile_phone": user, "pwd": passwd})
        # cls.member_id = jsonpath(resp.json(),"$..id")[0]
        # cls.token = jsonpath(resp.json(),"$..token")[0]
        setattr(EnvData, "member_id", str(jsonpath(resp.json(), "$..id")[0]))
        setattr(EnvData, "token", jsonpath(resp.json(), "$..token")[0])
        logger.info("======  充值模块用例 开始执行  ========")
        pass;

