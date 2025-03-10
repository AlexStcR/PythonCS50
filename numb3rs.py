import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        ip_pattern = r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$"

        numbers = ip.split(".")

        int_numbers = []
        for item in numbers:
            if item.isalpha():
                return False
            else:
                int_numbers.append(int(item))
    # print(int_numbers)
        match = re.search(ip_pattern, ip)

        for i in int_numbers:
            # print(i)
            if i < 0 or i > 255:

                return False

        if match:
            return True
        else:
            return False

    except (ValueError):
        return False


if __name__ == "__main__":
    main()
