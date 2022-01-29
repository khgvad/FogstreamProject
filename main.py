from user_interaction import EncryptionSimpleGui, UiLocale


class Main:
    @staticmethod
    def main():

        eg = EncryptionSimpleGui(UiLocale.RU)
        eg.start()


Main.main()
