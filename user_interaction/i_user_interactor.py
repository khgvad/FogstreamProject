from abc import ABCMeta, abstractmethod


class IUserInteractor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        raise NotImplementedError
