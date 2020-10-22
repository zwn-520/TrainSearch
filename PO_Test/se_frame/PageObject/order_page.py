# coding=utf-8
from selenium.webdriver.common.by import By
import time, sys

sys.path.append(r'D:\PythonSeleniumTest\PO_Test\se_frame\Base')
from base import Base


class OrderPage(Base):
    # 填写姓名
    def detail_name(self):
        time.sleep(2)
        return self.findele(By.CSS_SELECTOR, "#inputPassengerVue > div.pasg-add > ul > li:nth-child(2) > input")

    # 身份证
    def detail_uid(self):
        time.sleep(1)
        return self.findele(By.CSS_SELECTOR, "#inputPassengerVue > div.pasg-add > ul > li:nth-child(3) > input")

    # 手机号
    def detail_phone(self):
        time.sleep(1)
        return self.findele(By.CSS_SELECTOR, "#inputPassengerVue > div.pasg-add > ul > li:nth-child(6) > input")

    def user_info(self, name, uid, phone):
        time.sleep(3)
        self.detail_name().send_keys(name)
        self.detail_uid().send_keys(uid)
        self.detail_phone().send_keys(phone)
        time.sleep(3)
        return self.url()
