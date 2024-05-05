


class MadUserException(ValueError):
    def __init__(self, message=None, *args):
        super().__init__(*args)
        self.message = message
