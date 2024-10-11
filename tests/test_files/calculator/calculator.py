"""Calculator runnable
This is a calculator program, that can add, subtract, multiply and divide two numbers. Numbers and operators given from the user as the command line arguments.
The result is printed to the console.

Args:
    number1: First number to do operation with
    number2: Second number to do operation with
    operation: Operation, which can be: +, -, *, /

"""
import argparse
from os import name


def pars_arguments():
    """
    Parse the arguments with argparse

    Returns:
        The populated namespace from the arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", type=float, help="First number to do operation with", required=True)
    parser.add_argument("number2", type=float, help="Second number to do operation with")
    parser.add_argument("--operation", choices=["+", "-", "*", "/"], help="Operation, which can be: +, -, *, /", default="+")

    return parser.parse_args()

def get_operation_string():
    """
    Get the parsed parameters using pars_arguments() function and create the string format of the operation to be performed
    Returns:
        The string format of the operation to be performed
    """
    args = pars_arguments()
    if args.operation == "/" and args.number2 == 0:
        raise ZeroDivisionError()

    return str(args.number1) + " " + args.operation + " " + str(args.number2)


operation_string = get_operation_string()
result = eval(operation_string)
print("Result:", operation_string, "=", result)

if name == 'main':
    """call the parser and the evaluator method"""