from typing import Union


class Auxiliary:

    @staticmethod
    def rotate_right(rotating_list: Union[list, str], shift: int) -> list:
        rotating_list = rotating_list[-shift:] + rotating_list[:-shift]
        return rotating_list

    @staticmethod
    def rotate_left(rotating_list: Union[list, str], shift: int) -> list:
        return Auxiliary.rotate_right(rotating_list, -shift)

    @staticmethod
    def str_to_byte_list(text: str, encoding: str = 'utf-8') -> list[int]:
        return list(bytes(text, encoding))

    @staticmethod
    def byte_list_to_str(bytes_list: list[int], encoding: str = 'utf-8') -> str:
        _bytes = bytes(bytes_list)
        return _bytes.decode(encoding)

