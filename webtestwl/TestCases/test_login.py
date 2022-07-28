# -- coding: utf-8 --
# @Time : 2022/5/26 16:45
# @Author : wangling
# @Email : 731569578@qq.com
# @File : test_login.py
# @Software: PyCharm
import unittest
from webtestwl.Common.do_requests import send_requests;
from webtestwl.Common.do_excel import Do_Excel;
from webtestwl.Common.do_path import datas_dir;
from webtestwl.Common.handle_db import HandleDB;
from webtestwl.Common.myddt import ddt,data;
from webtestwl.Common.my_logger import logger;
from webtestwl.Common.handle_phone import get_new_phone,get_exit_phone;
from webtestwl.Common.handle_data import replace_mark_with_data,clear_EnvData_attrs;

he = Do_Excel(datas_dir +"\\api_cases.xlsx","登陆1")
cases = he.read_all_datas();
he.close_file();
db = HandleDB();
@ddt
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  登陆模块用例 开始执行  ========")
        # 清理 EnvData里设置的属性
        clear_EnvData_attrs();

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  登陆模块用例 执行结束  ========")
    #正常登陆
    @data(*cases)
    def test_normal_login(self,case):
        # 输入用户名 密码  调用接口 发送请求 然后断言 返回来的数据是否正确
        # 第一步：准备测试数据 1 接口地址  2 请求方法 3 请求头 4 请求数据 6 用例预期结果
        logger.info("*********   执行用例{}：{}   *********".format(case["id"], case["title"]))
        logger.info("*********   执行用例{}：{}  的请求数据为{} *********".format(case["id"], case["title"], case["request_data"]))
        # 替换 - 动态 -
        # 请求数据 #phone2# 替换 new_phone  生成新的手机号但是没有注册过的手机号  #phone# 替换 成配置文件里面指定的用户名 密码
        print(case["request_data"].find("#phone#"))
        if case["request_data"].find("#phone#") != -1:
            new_phone = get_exit_phone();
            logger.info("得到的手机号码为{}".format(new_phone))
            case = replace_mark_with_data(case, "#phone#", new_phone)
        elif case["request_data"].find("#test#") != -1:
            new_phone = get_new_phone()
            check_sql = "select * from member where mobile_phone=\'%s\'" %(new_phone);
            result = db.get_count(check_sql);
            while result == 1:
                new_phone = get_new_phone();
                check_sql = "select * from member where mobile_phone=\'%s\'" % (new_phone);
                result = db.get_count(check_sql);
            case = replace_mark_with_data(case, "#test#", new_phone)

        response = send_requests(case["method"],case["url"],case["request_data"]);
        # 期望结果，从字符串转换成字典对象。
        expected = eval(case["expected"]);
        # 断言 - code == 0 msg == ok
        logger.info("用例的期望结果为：{}".format(expected))
        logger.info("用例的sql为：{}".format(case["check_sql"]))
        # 第三步：断言
        try:
            self.assertEqual(response.json()["code"], expected["code"])
            self.assertEqual(response.json()["msg"], expected["msg"])
        except AssertionError:
            logger.exception("断言失败！")
            raise
        logger.info("*********   执行完毕{}*********")









# if __name__ == '__main__':
#     #requests_data = {"mobile_phone": "13592527751", "pwd": "1234567809"}
#     requests_data = {"mobile_phone": "13592527751", "pwd": "123456789"}
#     url = "/member/login";
#     result_data = send_requests("post",url,requests_data)
#     print(result_data.json())
#     #{"code“: 1001, "msg": "账号信息错误"}
#    # data = {'id': 13, 'title': '不输入类型', 'method': 'post', 'url': '/member/register', 'request_data': '{"mobile_phone":"#phone#","pwd":"12345678"}', 'expected': '{"code":0,"msg":"OK"}', 'check_sql': 'select * from member where mobile_phone="#phone#"'};
