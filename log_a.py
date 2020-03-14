import logging


logging.basicConfig(level=logging.INFO,
                    format='levelname:%(levelname)s filename: %(filename)s '
                           'outputNumber: [%(lineno)d]  thread: %(threadName)s output msg:  %(message)s'
                           ' - %(asctime)s', datefmt='[%d/%b/%Y %H:%M:%S]',
                    filename='./loggmsg.log') #设置日志的输出样式


logging.info("hi,leon")