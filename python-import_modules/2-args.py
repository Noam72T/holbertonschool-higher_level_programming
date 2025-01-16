#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Retrieve command-line arguments, excluding the script name
    argv = sys.argv[1:]
    argc = len(argv)

    # Print the number of arguments
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    # Print each argument with its position
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
