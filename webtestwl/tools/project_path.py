# -- coding: utf-8 --
# @Time : 2022/5/27 16:06
# @Author : wangling
# @Email : 731569578@qq.com
# @File : project_path.py
# @Software: PyCharm
import  os;
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0];
#测试用例的路径
test_case_path = os.path.join(project_path,'test_data','test_data.xlsx');
# 测试报告的路径
test_report_path = os.path.join(project_path,'test_result','html_report','test_api.html');