from selenium import webdriver
from driver import Driver
from utils.handle_yaml import read_yaml
from config.base_config import cookies_url, base_url
from config.base_config import time_out, poll_frequency
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()

    def get_element(self, locator):
        """
        显示等待的逻辑，寻找元素
        :param locator: 元素定位的方式和表达式，以元组形式传入，如（By.ID, 'kw'）
        :return:
        """
        WebDriverWait(
            driver=self.driver,
            timeout=time_out,
            poll_frequency=poll_frequency
        ).until(ec.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)



if __name__ == '__main__':
    page = BasePage()
