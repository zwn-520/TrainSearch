# encoding=utf-8
import logging, time
import sys

sys.path.append(r'D:\PythonSeleniumTest\PO_Test\se_frame\Common')
from function import project_path


class FrameLog():
    def __init__(self, logger=None):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个 handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = project_path() + "/Logs/"
        self.log_name = self.log_path + self.log_time + 'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)
        # 定义handler 的输出格式
        formatter = logging.Formatter('[%(asctime)s %(filename)s->'
                                      '%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    # 在记录后关闭日志
    def closeLog(self, fh):
        self.logger.removeHandler(fh)  # 移除句柄
        fh.close()                     # 关闭文件

    def log(self):
        return self.logger


if __name__ == '__main__':
    lo = FrameLog()
    log = lo.log()
    log.error('error')
    log.debug("debug")
    log.info("info")
    log.critical("严重")
