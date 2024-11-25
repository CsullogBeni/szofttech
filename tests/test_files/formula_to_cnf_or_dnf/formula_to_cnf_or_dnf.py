import argparse
from sympy.logic.boolalg import to_cnf, to_dnf


def parse_arguments():
    """
    Parse the arguments with argparse

    Returns:
        The populated namespace from the arguments
    """
    parser = argparse.ArgumentParser()
    parser.prog = "FormulaToCNForDNF"
    parser.description = ("This program can convert a formula to conjunctive normal form or disjunctive normal form."
                          "Negation: ~, disjunction: |, conjunction: &, implication: >>")
    parser.add_argument("--formula", "-f", type=str, help="The formula, which has to be convert")
    parser.add_argument("--conversion", "-c", choices=["cnf", "dnf"], help="Which conversion has to be done")

    return parser.parse_args()


def conversion(args):
    """
    This function makes the required conversion.
    Type of the conversion depends on the user.
    The result is printed to the console.

    Args:
        args:       The populated namespace from the arguments
    """
    if args.conversion == "cnf":
        print("Cnf:", to_cnf(args.formula))
    else:
        print("Dnf:", to_dnf(args.formula))


if __name__ == "__main__":
    """call the parser and the minmax_selection method"""
    parsed_args = parse_arguments()
    conversion(parsed_args)
