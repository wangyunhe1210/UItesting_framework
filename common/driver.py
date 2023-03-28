from selenium import webdriver
from config.base_config import cookies_url, base_url, implicitly_time_out
from utils.handle_yaml import read_yaml
from config.file_path import cookie_path


# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Program Files\Google\Chrome\Application\chrome.exe"

class Driver:
    _driver = None

    @classmethod
    def __login(cls):
        cls._driver.get(cookies_url)
        for cookie in read_yaml(cookie_path):
            cls._driver.add_cookie(cookie)
        cls._driver.get(base_url)

        return cls._driver

    @classmethod
    def get_driver(cls, browser='chrome'):
        if cls._driver is None:
            if browser == 'chrome':
                opt = webdriver.ChromeOptions()
                opt.debugger_address = '127.0.0.1:9222'
                cls._driver = webdriver.Chrome(options=opt)
            elif browser == 'firefox':
                cls._driver = webdriver.Firefox()
            else:
                raise '无此浏览器'
        cls._driver.implicitly_wait(implicitly_time_out)
        cls.__login()
        cls._driver.maximize_window()

        return cls._driver
