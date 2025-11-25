#####################################################################
#
# Project       : Data platform E-commerce
#
# File          : logger.py
#
# Description   : logger function
#
# Created       : 25 november 2025
#
# Author        : Mouloud BELLIL
#
# Email         : mouloud.bellil@outlook.fr
#
#######################################################################

import logging
from pathlib import Path


def logger(
    filepath: str, console_debug_level: int = 1, file_debug_level: int = 0
) -> logging.Logger:
    """function allowing to configure logger"""

    # define logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # remove old handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # ensure parent folder existe
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)

    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")

    # create console handler
    ch = logging.StreamHandler()

    # set log console level
    if console_debug_level == 0:
        ch.setLevel(logging.DEBUG)

    elif console_debug_level == 2:
        ch.setLevel(logging.WARNING)

    elif console_debug_level == 3:
        ch.setLevel(logging.ERROR)

    elif console_debug_level == 4:
        ch.setLevel(logging.CRITICAL)

    else:
        ch.setLevel(logging.INFO)

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # create file handler
    fh = logging.FileHandler(filepath)

    # set file log level
    if file_debug_level == 1:
        fh.setLevel(logging.INFO)

    elif file_debug_level == 2:
        fh.setLevel(logging.WARNING)

    elif file_debug_level == 3:
        fh.setLevel(logging.ERROR)

    elif file_debug_level == 4:
        fh.setLevel(logging.CRITICAL)

    else:
        fh.setLevel(logging.DEBUG)

    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


if __name__ == "__main__":
    logger(
        "/home/mouloud/Documents/projects/data_platform_e-commerce_company/logger.log"
    )
