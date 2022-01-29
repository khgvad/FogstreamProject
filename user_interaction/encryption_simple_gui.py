import PySimpleGUI as py_simple_gui
from singleton_meta import SingletonMeta
from encryption_core import ITextEncryptor, FileEncryption
from .i_user_interactor import IUserInteractor
from caption_type_binding import CaptionTypeBinding
from .ui_locale import UiLocale
from .lang.en import en_locale
from .lang.ru import ru_locale
from typing import Optional


class EncryptionSimpleGui(IUserInteractor, metaclass=SingletonMeta):

    def __init__(self, locale_: UiLocale = UiLocale.RU, theme: Optional[str] = "LightGray"):
        self.__window = None
        self.__theme = theme
        self.__lang_dict = self.__get_locale_dict(locale_)

    def __get_locale_dict(self, locale: UiLocale) -> dict:

        if locale == UiLocale.RU:
            return ru_locale

        return en_locale

    def __data_is_valid(self, selected_encryptor: list[str], key) -> bool:
        if len(selected_encryptor) != 1 or not key:
            return False
        return True

    def __encryption_interaction(self, path: str, encryptor: ITextEncryptor, key, encoding: str = 'utf-8'):
        try:
            FileEncryption.encrypt_file(path, encryptor, key, encoding)
            py_simple_gui.popup_ok(self.__lang_dict["SuccessfulEncryption"])
        except Exception as ex:
            py_simple_gui.popup_error(ex)

    def __decryption_interaction(self, path: str, encryptor: ITextEncryptor, key, encoding: str = 'utf-8'):
        try:
            FileEncryption.decrypt_file(path, encryptor, key, encoding)
            py_simple_gui.popup_ok(self.__lang_dict["SuccessfulDecryption"])
        except Exception as ex:
            py_simple_gui.popup_error(ex)

    def __initialize(self):
        py_simple_gui.theme('LightGray')
        locale = self.__lang_dict

        file_path_label = py_simple_gui.Text(f"{locale['FilePath']}:")
        file_path_input = py_simple_gui.InputText()

        encryption_type_values = ["CaesarCipher"]
        encryption_type_dict = {}
        encryption_type_localed = []

        for value_ in encryption_type_values:
            encryption_type_dict[locale[value_]] = value_
            encryption_type_localed.append(locale[value_])

        encryption_type_label = py_simple_gui.Text(f"{locale['EncryptionType']}:")
        encryption_type_listbox = py_simple_gui.Listbox(values=encryption_type_localed, size=(30, 3))

        key_label = py_simple_gui.Text(f"{locale['EncryptionKey']}:")
        key_input = py_simple_gui.InputText(key="-KEY-")

        encrypt_button_text = locale["EncryptButton"]
        decrypt_button_text = locale["DecryptButton"]

        encrypt_button = py_simple_gui.OK(encrypt_button_text)
        decrypt_button = py_simple_gui.OK(decrypt_button_text)

        browse_button_text = locale["BrowseButton"]
        browse_button = py_simple_gui.FileBrowse(browse_button_text)

        cancel_button_text = locale["CancelButton"]
        cancel_button = py_simple_gui.Cancel(cancel_button_text)

        layout = [[file_path_label, file_path_input],
                  [encryption_type_label, encryption_type_listbox],
                  [key_label, key_input],
                  [encrypt_button, decrypt_button,
                   py_simple_gui.Input(key='-FILE-', visible=False, enable_events=True), browse_button, cancel_button]]

        window = py_simple_gui.Window(locale["WindowTitle"], layout, finalize=True)
        self.__window = window

        while True:
            event, values = window.read()

            if event in (py_simple_gui.WIN_CLOSED, cancel_button_text):
                break
            else:
                selected_encryptor = encryption_type_listbox.get()
                key = values["-KEY-"]
                file_path = values["-FILE-"]

                if event == encrypt_button_text:
                    if self.__data_is_valid(selected_encryptor, int(key)):
                        encryptor_caption = selected_encryptor[0]
                        encryptor_type = CaptionTypeBinding.get_type(encryption_type_dict[encryptor_caption])
                        encryptor = encryptor_type()
                        self.__encryption_interaction(file_path, encryptor, key)
                    else:
                        py_simple_gui.popup_error(locale["InvalidData"])
                elif event == decrypt_button_text:
                    if self.__data_is_valid(selected_encryptor, int(key)):
                        encryptor_caption = selected_encryptor[0]
                        encryptor_type = CaptionTypeBinding.get_type(encryption_type_dict[encryptor_caption])
                        encryptor = encryptor_type()
                        self.__decryption_interaction(file_path, encryptor, key)
                    else:
                        py_simple_gui.popup_error(locale["InvalidData"])

            file_path_input.update(values["-FILE-"])

        window.close()
        self.__window = None

    def start(self):
        if self.__window is None:
            self.__initialize()
