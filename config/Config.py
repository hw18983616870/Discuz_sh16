"""
============================
@auther:多测师-黄sir
@time:2021/7/15:9:25
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
# 此模块用来专门存放项目所有目录的绝对路径
import os
# 1.项目最顶层的根目录的绝对路径
path = os.path.dirname(os.path.dirname(__file__))
# print(path)      #执行结果：D:/workspace/Discuz_sh16
# 2.config包的绝对路径
config_path = os.path.join(path,'config')
# print(config_path)
# 3.page包的绝对路径
page_path = os.path.join(path,'public','page')
# print(page_path)
# 4.utils包的绝对路径
utils_path = os.path.join(path,'public','utils')
# print(utils_path)
# 5.report包的绝对路径
report_path = os.path.join(path,'report')
# 6.run包的绝对路径
run_path = os.path.join(path,'run')
# 7.testcase包的绝对路径
testcase_path = os.path.join(path,'case')
# print(testcase_path)
# 8.data包的绝对路径
data_path = os.path.join(path,'data')





