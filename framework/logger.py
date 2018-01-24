import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        '''
        指定保存日志的文件路径，日志级别以及调用文件
        将日志存入到指定的文件中
        :param logger:
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建handler，写入日志文件
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/' + rq + '.log'
        fh = logging.FileHandler(log_path)
        fh.level = logging.INFO

        # 创建handler, 用于输出控制台
        ch = logging.StreamHandler()
        ch.level = logging.INFO

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.formatter = formatter
        ch.formatter = formatter

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
            return self.logger
