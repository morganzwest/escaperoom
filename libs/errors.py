from colorama import Fore, init

init()

class InputError(Exception):

    # Custom error arguments
    def __init__(self, inp: str, message = f"does not conform with file {__file__}."):
        self.input = inp
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{Fore.RED}\nUnprocessable Entity Error\n\'{self.input}\' {self.message} {Fore.BLUE}\nError Code : 422'


# ERROR CODE LOOKUP #
"""
    422 - (Unprocessable Entity Error) : Input Error
    
"""