import argparse

from . import add, div, mul, sub


def main() -> None:
    parser = argparse.ArgumentParser(description="Calc CLI")
    parser.add_argument("op", choices=["add", "sub", "mul", "div"])
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args()

    ops = {"add": add, "sub": sub, "mul": mul, "div": div}
    result = ops[args.op](args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()
