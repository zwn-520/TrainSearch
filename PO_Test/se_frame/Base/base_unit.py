# conding:utf-8
import unittest
import sys
from selenium import webdriver

sys.path.append(r'D:\PythonSeleniumTest\PO_Test\se_frame\Common')
from function import config_url


class UnitBase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(config_url())
        cls.driver.maximize_window()

    def tearDown(cls):
        cls.driver.quit()
