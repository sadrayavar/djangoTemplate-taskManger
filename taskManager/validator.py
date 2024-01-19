from django.core.exceptions import ValidationError

reservedWords = [
    "add",
    "delete",
    "edit",
    "myTasks",
    "register",
    "logout",
    "login",
    "profile",
    "admin",
    "account",
]


def validateReserved(text):
    global reservedWords
    if text in reservedWords:
        raise ValidationError("This name is reserved.")


def validateNumber(text):
    onlyNum = True
    for char in text:
        if char not in [str(i) for i in range(0, 10)]:
            onlyNum = False
    if onlyNum:
        raise ValidationError("Input cant be only numbers.")
