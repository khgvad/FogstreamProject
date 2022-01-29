from exception_processor import ExceptionProcessor
from logger import main_logger


class EncryptorCaptionMapping:

    __captions = {
        'CaesarTextEncryptor': "Caesar Cipher"
    }

    @staticmethod
    def get_caption(encryptor_class: str) -> str:

        try:
            return EncryptorCaptionMapping.__captions[encryptor_class]
        except KeyError as ex:
            message = ExceptionProcessor.get_exception_message(ex, "Encryptor key not found!")
            main_logger.print_error(message)
            raise
