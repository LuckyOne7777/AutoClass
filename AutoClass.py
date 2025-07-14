import argparse

def generate_class(class_name, vars):
    print(f"\nclass {class_name}:\n")
    print(f"    def __init__(self, {', '.join(vars)}):")
    for v in vars:
        print(f"        self.{v} = {v}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Class name")
    parser.add_argument("--vars", nargs="+", help="Variable names")

    args = parser.parse_args()

    if not args.name or not args.vars:
        args.name = input("Class name: ")
        args.vars = input("Vars (comma-separated): ").replace(" ", "").split(",")

    generate_class(args.name, args.vars)
