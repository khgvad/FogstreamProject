from encryption_core import CaesarTextEncryptor
from exception_processor import ExceptionProcessor
from logger import main_logger


class CaptionTypeBinding:

    __binding = {
        'CaesarCipher': CaesarTextEncryptor
    }

    @staticmethod
    def get_type(caption: str):
        try:
            return CaptionTypeBinding.__binding[caption]
        except KeyError as ex:
            message = ExceptionProcessor.get_exception_message(ex, "Caption key not found!")
            main_logger.print_error(message)
            raise
