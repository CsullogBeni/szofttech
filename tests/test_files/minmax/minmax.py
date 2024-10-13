import argparse


def pars_arguments():
    """
    Parse the arguments with argparse

    Returns:
        The populated namespace from the arguments
    """
    parser = argparse.ArgumentParser()
    parser.prog = "Minmax"
    parser.description = ("This program can select the maximum or the minimum from the given numbers."
                          "Numbers given from the user as the command line arguments. The program select maximum by "
                          "default, but user can ask minimum by --min flag. The result is printed to the console.")
    parser.add_argument("--min", action="store_true", help="Whether user wants minimum selection")
    parser.add_argument("numbers", type=float, nargs="+", help="Numbers to select maximum or minimum from")

    return parser.parse_args()


def minmax_selection(args):
    """
    This function defines the maximum or the minimum from the numbers given from the user as the command line arguments.
    Maximum or minimum selection depends on the user.
    The result is printed to the console.

    Args:
        args:       The populated namespace from the arguments
    """
    if args.min:
        print("Minimum of the numbers:", min(args.numbers))
    else:
        print("Maximum of the numbers:", max(args.numbers))


if __name__ == "__main__":
    """call the parser and the minmax_selection method"""
    parsed_args = pars_arguments()
    minmax_selection(parsed_args)
