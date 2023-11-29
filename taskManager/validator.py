from django.core.exceptions import ValidationError
from taskManager.constant import reservedWords


def validateReserved(text):
    if text in reservedWords:
        raise ValidationError("This name is reserved.")


def validateNumber(text):
    onlyNum = True
    for char in text:
        if char not in [str(i) for i in range(0, 10)]:
            onlyNum = False
    if onlyNum:
        raise ValidationError("Input cant be only numbers.")
