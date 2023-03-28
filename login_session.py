from selenium import webdriver
from time import sleep
from utils.handle_yaml import write_yaml
from config.base_config import cookies_url


def write_cookies():
    driver = webdriver.Chrome()
    driver.get(cookies_url)
    sleep(40)
    cookies = driver.get_cookies()
    write_yaml(r'config/cookies.yaml', cookies)



if __name__ == '__main__':
    write_cookies()
    # use_cookies()
