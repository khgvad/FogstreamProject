class ExceptionProcessor:

    @staticmethod
    def get_exception_message(ex: Exception, message: str):
        text = f'{message}: {ex}'
        return text
