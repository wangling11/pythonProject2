"""
读取配置文件
"""
from configparser import ConfigParser
import os

from webtestwl.Common.do_path import conf_dir

class DoConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")

file_path = os.path.join(conf_dir, "nmb.ini")
print(file_path)
conf = DoConfig(file_path)





# if __name__ == '__main__':
#     file_path = os.path.join(conf_dir, "nmb.ini")
#     print(file_path)
#     conf = DoConfig(file_path)
#     #conf = DoConfig("nmb.ini")
#     #conf.get("log","name")
#     base_url = conf.get("server","base_url")
#     print(base_url)

