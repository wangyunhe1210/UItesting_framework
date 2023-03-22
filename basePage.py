from selenium import webdriver
from driver import Driver


class BasePage:
    def __init__(self):
        self.driver = Driver.driver_handle()
        self.login_url = 'https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu'
        self.base_url = 'https://work.weixin.qq.com/wework_admin/frame'

