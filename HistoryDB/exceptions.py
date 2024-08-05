from mako.exceptions import CompileException, SyntaxException

class FilterCompileException(CompileException):
    def __str__(self):
        return self.__class__.__name__ + ": " + self.message


class FilterSyntaxException(SyntaxException):
    def __str__(self):
        return self.__class__.__name__ + ": " + self.message


class FilterOtherException(Exception):

    def __init__(self, message):
        self.message = "Unknown Filter compile Error" + message
        super().__init__(self.message)
