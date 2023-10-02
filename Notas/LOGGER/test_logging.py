import logging


def test_logginDemo():
    # Esta línea crea un objeto logger personalizado utilizando el nombre del módulo como nombre del logger. Esto es
    # útil porque te permite identificar de manera única la fuente de los registros.
    logger = logging.getLogger(__name__)

    # Creacion del objeto que manejara el archivo de logs a generar
    filehandler = logging.FileHandler("logfile.log")

    # Formato del texto generado en el archivo de logs DateTime : TipoError : nombreMetodo : Mensaje personalizado
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    # Se establece el formato en el objeto que manejara el archivo
    filehandler.setFormatter(formatter)

    # Manejador del archivo
    logger.addHandler(filehandler)

    # Podemos establecer desde que nivel queremos que se imprima en los logs
    logger.setLevel(logging.INFO)

    # Mensajes personalizados por cada resultado de la ejecuccion
    logger.debug("Ejecutandose el debug")
    logger.info("Estado de informacion")
    logger.warning("Estado de alerta")
    logger.error("Estado de error")
    logger.critical("Estado critico")
