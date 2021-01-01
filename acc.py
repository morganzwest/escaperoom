import datetime
import hub
import sys


def acc_write(arg_array: list):
    if len(sys.argv) < 5:
        arg_to_parse = ""
        for arg in sys.argv: arg_to_parse += (arg + ' ')
        arg_to_parse = arg_to_parse.strip()

        raise hub.errors.InputError(
            arg_to_parse,
            message = f"is an invalid argument. {__file__}.acc_write() requires exactly '3' input argument. For example: "
                      f"\"{__file__} acc_write <path> <mode> +<str>\"."
        )
    else:
        path = arg_array[0]  # The path to write the account too
        mode = arg_array[1]  # The mode to handle the file in

        string = "" # The output string to the file (including \n)
        for arg in arg_array[2:]:
            string += (arg + ' ')

        with open(path, mode) as f:
            f.write(string)


# Function Director # Example of 'sys.argv' = ['acc.py', 'function', 'arg1', 'arg2']
if len(sys.argv) > 1:
    if sys.argv[1] == "acc_write":
        acc_write(sys.argv[2:])
    else:
        raise hub.errors.InputError(
            sys.argv[0],
            message = f"{__file__}.__functiondirectories__ requires defining arguments. Arg index 1 is an invalid "
                      f"corresponding function index."
        )

else:
    raise hub.errors.InputError(
        sys.argv[0],
        message = f"{__file__} requires defining arguments. \"python3 acc.py <func> <*args>\"."
    )
