"""
============================
@auther:多测师-黄sir
@time:2021/7/15:14:03
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
from public.page.BasePage import BasePage
from public.utils.ReadDataIni import *
from selenium import webdriver
from time import sleep
import unittest
from public.page.Bbs_Login_Element import *
class Bbs_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        driver = webdriver.Chrome()
        BasePage().set_driver(driver)
        cls.dr = BasePage().get_driver()
        BasePage().wait_ele(20)
        BasePage().max_window()
        cls.dr.get(url)
    def test_login(self):
        '''输入用户名'''

        BasePage().find_ele(login_username)
        BasePage().sendkeys(username)
        '''输入密码'''

        BasePage().find_ele(login_pwd)
        BasePage().sendkeys(pwd)
        '''点击登录'''

        BasePage().find_ele(login_button)
        BasePage().ele_click()
        '''断言'''
        sleep(3)

        BasePage().find_ele(assert_ele)
        value = BasePage().get_text()
        assert value == '设置'

if __name__ == '__main__':
    b = Bbs_Login()
    b.test_login()






