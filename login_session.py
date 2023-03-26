from selenium import webdriver
from time import sleep
from utils.handle_yaml import read_yaml, write_yaml


def write_cookies():
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu')
    sleep(40)
    cookies = driver.get_cookies()
    write_yaml(r'./cookies.yaml', cookies)


def use_cookies():
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu')
    for cookie in read_yaml(r'./cookies.yaml'):
        driver.add_cookie(cookie)
    sleep(2)
    driver.get(r'https://work.weixin.qq.com/wework_admin/frame')
    sleep(2)
    driver.quit()


if __name__ == '__main__':
    write_cookies()
    # use_cookies()
