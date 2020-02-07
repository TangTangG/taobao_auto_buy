class SystemUnsupported(Exception):

    def __init__(self):
        message = "不支持您的系统"
        super().__init__(message)

class SubClassInvaild(Exception):

    def __init__(self):
        message = "SubClass didn't provide needed function"
        super().__init__(message)

class InvalidInputUrl(Exception):

    def __init__(self):
        message = "商品链接无效, 请检查后重试"
        super().__init__(message)

class InvalidInputTime(Exception):

    def __init__(self):
        message = "抢购时间无效, 请按照格式重新输入"
        super().__init__(message)
