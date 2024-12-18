import argparse
from random import randint

def parse_arguments():
    """
    Parse the arguments with argparse

    Returns:
        The populated namespace from the arguments
    """
    parser = argparse.ArgumentParser()
    parser.prog = "Random List Generator"
    parser.description = "Generates a random list of integers"
    parser.add_argument("--count", "-c", type=int, help="How many integers to generate", required=True)
    parser.add_argument("--lowerbound", "-lb", type=int, help="Lower bound, defaults to 0", default=0)
    parser.add_argument("--upperbound", "-ub", type=int, help="Upper bound, defaults to the integer limit", default=2147483647)

    return parser.parse_args()

def generate(args):
    """
    Generates random numbers seperated by spaces. Count and bounds specified by the args parameter.

    Args:
      args:  The populated namespace from the arguments
    """
    l = [randint(args.lowerbound, args.upperbound) for _ in range(0, args.count)]
    print(*l, sep=' ')


if __name__ == "__main__":
    parsed_args = parse_arguments()
    generate(parsed_args)
