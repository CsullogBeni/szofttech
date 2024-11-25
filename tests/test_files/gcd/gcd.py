import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.prog = "gcd"
    parser.description = ("This program calculates the Greatest Common Divisor (GCD) of two given numbers. "
                          "The numbers are provided by the user as command-line arguments. The result is printed to the console.")
    parser.add_argument("--number1", "-n1", type=int, help="The first number", required=True)
    parser.add_argument("--number2", "-n2", type=int, help="The second number",required=True)

    return parser.parse_args()