# quiz_exceptions.py

class InvalidAnswerError(Exception):
    def _init_(self, message="Answer must be a number."):
        super()._init_(message)