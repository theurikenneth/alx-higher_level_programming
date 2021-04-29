#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    """Throws an error if arguments are not 3"""
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    """Defines operator and checks whether it is an operator"""
    ops = {"+": add, "-": sub, "*":mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operator: +, -, * and /")
        sys.exit(1)

    """Casts a and b into integers and assumes all arguments are castable into integers"""
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    """prints a, operator and b as they are arguments 1, 2 and 3 and displays the answer"""
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
