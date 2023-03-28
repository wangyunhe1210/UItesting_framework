import os

# 主路径
base_path = os.path.dirname(os.path.dirname(__file__))

# 基础路径
common_path = os.path.join(base_path, 'common')
config_path = os.path.join(base_path, 'config')
page_path = os.path.join(base_path, 'PageObject')
utils_path = os.path.join(base_path, 'utils')

# 细分路径
cookie_path = os.path.join(config_path, 'cookies.yaml')