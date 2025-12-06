#!/usr/bin/env python3

import sys
import random
import string


def usage():
    print("Usage: python3 password-generator.py <length>")
    print("Example: python3 password-generator.py 16")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()

    try:
        length = int(sys.argv[1])
        if length <= 0:
            raise ValueError
    except ValueError:
        print("Error: <length> must be a positive integer.")
        usage()

    charset = string.ascii_letters + string.digits

    password = "".join(random.choice(charset) for _ in range(length))
    print(password)
