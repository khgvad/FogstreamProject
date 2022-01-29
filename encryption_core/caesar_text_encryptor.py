from .i_text_encryptor import ITextEncryptor
from typing import Union


class CaesarTextEncryptor(ITextEncryptor):

    def encrypt(self, message: str, key: Union[int, str]) -> str:
        if isinstance(key, str):
            key = int(key)

        result = []

        for symbol in message:

            utf_8_length = 1114111
            new_symbol = chr((ord(symbol) + key) % utf_8_length)
            result.append(new_symbol)

        return ''.join(result)

    def decrypt(self, message: str, key: Union[int, str]) -> str:
        if isinstance(key, str):
            key = int(key)

        return self.encrypt(message, -key)
