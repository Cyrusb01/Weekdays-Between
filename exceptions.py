class InvalidDate(Exception):
    def __init__(self, message="Invalid Date. This date does not exist"):
        self.message = message
        super().__init__(self.message)


class InvalidInput(Exception):
    def __init__(
        self, message="This date format is not supported. use mm/dd/y or mm-dd-y"
    ):
        self.message = message
        super().__init__(self.message)
