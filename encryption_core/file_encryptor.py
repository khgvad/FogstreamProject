from .i_text_encryptor import ITextEncryptor
from .encryptor_caption_mapping import EncryptorCaptionMapping
from exception_processor import ExceptionProcessor
from logger import main_logger
from collections.abc import Iterable


class FileEncryption:

    @staticmethod
    def __file_get_contents(path: str, encoding_: str = 'utf-8') -> Iterable[str]:
        with open(path, 'r', encoding=encoding_) as enc_file:
            read_text = enc_file.readlines()
        return read_text

    @staticmethod
    def __file_put_contents(lines: Iterable[str], path: str, encoding_: str = 'utf-8') -> None:
        with open(path, 'w', encoding=encoding_) as enc_file:
            text_to_write = ''.join(lines).rstrip("\n")
            enc_file.write(text_to_write)

    @staticmethod
    def __encrypt_lines(lines: Iterable[str], encryptor: ITextEncryptor, key) -> Iterable[str]:
        encrypted_lines = []

        for line in lines:
            stripped_str = line.strip("\n")
            encrypted_str = encryptor.encrypt(stripped_str, key)
            encrypted_lines.append(encrypted_str + "\n")

        return encrypted_lines

    @staticmethod
    def __decrypt_lines(lines: Iterable[str], encryptor: ITextEncryptor, key) -> Iterable[str]:
        decrypted_lines = []

        for line in lines:
            stripped_str = line.strip("\n")
            decrypted_str = encryptor.decrypt(stripped_str, key)
            decrypted_lines.append(decrypted_str + "\n")

        return decrypted_lines

    @staticmethod
    def encrypt_file(path: str, encryptor: ITextEncryptor, key, encoding_: str = 'utf-8') -> None:

        encryptor_type = type(encryptor).__name__
        encryptor_caption = EncryptorCaptionMapping.get_caption(encryptor_type)
        main_logger.print_info(f"Encryption started. Type: {encryptor_caption}")

        try:
            read_lines = FileEncryption.__file_get_contents(path, encoding_)
            strings_to_write = FileEncryption.__encrypt_lines(read_lines, encryptor, key)
            FileEncryption.__file_put_contents(strings_to_write, path, encoding_)

        except Exception as ex:
            ex_message = ExceptionProcessor.get_exception_message(ex, "Encryption failed")
            main_logger.print_error(ex_message)
            raise

        main_logger.print_info("Encryption completed succesfully!")

    @staticmethod
    def decrypt_file(path: str, encryptor: ITextEncryptor, key, encoding_: str = 'utf-8') -> None:
        encryptor_type = type(encryptor).__name__
        encryptor_caption = EncryptorCaptionMapping.get_caption(encryptor_type)
        main_logger.print_info(f"Decryption started. Type: {encryptor_caption}")

        try:
            read_lines = FileEncryption.__file_get_contents(path, encoding_)
            strings_to_write = FileEncryption.__decrypt_lines(read_lines, encryptor, key)
            FileEncryption.__file_put_contents(strings_to_write, path, encoding_)

        except Exception as ex:
            ex_message = ExceptionProcessor.get_exception_message(ex, "Decryption failed")
            main_logger.print_warning(f"Decryption failed: {ex_message}")
            raise

        main_logger.print_info("Decryption completed succesfully!")
