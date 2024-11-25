import argparse

def parse_arguments():
    """
    Parse the arguments with argparse

    Returns:
        The populated namespace from the arguments
    """
    parser = argparse.ArgumentParser()
    parser.prog = "gcd"
    parser.description = ("This program calculates the Greatest Common Divisor (GCD) of two given numbers. "
                          "The numbers are provided by the user as command-line arguments. The result is printed to the console.")
    parser.add_argument("--number1", "-n1", type=int, help="The first number", required=True)
    parser.add_argument("--number2", "-n2", type=int, help="The second number",required=True)

    return parser.parse_args()

def gcd(a, b):
    """
    This function calculates the GCD of two numbers using the Euclidean algorithm.

    Args:
        a: The first number
        b: The second number
    """
    while b:
        a, b = b, a % b
    return a
def calculate_gcd(args):
    """
    This function calculates the GCD of the input numbers.

    Args:
        args: The populated namespace from the arguments
    """
    result = gcd(args.number1, args.number2)
    print(f"The GCD of {args.number1} and {args.number2} is: {result}")