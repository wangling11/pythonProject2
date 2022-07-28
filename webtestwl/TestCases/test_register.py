# -- coding: utf-8 --
# @Time : 2022/7/15 17:37
# @Author : wangling
# @Email : 731569578@qq.com
# @File : test_register.py
# @Software: PyCharm
import os
import unittest

from webtestwl.Common.myddt import ddt,data
from webtestwl.Common.do_excel import Do_Excel
from webtestwl.Common.do_path import datas_dir
from webtestwl.Common.my_logger import logger
from webtestwl.Common.do_config import conf;
from webtestwl.Common.do_requests import send_requests;
from webtestwl.Common.handle_phone import get_new_phone;
from webtestwl.Common.handle_data import replace_mark_with_data
from webtestwl.Common.handle_db import HandleDB;

filename = os.path.join(datas_dir, "api_cases.xlsx")
base_url = conf.get("server", "base_url")
# os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger.info("******测试用例的名称：{}********测试的地址：{}************".format(filename, base_url))
exc = Do_Excel(filename, "注册1");
cases = exc.read_all_datas()
logger.info("******测试数据：{}************".format(cases))
exc.close_file()
db = HandleDB();


@ddt
class Test_Register(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  注册模块用例 开始执行  ========")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  注册模块用例 执行结束  ========")
    # 正常注册
    @data(*cases)
    def test_normal_register(self,case):
        #第一步：准备测试数据 1 接口地址  2 请求方法 3 请求头 4 请求数据 6 用例预期结果
        logger.info("*********   执行用例{}：{}   *********".format(case["id"], case["title"]))
        # 替换 - 动态 -
        # 请求数据 #phone# 替换 new_phone
        # check_sql里的  #phone# 替换 new_phone
        if case["request_data"].find("#phone#") != -1:
            new_phone = get_new_phone()
            case = replace_mark_with_data(case, "#phone#", new_phone)
        # 第二步：发送请求
        response = send_requests(case["method"],case["url"],case["request_data"],token=None)
        # 期望结果，从字符串转换成字典对象。
        expected = eval(case["expected"])
        # 断言 - code == 0 msg == ok
        logger.info("用例的期望结果为：{}".format(expected))
        # 第三步：断言
        try:
            self.assertEqual(response.json()["code"], expected["code"])
            self.assertEqual(response.json()["msg"], expected["msg"])
            if case["check_sql"]:
                result = db.select_one_data(case["check_sql"]);
                self.assertIsNotNone(result);
        except AssertionError:
            logger.exception("断言失败！")
            raise
        logger.info("*********   执行完毕{}*********")

