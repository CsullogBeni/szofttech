# Implement a calculator program, that can add, subtract, multiply and divide two numbers.
#  - Numbers and operators given from the user as the command line arguments.
#  - Consider using argpasre library.
#  - Consider using eval builtin function.
#  - Print or log the result.
import argparse

def check_number(value):
    try:
        float(value)
        return value
    except ValueError:
        raise argparse.ArgumentTypeError("Argument is not a number")

parser = argparse.ArgumentParser()
parser.add_argument("number1", type=check_number, help="First number")
parser.add_argument("number2", type=check_number, help="Second number")
parser.add_argument("operation", choices=["+", "-", "*", "/"], help="Operation")

args = parser.parse_args()

operation_string = args.number1 + " " + args.operation + " " + args.number2
result = eval(operation_string)
print("Result:", operation_string, "=", result)