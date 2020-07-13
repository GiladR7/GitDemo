import inspect
import logging


class LogClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        Log = logging.getLogger(loggerName)
        File = logging.FileHandler('LogFile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        File.setFormatter(formatter)
        Log.addHandler(File)
        Log.setLevel(logging.INFO)
        return Log

