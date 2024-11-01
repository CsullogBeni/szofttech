import argparse


def pars_arguments():
    """
    Parse the arguments with argparse

    Returns:
        The populated namespace from the arguments
    """
    parser = argparse.ArgumentParser()
    parser.prog = "Calculator"
    parser.description = ("This program can add, subtract, multiply and divide two numbers. Numbers and operators "
                          "given from the user as the command line arguments. The result is printed to the console.")
    parser.add_argument("--number1", "-n1", type=float, help="First number to do operation with", required=True)
    parser.add_argument("--number2", "-n2", type=float, help="Second number to do operation with")
    parser.add_argument("--operation", "-o", choices=["+", "-", "*", "/"], help="Operation, which can be: +, -, *, /",
                        default="+")

    return parser.parse_args()


def get_operation_string(args):
    """
    Create the string format of the operation to be performed if the operation is mathematically possible

    Args:
        args:       The populated namespace from the arguments
    Returns:
        The string format of the operation to be performed
    """
    if args.operation == "/" and args.number2 == 0:
        raise ZeroDivisionError()

    return str(args.number1) + " " + args.operation + " " + str(args.number2)


def calculate(args):
    """
    This function can add, subtract, multiply and divide two numbers.
    Numbers and operators given from the user as the command line arguments.
    The result is printed to the console.

    Args:
        args:       The populated namespace from the arguments
    """
    operation_string = get_operation_string(args)
    result = eval(operation_string)
    print("Result:", operation_string, "=", result)


if __name__ == "__main__":
    """call the parser and the evaluator method"""
    parsed_args = pars_arguments()
    calculate(parsed_args)
