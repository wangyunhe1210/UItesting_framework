from selenium import webdriver
from driver import Driver
from utils.handle_yaml import read_yaml


class BasePage:
    def __init__(self):
        self.driver = Driver.driver_handle()
        self.login_url = 'https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu'
        self.base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def __login(self):
        self.driver.get(self.login_url)
        for cookie in read_yaml(r'./cookies.yaml'):
            self.driver.add_cookie(cookie)
        self.driver.get(self.base_url)

        return self.driver


if __name__ == '__main__':
    page = BasePage()