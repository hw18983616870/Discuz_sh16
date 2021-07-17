"""
============================
@auther:多测师-黄sir
@time:2021/7/15:15:55
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
import unittest
from public.page.BasePage import BasePage
from public.page.Bbs_Set_Element import *
class Bbs_Setting(unittest.TestCase):
    def test_bbs_seting(self):
        # 点击设置按钮
        BasePage().find_ele(setting_ele)
        BasePage().ele_click()
        #验证页面跳转成功
        BasePage().find_ele(assert_ele)
        value = BasePage().get_text()
        assert value == '修改头像'
