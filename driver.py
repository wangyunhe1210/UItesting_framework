from selenium import webdriver


class Driver:
    _driver = None

    @classmethod
    def driver_handle(cls, browser='chrome'):
        if cls._driver is None:
            if browser == 'chrome':
                cls._driver = webdriver.Chrome()
            elif browser == 'firefox':
                cls._driver = webdriver.Firefox()
            else:
                raise '无此浏览器'

        return cls._driver
