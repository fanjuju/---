import logging.handlers
import config

class GetLog:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 日志器设置错误级别
            cls.logger.setLevel(logging.INFO)
            # 设置格式器样式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            # 获取格式器
            fm = logging.Formatter(fmt)
            print(config.DIR_NAME)
            # 获取处理器
            tf = logging.handlers.TimedRotatingFileHandler(filename= config.DIR_NAME + '/buy/logger/test_1.log',
                                                           when='H',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8'
                                                           )
            # 在处理器中添加格式器
            tf.setFormatter(fm)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)
        return cls.logger

if __name__ == '__main__':
    GetLog().get_logger()
