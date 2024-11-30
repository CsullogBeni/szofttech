import argparse


def parse_arguments():
    """
    Parse the arguments with argparse

    Returns:
        The populated namespace from the arguments
    """
    parser = argparse.ArgumentParser()
    parser.prog = "AlphabeticalOrder"
    parser.description = ("This program gives the alphabetical ordered form of a given string list. "
                          "Strings given from the user as the command line arguments. The program orders asc by "
                          "default, but user can ask desc by --desc flag. The result is printed to the console.")
    parser.add_argument("--desc", "-d", action="store_true", help="Whether user wants desc order")
    parser.add_argument("--list", "-l", type=str, nargs="*", help="List of strings")

    return parser.parse_args()


def alphabetical_order(args):
    """
    This function creates the ordered list of the given list from the user as the command line arguments.
    Order direction depends on the user.
    The result is printed to the console.

    Args:
        args:       The populated namespace from the arguments
    """
    args.list.sort(reverse=args.desc)
    print("Ordered list:", args.list)


if __name__ == "__main__":
    """call the parser and the alphabetical_order method"""
    parsed_args = parse_arguments()
    alphabetical_order(parsed_args)
