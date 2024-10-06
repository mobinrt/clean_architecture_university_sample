

class BaseError(Exception):
    message: str = 'Server Internal Error'

    def __str__(self):
        return self.message
