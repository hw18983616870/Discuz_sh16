"""
============================
@auther:多测师-黄sir
@time:2021/7/15:10:09
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
# 此模块是用来专门读取ini配置文件的
from config.Config import *
from configparser import ConfigParser
class ReadDataIni(ConfigParser):
    def __init__(self,filename):
        super(ConfigParser, self).__init__()
        self.read(filename)

    def read_data(self,section,option):
        return self.get(section=section,option=option)
filename = os.path.join(data_path,'Data.ini')
# print(filename)
r = ReadDataIni(filename)
url = r.read_data(section='bbs_test',option='url')
# print(url)
username = r.read_data(section='bbs_test',option='username')
# print(username)
pwd = r.read_data(section='bbs_test',option='pwd')
# print(pwd)

# --------------------------------------------------------------------
url1 = r.read_data(section='bbs_test1',option='url')
# print(url1)