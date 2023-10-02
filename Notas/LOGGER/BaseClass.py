import inspect
import logging


class BaseLoginClass:

    def get_logger(self):
        loggerName = inspect.stack()[1][3] # Nos sirve para obtener el nombre de las funciones que llaman la funcion del logger que estan por fuera de la clase
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
