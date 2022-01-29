import logging
from typing import Optional


class Logger:

    def __init__(self, log_path: str, log_format: Optional[str] = None) -> None:

        basic_format = '%(asctime)s %(levelname)s: %(message)s'
        if log_format is None:
            _format = basic_format
        else:
            try:
                _format = log_format
            except Exception as ex:
                _format = basic_format
                print(ex)

        logging.basicConfig(filename=log_path, format=_format, filemode='a+', level=logging.DEBUG)

    def print_debug(self, message: str) -> None:
        logging.debug(message)

    def print_info(self, message: str) -> None:
        logging.info(message)

    def print_warning(self, message: str) -> None:
        logging.warning(message)

    def print_error(self, message: str) -> None:
        logging.error(message)

    def print_critical(self, message: str) -> None:
        logging.critical(message)


main_logger = Logger("./logs/main.log")
