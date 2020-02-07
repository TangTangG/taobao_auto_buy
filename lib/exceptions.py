class SystemUnsupported(Exception):

    def __init__(self):
        message = "Didn't support your system"
        super().__init__(message)

class SubClassInvaild(Exception):

    def __init__(self):
        message = "SubClass didn't provide needed function"
        super().__init__(message)

class InvalidInputUrl(Exception):

    def __init__(self):
        message = "Input url is not valid"
        super().__init__(message)

class InvalidInputTime(Exception):

    def __init__(self):
        message = "Input time is not valid"
        super().__init__(message)
