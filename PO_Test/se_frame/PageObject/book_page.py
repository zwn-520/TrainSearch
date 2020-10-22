# coding=utf-8
from selenium.webdriver.common.by import By
import time, sys

sys.path.append(r'D:\PythonSeleniumTest\PO_Test\se_frame\Base')
from base import Base


class BookPage(Base):
    # 预定车票
    def book(self):
        self.findele(By.CSS_SELECTOR, "div.List-Box > div > div:nth-child(1) > div.w6 > div:nth-child(1) > a").click()
        return self.url()

    # 动车

    def book_typeID(self):
        return self.findele(By.CSS_SELECTOR, "#search_cate_vue > dl:nth-child(1) > dd:nth-child(4) > label > i")

    # 关闭浮层
    def book_close(self):
        return self.findele(By.CSS_SELECTOR, "#appd_wrap_close")

    def book_nologin(self):
        return self.findele(By.CSS_SELECTOR, "#btn_nologin")

    def book_btn(self):
        try:
            time.sleep(7)
            self.book_close().click()
            time.sleep(2)
            self.book_nologin().click()

        except:
            self.log.error("车次查询失败")
            None
        return self.url()
