# encoding=utf-8

import os, configparser


# 获取项目路径
def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]
# os.path.realpath(__file__)为本文件的绝对路径：D:\PythonSeleniumTest\PO_Test\se_frame\Common\pathtest.py
# 通过切片分割，获得文件目录os.path.split(os.path.realpath(__file__))[0]：
#   D:\PythonSeleniumTest\PO_Test\se_frame\Common
# 再次通过分隔符‘C’，将 Common分开，获得上级目录 D:\PythonSeleniumTest\PO_Test\se_frame\

# 返回config.ini 文件中的 testUrl
def config_url():
    config = configparser.ConfigParser()
    config.read(project_path() + "config.ini")
    return config.get('testUrl', 'url')


if __name__ == '__main__':
    print("项目路径为：" + project_path())
    print("被测系统URL为：" + config_url())
