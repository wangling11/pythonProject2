# -- coding: utf-8 --
# @Time : 2022/7/18 20:34
# @Author : wangling
# @Email : 731569578@qq.com
# @File : runtest.py
# @Software: PyCharm
# 加载用例到测试套件
from unittestreport import TestRunner;
from webtestwl.Common.do_path import cases_dir,reports_dir;
import unittest


suite = unittest.defaultTestLoader.discover(cases_dir);
# 创建测试运行程序
# runner = TestRunner(suite)
# 2、创建一个用例运行程序
runner = TestRunner(suite,
                    tester='测试人员—王玲',
                    filename="reports测试",
                    report_dir=reports_dir,
                    title='王玲的测试报告',
                    desc='小柠檬项目测试生成的报告描述',
                    templates=1
                    );
# 运行用例，生成测试报告
runner.run()
