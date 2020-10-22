# encoding=utf-8
import unittest
import HTMLTestRunner
import time,sys
sys.path.append(r'D:\PythonSeleniumTest\PO_Test\se_frame\Common')
from function import project_path

if __name__ == '__main__':
    test_dir = project_path()+"TestCases"
    tests = unittest.defaultTestLoader.discover(test_dir, pattern='Test*.py', top_level_dir=None)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    file_path = project_path()+"/Reports/"+now+'.html'
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试报告')
    runner.run(tests)
    fp.close()
