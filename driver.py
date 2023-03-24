from selenium import webdriver

# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Program Files\Google\Chrome\Application\chrome.exe"

class Driver:
    _driver = None

    @classmethod
    def driver_handle(cls, browser='chrome'):
        if cls._driver is None:
            if browser == 'chrome':
                opt = webdriver.ChromeOptions()
                opt.debugger_address = '127.0.0.1:9222'
                cls._driver = webdriver.Chrome(options=opt)
            elif browser == 'firefox':
                cls._driver = webdriver.Firefox()
            else:
                raise '无此浏览器'

        return cls._driver
