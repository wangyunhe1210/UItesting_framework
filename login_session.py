from selenium import webdriver
from time import sleep
import yaml


def write_yaml(file_name, datas):
    with open(file_name, 'w', encoding='utf8') as f:
        yaml.dump(datas, f)


def read_yaml(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        res = yaml.safe_load(f)
        return res


def write_cookies():
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu')
    sleep(60)
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
    # write_cookies()
    use_cookies()
