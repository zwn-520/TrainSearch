# coding=utf-8
from selenium.webdriver.common.by import By
import time, sys

sys.path.append(r'D:\PythonSeleniumTest\PO_Test\se_frame\Base')
from base import Base


class SearchPage(Base):
    def search_leave(self):
        return self.findele(By.ID, "departCityName")

    def search_arrive(self):
        return self.findele(By.ID, "arriveCityName")

    def search_date(self):
        return self.findele(By.ID, "departDate")

    def search_btn(self):
        return self.findele(By.CSS_SELECTOR, "#searchBoxTemplete > div > div.s_box > div.search_box > div > input")

    def search_current(self):
        return self.findele(By.CSS_SELECTOR, "#searchBoxTemplete > div > div.s_box > div.search_box > ul > li.current")

    def search_js(self, value):
        jsvalue = "document.getElementById('departDate').value='%s'" % value
        print(jsvalue)
        self.js2('departDate')
        self.js(jsvalue)

    def search_train(self, leave, arrive, leave_date):
        self.search_leave().send_keys(leave)
        time.sleep(2)
        self.search_arrive().send_keys(arrive)
        time.sleep(1)
        self.search_js(leave_date)
        self.search_current().click()
        time.sleep(1)
        self.search_btn().click()
        time.sleep(2)
        return self.url()


