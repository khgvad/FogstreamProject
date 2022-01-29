from abc import ABCMeta, abstractmethod
from typing import Union


class ITextEncryptor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def encrypt(self, message: str, key) -> str:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, message: str, key) -> str:
        raise NotImplementedError
