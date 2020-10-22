# coding=utf-8
import os
import sys

sys.path.append(os.path.split(os.getcwd())[0])
import time, unittest, HTMLTestRunner
from selenium import webdriver
from PageObject.book_page import BookPage
from PageObject.order_page import OrderPage
from PageObject.search_page import SearchPage
from Common.function import config_url
from Common.excel_data import read_excel
from Common.function import project_path


class logingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_excel(project_path() + 'Data/testdata.xlsx', 0)
        cls.driver = webdriver.Chrome()
        cls.driver.get(config_url())
        cls.driver.maximize_window()

    def test_02(self):
        # self.driver.get("")
        search = SearchPage(self.driver)
        # date_start = datetime.datetime.strptime(self.data.get(1)[2], '%Y-%m-%d').date()
        print(self.data.get(1)[0])
        print(self.data.get(1)[1])
        print(self.data.get(1)[2])
        res = search.search_train(self.data.get(1)[0], self.data.get(1)[1], self.data.get(1)[2])
        self.assertIn('trainBooking', res)

    def test_03(self):
        book = BookPage(self.driver)
        res = book.book()
        self.assertIn('trainBooking', res)

    def test_04(self):
        order = OrderPage(self.driver)
        res = order.user_info(self.data.get(1)[3], self.data.get(1)[4], self.data.get(1)[5])
        self.assertIn("inputPassengers", res)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(logingTest("test_02"))
    suiteTest.addTest(logingTest("test_03"))
    suiteTest.addTest(logingTest("test_04"))

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    file_path = project_path() + "/Reports/" + now + '.html'
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试报告')
    runner.run(suiteTest)
    print(file_path)
    fp.close()