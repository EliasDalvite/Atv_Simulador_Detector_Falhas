import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler("saida.log"),
        logging.StreamHandler()
    ],
)
logger = logging.getLogger(__name__)


def loga_info(data):
    logger.info(data)


def loga_warning(data):
    logger.warning(data)


def loga_error(data):
    logger.error(data)


def loga_critical(data):
    logger.critical(data)
