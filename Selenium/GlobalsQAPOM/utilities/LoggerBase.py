# In utilities/LoggerBase.py
import logging
import inspect
import os

class LoggerBase:
    logger = None

    @classmethod
    def getLogger(cls):
        if cls.logger is None:
            log_dir = './logfiles'
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            logger_name = inspect.stack()[1][3]
            logger = logging.getLogger(logger_name)
            if not logger.handlers:
                file_handler = logging.FileHandler(os.path.join(log_dir, 'logfile.log'))
                formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
                logger.setLevel(logging.INFO)
            cls.logger = logger
        return cls.logger
