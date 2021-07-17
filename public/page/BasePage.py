"""
============================
@auther:多测师-黄sir
@time:2021/7/15:11:12
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
#此模块主要用于封装UI页面 元素操作的所有方法
#以下代码用于调试数据使用
# from selenium import webdriver
# driver = webdriver.Chrome()
class BasePage:

    # 单例模式
    @classmethod
    def set_driver(cls,driver):
        cls.driver = driver

    @classmethod
    def get_driver(cls):
        return cls.driver
    '''封装定位页面元素的方法'''
    @classmethod
    def find_ele(cls,element):
        # element = ('id','kw')
        type = element[0]
        value = element[1]
        if type == 'id':
            cls.ele = cls.driver.find_element_by_id(value)
        elif type == 'name':
            cls.ele = cls.driver.find_element_by_name(value)
        elif type == 'class':
            cls.ele = cls.driver.find_element_by_class_name(value)
        elif type == 'xpath':
            cls.ele = cls.driver.find_element_by_xpath(value)
        elif type == 'css':
            cls.ele = cls.driver.find_element_by_css_selector(value)
        elif type == 'link':
            cls.ele = cls.driver.find_element_by_link_text(value)

    '''封装元素输入的方法'''
    def sendkeys(self,value):
        self.ele.send_keys(value)
    '''封装元素点击的方法'''
    def ele_click(self):
        self.ele.click()
    '''封装窗口最大化的方法'''
    def max_window(self):
        self.driver.maximize_window()
    '''封装隐式等待的方法'''
    def wait_ele(self,sec):
        self.driver.implicitly_wait(sec)
    '''获取页面元素的文本值'''
    def get_text(self):
        return self.ele.text

if __name__ == '__main__':
    b = BasePage()
    b.set_driver(driver)
    driver = b.get_driver()
    driver.get("http://www.baidu.com")
    b.wait_ele(20)
    b.max_window()
    baidu_input = ('id','kw')
    b.find_ele(baidu_input)
    b.sendkeys('python')
    baidu_butten = ('id','su')
    b.find_ele(baidu_butten)
    b.ele_click()









