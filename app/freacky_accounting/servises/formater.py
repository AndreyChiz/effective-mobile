from config import root_logger as logger
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class Formater:

    def __init__(self, *args, **kwargs):
        logger.info("formater initialized")
