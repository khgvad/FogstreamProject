from user_interaction import EncryptionSimpleGui, UiLocale
from Cryptodome.Cipher import AES


class Main:
    @staticmethod
    def main():
        # key = b'Sixteen byte key'
        # cipher = AES.new(key, AES.MODE_EAX, nonce=b"cvbdeff")
        # ciphertext, tag = cipher.encrypt_and_digest(b"hello")
        #
        # cipher1 = AES.new(key, AES.MODE_EAX, nonce=b"cvbdeff")
        # plaintext = cipher1.decrypt(ciphertext)
        # a = plaintext.decode()

        eg = EncryptionSimpleGui(UiLocale.RU)
        eg.start()


Main.main()
